# wandb. weights and biases

Библиотека и сервис для сбора информации о обучении моделей

- логирование на сервис в реальном времени для построению кривых обучение
- сбор информации об отдельных запусках моделей с отображением статистики и произвольной модели
- различные визуализации 


1. Зарегестрироваться в https://wandb.ai/

2. Создать проект в котором будут собрана вся нформациия о моделях и их запусках

3. Установить библиотеку 

```python
%%capture
!pip install wandb -qqq
import wandb
```

4. Подключится для удалённого логирования

`!wandb login`

5. Инициализировать сессию для загрузки информации об отдельном запуске
```python
wandb.init(project="project name",   # один проект на много запусков
           config={                   # словарь с описанием текущего запуска. ключи -- произвольные
    "learning_rate": 1e-3,
    "net": "CNN3 (skip-connection, sum)",
    "params": sum(p.numel() for p in my_model.parameters() if p.requires_grad)      # подсчёт числа параметров модели
})
```


6. Сохранить модель
```
    # WandB – Save the model checkpoint. This automatically saves a file to the cloud and associates it with the current run.
    torch.save(model.state_dict(), "model.h5")
    wandb.save('model.h5')
```


6. Логировать серийную информацию. Автоматически будут построены графики на странице проекта
```
wandb.log({"train loss":loss.item(), "train acc":AccTrain[-1], "val loss":loss_val.item(), "val acc":AccVal[-1]})
```
Можно сохранять в том числе изображения (pytorch Images). По одному или все разом:
```python
wandb.log({"val\test misprediction" : [wandb.Image(img) for img in mispredicted]})
```

7. Сохранить не серийную информацию:

```python
# после обучения можно в текущий запуск записать конечные параметры
wandb.run.summary['accuracy'] =  accuracy_score(ytest, ypred)
wandb.run.summary['f1'] =  f1_score(ytest, ypred)
```

8. Одно выполнение (Run) завершится автоматически, как только будет снова вызвано `wandb.init`. Но можно завершить вручную
```python
wandb.sdk.wandb_run.finish()
```
Обычно завершение одного Выполнения занимает какое-то время. 
