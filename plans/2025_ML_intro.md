# Введение в разработку интеллектуальных систем

## После освоения курса Вы сможете
* Ориентироваться в основных понятиях машинного обучения (МО): виды МО, данные, модели, методы МО и т.д.

* Понимать жизненный цикл ML-проекта и выбирать подходящие этапы: сбор данных, анализ данных, подготовка данных, обучение модели, валидация модели, создание приложения на основе модели.

* Обучать и оценивать простые модели надёжно: линейная/логистическая регрессия; строить пайплайны и кросс-валидацию.

* Выбирать и интерпретировать ключевые метрики качества (MAE/MSE/R², Accuracy/Precision/Recall/F1) и диагностировать переобученеи и недообучение.

* Сериализовать модель и подготовить минимальный интерфейс/API (Gradio/FastAPI) для демонстрации результата.


# План
1. Основы ИИ: определения ИИ, машинного обучения (МО) и их взаимосвязь; отличие от классического программирования; примеры применения. История ИИ. [слайды - 1](https://docs.google.com/presentation/d/11zFsnGJAaCzFGGVAjrd_OyNGD-fB6uLr3R-azaof0Qk)

2. Жизненный цикл ML-проекта: этапы от бизнес-задачи до развертывания; CRISP-DM.  [слайды - 1](https://docs.google.com/presentation/d/11zFsnGJAaCzFGGVAjrd_OyNGD-fB6uLr3R-azaof0Qk)

3. Данные для МО: понятия признак (feature) и целевая переменная (target), типы данных, концепция разведочного анализа данных (EDA). [слайды - 1](https://docs.google.com/presentation/d/11zFsnGJAaCzFGGVAjrd_OyNGD-fB6uLr3R-azaof0Qk), [слайды - 2](https://docs.google.com/presentation/d/1mK9CfhwjQtAdJZENV3vU4nCGSkzI8_Ugkv_AavBVEaM)

4. Обучения с учителем: задачи регрессии и классификации; разделение данных на обучающую (train) и тестовую (test) выборки. [слайды - 1](https://docs.google.com/presentation/d/11zFsnGJAaCzFGGVAjrd_OyNGD-fB6uLr3R-azaof0Qk)

5. Простые модели: линейная и логистическая регрессия. Функции потерь: MSE, LogLoss. Использование scikit-learn: fit, predict.
    - Линейная регрессия: модель и пример: https://colab.research.google.com/drive/1YadlNYk9_WkCQY6L-HKP9SI7xZjuzIMx
    - Логистическая регрессия: мдель и пример: https://colab.research.google.com/drive/1AdbtsRkX0jRVByuAKJxchYPcciTgFpqh?usp=sharing#scrollTo=UmtvOZb6DzgM

6. Качество модели: метрики для регрессии (MAE, MSE, R²), метрики для классификации (Accuracy, Precision, Recall, F1-score), матрица ошибок, визуальное объяснение недообучения (underfitting) и переобучения (overfitting). Воспроизводимость экспериментов. [слайды - 2](https://docs.google.com/presentation/d/1mK9CfhwjQtAdJZENV3vU4nCGSkzI8_Ugkv_AavBVEaM)

7. Другие парадигмы в ИИ (Обзор): обучение без учителя (Unsupervised Learning), кластеризация; обучение с подкреплением (Reinforcement Learning), агент, среда, вознаграждение; краткий обзор других направлений.

8. Развертывание и использование модели: сериализация модели, концепция API для модели, создание простого веб-приложения с помощью Gradio и FastAPI.
    - Коротко о RESTful API → OpenAPI → FastAPI: https://github.com/ivtipm/ML/tree/main/examples/FastAPI
    - Создание простого пользовательского интерфейса (Gradio): https://github.com/ivtipm/ML/blob/main/examples/gradio.ipynb
9. Простейшее приложение в докер-контейнере.\
   Примеры:
    - https://github.com/ivtipm/ML/blob/main/examples/docker-ML-web
    - https://github.com/ivtipm/ML/blob/main/examples/docker-api 

# Задания

## Генетический алгоритм?

## Датасеты. Первичный анализ данных.
1. Загрузка и первичный анализ данных. Запросы к pandas.
1. Визуализации.

## Модели. Классификация и регрессия.
1. Подготовка данных. 
1. Обучение и оценка модели.
1. Пайплайны?

## Контейнер с моделью?
1. 

## Тест

# Экзамен
