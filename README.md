# Введение в ИИ

### [Курс 2022](2022/readme.md)

### [Курс 2022. Заочное. Осень](dist/2022/fall.md)

## План
- Небольшой чеклист по математике: https://habr.com/ru/company/ruvds/blog/676114/

1. Введение. (Философские измышления)
2. Машинное обучение (общие принципы, решаемые задачи, обзор методов, способы оценки моделей).
3. Деревья решений (классификация)
4. K-means (кластеризация).
5. Нейросети
    - введения (мат. модели, свойства, задачи, линейная разделимость)
    - персептрон (Розенблатта, многослойный, алгоритмы: обратного распространения ошибки и стохастический градиентный спуск)
    - сети с обратными связями
    - нелинейная разделимость, радиально-базисные сети
    - самоорганизующиеся сети( кластеризация и классификация на них)
    - свёрточные сети (когнитрон, неокогнитрон, сверточные сети)
    - глубокое обучение нейронных сетей
    - предобработка данных
6. Не нейросетевые методы
    - Методы опорных векторов
    - логистическая регрессия
    - методы ансамблей
    - случайный лес.

## Примеры
1. Обработка данных: https://colab.research.google.com/drive/1kLfmJ4q81BNZtMs-oVX9cKJGsT3mYWmR?usp=sharing
2. Классификация, персептрон (Keras, pytorch): https://colab.research.google.com/drive/1YtK4an7UAhnxTmhmQzZd6Eo3esfv6TL3?usp=sharing
4. Классикация изображений, CNN, предобученные сети (keras): https://colab.research.google.com/drive/1kqSiP9IpPmW8dw9NxV5Sm5pMLMqfINZb?usp=sharing
1. Интерактивные графики, уменьшение размерности, веб-формы (plotly, PCA, gradio): https://colab.research.google.com/drive/1SzAlYDLpjf65nnRbTVRtFxUWuyJnA8_s?usp=sharing
5. Отслеживание метрик моделей: [wandb.md](wandb.md)
6. Простые примеры использования RNN (pytorch, LSTM, MNIST): https://colab.research.google.com/drive/1XXQgLdECny8MvO8VVcEn3-cM1TW8pdHK?usp=sharing
7. Временной ряд, RNN, LSTM: https://colab.research.google.com/drive/1IDf2w2WFmkcSG70-3Fl-Ylx1aDbHJoQc?usp=sharing
8. Обработка данных, деревья решений, случайный лес, апсемлинг (ADASYN) и андерсемплинг (TomekLinks): https://colab.research.google.com/drive/1oudif62hPceY8h_1kOXd8A8QoPh2gTT7?usp=sharing
9. [Предобработка текста, TF-IDF, SVM](https://github.com/ivtipm/ML/blob/main/examples/text/text_preprocess.md)
10. [Классификация текстов, Embeddings, LSTM (Keras)](https://github.com/ivtipm/ML/blob/main/examples/text/text_keras.md)
11. Кластеризация https://colab.research.google.com/drive/1OjrSLj2hWx-0AqZtTc4ydOH5d22DFDxf


## [Задания 2021](tasks/tasks.md)


[Заочное: занятия 30 ноября - 9 декабря 2020](https://github.com/ivtipm/ML/blob/main/dist2020/lessons.md) (заочное)


# Ссылки
## Теория
- Классические методы МО и начало НС: https://ml-handbook.ru (материаля ШАД Яндекса)
- Основы нейрокомпьютерных систем [Текст] : учебное пособие / Д. А. Семигузов
- Deep Learning with PyTorch, Eli Stevens, Luca Antiga, Thomas Viehmann --  теория + PyTorch

### Python
- Изучаем Python. Лутц Марк
- Программируем на Python. Лутц Марк
- https://stepik.org/course/67/syllabus
- https://github.com/VetrovSV/Programming

## Курсы по глубокому обучению
- [stepik:Deep Learning (семестр 1, осень 2020)](https://stepik.org/course/82177/promo). Введение в МО, обработка изображений.
- [stepik:Deep Learning (семестр 2)](https://stepik.org/course/65855/syllabus). Посвящённый обработке текстов и аудиозаписей (материалы доступны, начнётся заново осенью 2021)

## Для практики
- [Dive into Deep Learning](http://d2l.ai/index.html) -- книжка (eng) по глубокому обучению, с примерами и заданиями.
- [ODS: competitions](http://d2l.ai/index.html) -- соревнования по МО
- [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php) -- большая коллекция датасетов
- [Kaggle](https://www.kaggle.com/)

## ПО
- [PyCahrm](https://www.jetbrains.com/ru-ru/pycharm/download/)
- [google colaboratory](https://colab.research.google.com) -- для запуска кода на python и обучения НС на GPU
- [Anaconda](https://www.anaconda.com/products/individual) -- дистрибутив для научных вычислений на Python

### Библиотеки
- [sklearn](https://scikit-learn.org/stable/) -- классические мтоды МО (python)
- [keras](https://keras.io/) -- глубокое обучение (python)
- [pytorch](https://pytorch.org/) -- популярный и гибкий фреимвок для МО
- [gradio](https://gradio.app/getting_started/) -- для быстрого создания веб-интерфесов
- [wandb](https://wandb.ai/site) -- библиотека и интернет-сервис для отслеживания процесса обучения моделей, сравнения метрик моделей

## Датасеты
1. [Ирисы Фишера -- задача классификации](https://archive.ics.uci.edu/ml/datasets/iris)
2. [Классификация: доходы (Adult Data Set)](https://archive.ics.uci.edu/ml/datasets/adult)
3. https://github.com/ivtipm/ML/tree/main/datasets

### Дополнительно
- Портал открытых данных РФ http://data.gov.ru/
- Пакеты открытых данных https://hubofdata.ru/datase
