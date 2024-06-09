# wandb. Weights and Biases

Библиотека и сервис для сбора информации об обучении моделей.

- Логирование на сервис в реальном времени для построению кривых обучения
- Сбор информации об отдельных запусках моделей (нейросетевых и не только) с отображением статистики и произвольной модели
- Интеграция с пакетами: Pytorch, Keras[[doc](https://docs.wandb.ai/guides/integrations/keras)], TensorFlow, SKlearn [[doc](https://docs.wandb.ai/guides/integrations/scikit)] и др.
- Создание отчётов и различных визуализаций показателей обучения, гиперпараметров и т.п.
- Возможность делиться (по ссылке) отчётом или данными об обучении модели
- Сохранение моделей, их гиперпараметров, ноутбуков, небольших датасетов и т.п. [[doc](https://docs.wandb.ai/guides/artifacts)]


1. Зарегистрироваться в https://wandb.ai. Есть регистрация через аккаунт гугл.

2. Создать проект в котором будут собрана вся информация о моделях и их запусках.

3. Установить библиотеку wandb для Python

```python
%%capture
!pip install wandb -qqq
import wandb
```

4. Войти в аккаунт для удалённого логирования

В Jupyter Notebook (google collab):
```python
wandb.login()
```

или

`!wandb login`

    Авторизация из ноутбука kaggle:
    1. Получить ключ `!wandb login`
    2. Добавить его в хранилище secrets среды Kaggle: menu Add-ons - Secrets, задать имя (например my_wandb_key)
    3. Обратиться к сохранённому ключу из ноутбука, авторизоваться:
    ```python
    from kaggle_secrets import UserSecretsClient
    user_secrets = UserSecretsClient() 
    personal_key_for_api = user_secrets.get_secret("my_wandb_key")
    !wandb login $personal_key_for_api
    ```


5. Инициализировать сессию для загрузки информации об отдельном случае (run) обучения модели
```python
wandb.init(project="project name",   # один проект на много запусков
           config={                   # словарь с описанием текущего запуска. ключи -- произвольные
    "learning_rate": 1e-3,
    "net": "CNN3 (skip-connection, sum)",
    "params": sum(p.numel() for p in my_model.parameters() if p.requires_grad)      # подсчёт числа параметров модели
})
```
В словарь стоит записывать все основные гиперпараметры модели и параметры процесса обучения:
- название модели (описание гиперпараметров) или нейросети (её архитектуры НС, число слоёв, число нейронов, функции активации, ... )
  - веса можно НС сохранить отдельно
  - число параметров можно подсчитывать автоматически
- метод оптимизации весов (если меняется)
- функцию потерь
- learning rate и параметры его изменения
- информация о обучающей выборке: размер батча, аугментация, способы предобработки
- информацию о количестве объектов в обучающих выборках, количестве признаков
- информацию о способе подготовки данных (кодирование, нормализация, очистка, балансировка классов и т.п.)

По умолчанию при вызове init в wandb сохраняется и текущая версия ноутбука, гда эта функция вызвана.
https://docs.wandb.ai/guides/app/features/panels/code. Просмотреть код можно на вкладке Code, на странице запуска (run).

После нескольких запусков функции init можно получить таблицу вида:\
![](img/wandb-table.png)\


6. Сохранить модель на сервере wandb
```
    # WandB – Save the model checkpoint. This automatically saves a file to the cloud and associates it with the current run.
    torch.save(model.state_dict(), "model.h5")
    wandb.save('model.h5')
```


6. *Для нейросети или модели с итерационным методом обучения.*
Логировать серийную информацию во время обучения. Автоматически будут построены кривые обучения (здесь функции потерь и общей точности) на странице проекта. Эти кривые будут обновляться по мере добавления данных
```
wandb.log({"train loss":loss.item(), "train acc":AccTrain[-1], "val loss":loss_val.item(), "val acc":AccVal[-1]})
```
Пример графиков\
![](img/wandb-learning-curve.png)
Здесь видно как обучались разные модели с разными параметрами

Можно сохранять в том числе изображения (pytorch Images). По одному или все разом:
```python
wandb.log({"val\test misprediction" : [wandb.Image(img) for img in mispredicted]})
```

Интеграция с keras для логирования
```python
import wandb
from wandb.keras import WandbMetricsLogger, WandbModelCheckpoint
...

# Pass the WandbModelCheckpoint to model.fit
model.fit(
    X_train,
    y_train,
    validation_data=(X_test, y_test),
    callbacks=[
        WandbMetricsLogger(),                    # логировать лосс и доступные метрики
        WandbModelCheckpoint("models"),          # сохранять модель
    ],
)
```


7. Сохранить не серийную информацию, результаты обучения:

```python
# после обучения можно в текущий запуск записать конечные параметры
wandb.run.summary['accuracy'] =  accuracy_score(ytest, ypred)
wandb.run.summary['f1'] =  f1_score(ytest, ypred)
```



8. Один Сеанс (Run) завершится автоматически, как только будет снова вызвано `wandb.init`. Но можно завершить вручную
```python
wandb.sdk.wandb_run.finish()
```
Обычно завершение одного Cенаса (Run) происходит не мгновенно.

После сбора информации об отдельных Сеансах составляется отчёт, который включает кривые обучения и диаграмму влияния параметров на конечный результат. Например, график в параллельных координатах\
![](img/wandb-report1.png)



**Артефакты**
При обучении можно сохранять отдельные данные (в wandb они называются артефактами). Например можно сохранять небольшие файлы, датасеты или результаты их обработки.

# См. также похожие интструменты
neptune.ai, comet_ml, mlflow

Короткий обзор: https://neptune.ai/blog/weights-and-biases-alternatives

# Ссылки
- Пример интеграции WandB и SKLearn: https://colab.research.google.com/github/wandb/examples/blob/master/colabs/scikit/Simple_Scikit_Integration.ipynb#scrollTo=qpcQ2HDs5LQ2