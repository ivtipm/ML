# Машинное обучение

### [Магистратура. Осень. Нейросети](plans/2024_NN.md)
### [Магистратура. Очное. 2024. Методы машиннного обучения](plans/2024_plan.md)
### [Магистратура. Заочное. 2024. Методы машиннного обучения.](plans/2024_distance.md)
### [ДПО Курс. 2024. Весна. Машинное обучение](plans/facultative_2024_ML.md)

##### [Курс 2023. Осень. Нейросети](plans/2023_NN.md)
##### [Курс 2023. Весна. Методы МО](ML/readme.md)
##### [Курс 2022. Заочное. Осень](dist/2022/fall.md), [Курс 2023 (продолжение). Заочное. Весна](dist/2023/plan_ivtm-21.md)

Старые задания:
- [Курс 2022](2022/readme.md)
- [Задания 2021](tasks/tasks.md)
- [Заочное: занятия 30 ноября - 9 декабря 2020](https://github.com/ivtipm/ML/blob/main/dist2020/lessons.md) (заочное)

# Темы, важные для дальнейшего освоения МО
- Небольшой чеклист по математике: https://habr.com/ru/company/ruvds/blog/676114/
- Короткая шпаргалка по Python: https://miro.com/app/board/uXjVORmoCO0=/?moveToWidget=3458764545754982875&cot=14


## Примеры
### Анализ данных и классические методы МО
0. Python. Настройка рабочего окружения. Виртуальное окружение. Pip. Jupyter Notebook. Jupyter lab. Google Colab. [todo:] https://miro.com/app/board/uXjVNQC1rq8=/?share_link_id=860218532001
1. Разведочный анализ данных (exploratory data analysis, EDA), визуализация и подготовка данных для моделей МО. [pandas, numpy, matplotlib, seaborn]
   [colab.research.google.com/drive/1kLfmJ4q81BNZtMs-oVX9cKJGsT3mYWmR](https://colab.research.google.com/drive/1kLfmJ4q81BNZtMs-oVX9cKJGsT3mYWmR?usp=sharing)
1. Задача регрессии. Метод линейной регрессии. Теория + пример: [Линейная регрессия. МНК. Метод макс.правдоподобия. sklearn.ipynb colab.research.google.com/drive/1YadlNYk9_WkCQY6L-HKP9SI7xZjuzIMx](https://colab.research.google.com/drive/1YadlNYk9_WkCQY6L-HKP9SI7xZjuzIMx?usp=sharing)
1. Задача классификации. Линейная разделимость классов. Сигмоида. Вероятностная модель; SoftMax. LogLoss. 
   - [colab.research.google.com/drive/1AdbtsRkX0jRVByuAKJxchYPcciTgFpqh?usp=sharing](https://colab.research.google.com/drive/1AdbtsRkX0jRVByuAKJxchYPcciTgFpqh?usp=sharing)
1. Метод опорных векторов (Support Vector Machine, SVM) и метод k-ближайших соседей (k-nearest neighbors).
   - [colab.research.google.com/drive/1oh7-ID00MN-AoJtAm4uL-bj0sqf5ieuk?usp=sharing](https://colab.research.google.com/drive/1oh7-ID00MN-AoJtAm4uL-bj0sqf5ieuk?usp=sharing)
2. Решающие деревья (Decision Tree). Ансамбли моделей (ensembles): Беггинг (bagging), Бустинг (адаптивный и градиентный), Стекинг, Голосование. [colab.research.google.com/drive/1Bin_h7BPSfnxs4Pea7eibceNMkOEcKmg?usp=sharing](https://colab.research.google.com/drive/1Bin_h7BPSfnxs4Pea7eibceNMkOEcKmg?usp=sharing)
3. Кластеризация. Диаграммы рассеивания. Seaborn.
    - [учебное пособие](https://raw.githubusercontent.com/ivtipm/ML/main/%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%20%D0%B8%20%D0%B2%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8%20%D1%8D%D0%BA%D1%81%D0%BF%D0%B5%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.pdf#page=111)
4. Уменьшение размерности. PCA (Principal component analysis ). UMAP. [seaborn, plotly]. 
Кластеризация. KMeans. Метод локтя. Коэффициент силлуэта. [colab.research.google.com/drive/1OjrSLj2hWx-0AqZtTc4ydOH5d22DFDxf](https://colab.research.google.com/drive/1OjrSLj2hWx-0AqZtTc4ydOH5d22DFDxf)

5. Временные ряды (time series). 
- Разложение. Начальный анализ. Простые модели: [sktime, statmodels]: https://colab.research.google.com/drive/1hgFTqkfu37v7PQAR9JYcH610FJdXOP-b#scrollTo=Hj0GjwJKVawA
- Стационарность. Тренд, сезонность, шум. Методы: AR, MA, ARMA, ARIMA, SARIMA. Пакет Facebook Prophet. https://colab.research.google.com/drive/1ZOOJK2-9mYED6WiMRnFAe74miSfjKHxG

6. [Предобработка текста, TF-IDF, SVM](https://github.com/ivtipm/ML/blob/main/examples/text/text_preprocess.md)



### Основы глубокого обучения
3. Классификация, персептрон (Keras, pytorch): [colab.research.google.com/drive/1YtK4an7UAhnxTmhmQzZd6Eo3esfv6TL3](https://colab.research.google.com/drive/1YtK4an7UAhnxTmhmQzZd6Eo3esfv6TL3?usp=sharing)
    - шпаргалка по pytorch: [torch.md](torch.md)
4. Классификация изображений, CNN, предобученные сети (keras): [colab.research.google.com/drive/1kqSiP9IpPmW8dw9NxV5Sm5pMLMqfINZb](https://colab.research.google.com/drive/1kqSiP9IpPmW8dw9NxV5Sm5pMLMqfINZb?usp=sharing)


6. Простые примеры использования RNN (pytorch, LSTM, MNIST): [colab.research.google.com/drive/1XXQgLdECny8MvO8VVcEn3-cM1TW8pdHK](https://colab.research.google.com/drive/1XXQgLdECny8MvO8VVcEn3-cM1TW8pdHK?usp=sharing)
7. Временной ряд, RNN, LSTM: [colab.research.google.com/drive/1IDf2w2WFmkcSG70-3Fl-Ylx1aDbHJoQc](https://colab.research.google.com/drive/1IDf2w2WFmkcSG70-3Fl-Ylx1aDbHJoQc?usp=sharing)
8. Обработка данных, деревья решений, случайный лес, апсемлинг (ADASYN) и андерсемплинг (TomekLinks): [colab.research.google.com/drive/1oudif62hPceY8h_1kOXd8A8QoPh2gTT7](https://colab.research.google.com/drive/1oudif62hPceY8h_1kOXd8A8QoPh2gTT7?usp=sharing)

10. [Классификация текстов, Embeddings, LSTM (Keras)](https://github.com/ivtipm/ML/blob/main/examples/text/text_keras.md)
    - http://nlpprogress.com — каталог последних достижений и дастасетов по областям NLP 

11. Пример использования BERT для создания векторных представлений текстов: https://colab.research.google.com/drive/1Aacg8tUXXNICQ0SetvqoIPD7GXnm0Ymx?usp=sharing

### Разное
1. Интерактивные графики, уменьшение размерности, веб-формы (plotly, PCA, gradio): [colab.research.google.com/drive/1SzAlYDLpjf65nnRbTVRtFxUWuyJnA8_s](https://colab.research.google.com/drive/1SzAlYDLpjf65nnRbTVRtFxUWuyJnA8_s?usp=sharing)
5. Отслеживание метрик моделей: [wandb.md](wandb.md)






# Ссылки
## Теория
- Классические методы МО и начало НС: [https://academy.yandex.ru/handbook/ml](https://academy.yandex.ru/handbook/ml) (материалы ШАД Яндекса)
- Теория по классическим методам МО с интерактивынми примерами: [mlu-explain.github.io](https://mlu-explain.github.io/)
- Основы нейрокомпьютерных систем [Текст] : учебное пособие / Д. А. Семигузов
- Deep Learning with PyTorch, Eli Stevens, Luca Antiga, Thomas Viehmann — теория + PyTorch
- шапаргалка по МО https://ml-cheatsheet.readthedocs.io/en/latest/index.html

### Python
- Изучаем Python. Лутц Марк
- Программируем на Python. Лутц Марк
- https://stepik.org/course/67/syllabus
- https://github.com/VetrovSV/Programming

## Курсы по глубокому обучению
- [stepik:Deep Learning (семестр 1, осень 2020)](https://stepik.org/course/82177/promo). Введение в МО, обработка изображений.
- [stepik:Deep Learning (семестр 2)](https://stepik.org/course/65855/syllabus). Посвящённый обработке текстов и аудиозаписей (материалы доступны, начнётся заново осенью 2021)

## Для практики
- [Dive into Deep Learning](http://d2l.ai/index.html) — книжка (eng) по глубокому обучению, с примерами и заданиями.
- [ODS: competitions](http://d2l.ai/index.html) — соревнования по МО
- [Kaggle](https://www.kaggle.com/)

## ПО
- [google colaboratory](https://colab.research.google.com) — для запуска кода на python и обучения НС на GPU
- [Anaconda](https://www.anaconda.com/products/individual) — дистрибутив для научных вычислений на Python
- DataSpell (бесплатно для студентов)
- [PyCahrm](https://www.jetbrains.com/ru-ru/pycharm/download/)

### Библиотеки
- [sklearn](https://scikit-learn.org/stable/) — классические мтоды МО (python)
- [keras](https://keras.io/) — глубокое обучение (python)
- [pytorch](https://pytorch.org/) — популярный и гибкий фреимвок для МО
- [gradio](https://gradio.app/getting_started/) — для быстрого создания веб-интерфесов
- [wandb](https://wandb.ai/site) — библиотека и интернет-сервис для отслеживания процесса обучения моделей, сравнения метрик моделей

## Датасеты
1. [Классификация: Ирисы Фишера](https://archive.ics.uci.edu/ml/datasets/iris) (небольшой простой датасет)
2. [Классификация: пингвины](https://github.com/allisonhorst/palmerpenguins) (небольшой простой датасет)
3. [Классификация: доходы (Adult Data Set)](https://archive.ics.uci.edu/ml/datasets/adult)\
Каталоги датасетов:
5. https://github.com/ivtipm/ML/tree/main/datasets
6. https://huggingface.co/datasets
7. https://www.kaggle.com/datasets
8. https://pytorch.org/text/stable/datasets.html#text-classification — текстовые дастасеты pytorch
9. [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php) — большая коллекция датасетов
10. https://commoncrawl.org/overview - текстовые датасеты собранные со всего интернета, терабайты данных 

### Дополнительно
- Портал открытых данных РФ http://data.gov.ru/
- Пакеты открытых данных https://hubofdata.ru/datase
