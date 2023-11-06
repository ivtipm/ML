# Методы МО
# Содержание
## Математические аспекты анализа данных и машинного обучения
### Лекции
#### 1. Введение в машинное обучение
   - Слайды: [docs.google.com/presentation/d/1mK9CfhwjQtAdJZENV3vU4nCGSkzI8_Ugkv_AavBVEaM/edit?usp=sharing](https://docs.google.com/presentation/d/1mK9CfhwjQtAdJZENV3vU4nCGSkzI8_Ugkv_AavBVEaM/edit?usp=sharing)

#### 2. Теория вероятностей и математическая статистика
   - [raw.githubusercontent.com/VetrovSV/AppMathST/master/variables_1.pdf](https://raw.githubusercontent.com/VetrovSV/AppMathST/master/variables_1.pdf)
   - [raw.githubusercontent.com/VetrovSV/AppMathST/master/variables_2.pdf](https://raw.githubusercontent.com/VetrovSV/AppMathST/master/variables_2.pdf)
   - [raw.githubusercontent.com/VetrovSV/AppMathST/master/statistics.pdf](https://raw.githubusercontent.com/VetrovSV/AppMathST/master/statistics.pdf)
   - Примеры распределений и их вид в зависимости от параметров: [seeing-theory.brown.edu/probability-distributions/index.html#section3](https://seeing-theory.brown.edu/probability-distributions/index.html#section3)
   - Среднее значение (average) и дисперсия (variance), интерактивный пример: [seeing-theory.brown.edu/basic-probability/index.html#section3](https://seeing-theory.brown.edu/basic-probability/index.html#section3)

#### 3. Линейная регрессия. Метод наименьших квадратов. Статистический вывод
   - Повторение: случайная величина, числовые характеристики, распределение.
   - [raw.githubusercontent.com/VetrovSV/AppMathST/master/statistics.pdf](https://raw.githubusercontent.com/VetrovSV/AppMathST/master/statistics.pdf)
   - [Математические модели и вычислительные методы обработки экспериментальных данных](https://raw.githubusercontent.com/ivtipm/ML/main/%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%20%D0%B8%20%D0%B2%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8%20%D1%8D%D0%BA%D1%81%D0%BF%D0%B5%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.pdf) раздел 2.4
   - Корреляция, коэффициент линейной корреляции (Пирсона), оценка качества уравнения регресии, коэффициент детерминации.
   - Линейная регрессия в sklearn
   - Теория + пример: [colab.research.google.com/drive/1YadlNYk9_WkCQY6L-HKP9SI7xZjuzIMx?usp=sharing](https://colab.research.google.com/drive/1YadlNYk9_WkCQY6L-HKP9SI7xZjuzIMx?usp=sharing)

#### 4. Градиентный спуск и стохастический градиентный спуск
   - Теория: [raw.githubusercontent.com/ivtipm/ML/main/Gradient%20Descent.pdf](https://raw.githubusercontent.com/ivtipm/ML/main/Gradient%20Descent.pdf)
   - [colab.research.google.com/drive/1YadlNYk9_WkCQY6L-HKP9SI7xZjuzIMx#scrollTo=Bz-MhoMQ8XPR](https://colab.research.google.com/drive/1YadlNYk9_WkCQY6L-HKP9SI7xZjuzIMx#scrollTo=Bz-MhoMQ8XPR)

#### 5. Логистическая регрессия.
   - Линейная разделимость классов. Сигмоида. Вероятностная модель; LogLoss.
   - [colab.research.google.com/drive/1AdbtsRkX0jRVByuAKJxchYPcciTgFpqh?usp=sharing](https://colab.research.google.com/drive/1AdbtsRkX0jRVByuAKJxchYPcciTgFpqh?usp=sharing)

#### 6. Регуляризация линейной регрессии и логистической регрессии.
#### 7. Повторные выборки. Кросс-валидация. Выбор модели.
#### 8. Выбор признаков (отбор признаков на основе статистической значимости, создание новых признаков, ... )

### Практики
#### 1. Обзор основных средств анализа данных. Установка и настройка рабочей среды.
   - Python. pip. virtual enviroment? conda?
   - GNU Tools. cd, ls, pwd, ..., wc, cat, head, tail, less, diff?
   - Jupyter Notebook. Google Colaboratory. Kaggle.

#### Домашнее задание 1. EDA и предварительная обработка
   - Изучите возможности google collaboratore, ноутбуков kaggle.com, установите DataSpell
   - Посмотрите основные возможности библиотек NumPy и Pandas.  [ [Математические модели и вычислительные методы обработки экспериментальных данных](https://raw.githubusercontent.com/ivtipm/ML/main/%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%20%D0%B8%20%D0%B2%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8%20%D1%8D%D0%BA%D1%81%D0%BF%D0%B5%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.pdf)  ]

#### 3. Библиотеки анализа данных и машинного обучения.
   -  Numpy. Pandas. SciPy. Matplotlib. Seaborn. plotly. Sklearn.

#### Домашнее задание 2. EDA, визуализация, предварительная обработка данных для регресии
Предварительный анализ данных и визуализация:
- данные:[www.kaggle.com/competitions/california-house-prices/overview](https://www.kaggle.com/competitions/california-house-prices/overview)
   - После согласования с преподавателем можно использовать свои данные
0. Зарегистрируйтесь на Kaggle
1. Изучите пропуски, дубликаты, числовые характеристики
2. Постройте графики:
      - пропусков
      - распределений,
      - диаграммы размаха для отдельных величин, диаграммы размаха для одной величины в зависимости от значения категориальной величины,
      - попарные диаграммы рассеяния
2. Подготовьте данные:
   - Избавьтесь от пропусков, дубликатов, выбросов и некорректных значений (если они есть)
   - Закодируйте не числовые признаки
2. Напишите несколько простых и составных запросов для DataFrame, используйте группировки
3. Проверьте гипотезу о нормальности распределения
4. Комментируйте код. создавайте функции обработки
6. Напишите выводы. Что вы поняли о данных? Напишите выводы о проделанной работе.
5. Сдайте работу в виде ссылки на тетрадку (Notebook) Google Colaboratory или Kaggle

Подсказка: в черновой версии программы можно удалить большую часть признаков (столбцов) с пропусками или с данными, которые не несут существенной информации. Так будет проще на практике изучить всю последовательность действий предварительного анализа и обработки данных. После, можно подумать какие из удалённых признаков стоит оставить и как заполнить пропуски, выбросы и ошибочные значения.



Задавайте вопросы, возникающие во время выполнения задания, в дискорде.

Источники:
1. [ [Математические модели и вычислительные методы обработки экспериментальных данных](https://raw.githubusercontent.com/ivtipm/ML/main/%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%20%D0%B8%20%D0%B2%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8%20%D1%8D%D0%BA%D1%81%D0%BF%D0%B5%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.pdf)  ]
2. [colab.research.google.com/drive/1kLfmJ4q81BNZtMs-oVX9cKJGsT3mYWmR](https://colab.research.google.com/drive/1kLfmJ4q81BNZtMs-oVX9cKJGsT3mYWmR)
3. Документация Pandas, Numpy, matplotlib, seaborn, scipy




#### 5. Теория вероятностей и математическая статистика. Основные понятия. Корреляция. Законы распределения
#### 6. Оптимизация. Метод наименьших квадратов, градиентный спуск, стохастический градиентный спуск.
#### 7. Теория вероятностей и математическая статистика. Доверительный интервал. Проверка гипотез.
#### 8. Линейная регрессия
#### Домашнее задание 3. Регрессия
Решите задачу регрессии для набора данных из [предыдущей работы](#домашнее-задание-2-eda-визуализация-предварительная-обработка)

#### 9. Логистическая регрессия, многоклассовая классификация

#### Домашнее задание 4. Классификация
- Минимальный вариант.
   Решите задачу многоклассовой классификации на основе логистической регрессии для синтетических данных (см. функцию make_classification). Создайте данные где минимум 6 признаков, часть из них не должны влиять на целевую переменную.
- [Полноценный вариант с предварительным анализом и предварительной обработкой](task_classification.md)

#### 10. Регуляризация и выбор модели. Отбор признаков.
   - [colab.research.google.com/drive/1oF1OSgi_v_TgXsIJOvupmo020rKyPPP0#scrollTo=bQ8AgaO1Mbn2](https://colab.research.google.com/drive/1oF1OSgi_v_TgXsIJOvupmo020rKyPPP0#scrollTo=bQ8AgaO1Mbn2)
   - Балансирование выборок:
   ```pyhton
   from imblearn.under_sampling import TomekLinks
   from imblearn.over_sampling import ADASYN
   ```
      - [imbalanced-learn.org/stable/over_sampling.html#from-random-over-sampling-to-smote-and-adasyn](https://imbalanced-learn.org/stable/over_sampling.html#from-random-over-sampling-to-smote-and-adasyn)
      - [imbalanced-learn.org/stable/under_sampling.html?highlight=tomeklinks#tomek-s-links](https://imbalanced-learn.org/stable/under_sampling.html?highlight=tomeklinks#tomek-s-links)


#### Домашнее задание 5. Регрессия (продолжение)
Дополните решение задачи регрессии:
1. Постройте модели с регуляризациями  L1, L2 отдельно и вместе
1. В пояснениях напишите формулы
1. Оцените их качество по сравнению с классическим уравнением регрессии
1. Поэкспериментируйте с отбором признаков на основе этих регрессий.
1. Поэкспериментируйте с полиномиальными признаками.
1. Дополните выводы

#### Домашнее задание 6. SVM, kNN и поиск по сетке гиперпараметров
1. Дополните работы по регрессии и классификации моделями на основе kNN и SVM
2. Подберите гиперпараметры для всех моделей
3. Сравните качество моделей. Сделайте выводы на основе сравнения.



## Методы машинного обучения
### Лекции
#### 1. Метод опорных векторов и метод k-ближайших соседей
   - [colab.research.google.com/drive/1oh7-ID00MN-AoJtAm4uL-bj0sqf5ieuk?usp=sharing](https://colab.research.google.com/drive/1oh7-ID00MN-AoJtAm4uL-bj0sqf5ieuk?usp=sharing)
#### 2. Байесовская линейная регрессия и наивный байесовский классификатор
   - [colab.research.google.com/drive/1xJPrNR-iU6hmsMyzJHQIwTyYxjkhW3nm#scrollTo=P-1-EUt4mAHS](https://colab.research.google.com/drive/1xJPrNR-iU6hmsMyzJHQIwTyYxjkhW3nm#scrollTo=P-1-EUt4mAHS)
#### 3. Деревья решений и ансамбли методов
   - [colab.research.google.com/drive/1Bin_h7BPSfnxs4Pea7eibceNMkOEcKmg?usp=sharing](https://colab.research.google.com/drive/1Bin_h7BPSfnxs4Pea7eibceNMkOEcKmg?usp=sharing)
#### 4. Кластеризация
   - [учебное пособие](https://raw.githubusercontent.com/ivtipm/ML/main/%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%20%D0%B8%20%D0%B2%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8%20%D1%8D%D0%BA%D1%81%D0%BF%D0%B5%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.pdf#page=111)
   - пример: [colab.research.google.com/drive/1OjrSLj2hWx-0AqZtTc4ydOH5d22DFDxf](https://colab.research.google.com/drive/1OjrSLj2hWx-0AqZtTc4ydOH5d22DFDxf)


#### 5. Уменьшение размерности и метод главных компонент
   - Интерактивные графики и веб-формы: [colab.research.google.com/drive/1SzAlYDLpjf65nnRbTVRtFxUWuyJnA8_s?usp=sharing](https://colab.research.google.com/drive/1SzAlYDLpjf65nnRbTVRtFxUWuyJnA8_s?usp=sharing)
#### 6. Рекомендательные системы
#### 7. Распределенные алгоритмы
- ...
- 6 способов значительно ускорить pandas с помощью пары строк кода: https://habr.com/ru/articles/503726/, https://habr.com/ru/articles/504006/
#### 8. Нейронные сети
   - Слайды: [docs.google.com/presentation/d/1YCJhQIj2BV42sDLKtxmytcYW5W39EJceYfqrYT7bKNo/edit?usp=sharing](https://docs.google.com/presentation/d/1YCJhQIj2BV42sDLKtxmytcYW5W39EJceYfqrYT7bKNo/edit?usp=sharing)
   - [colab.research.google.com/drive/1YtK4an7UAhnxTmhmQzZd6Eo3esfv6TL3 — Пример полносвязной ести на PyTorch](https://colab.research.google.com/drive/1YtK4an7UAhnxTmhmQzZd6Eo3esfv6TL3 — Пример полносвязной ести на PyTorch)
   - [colab.research.google.com/drive/1_5JVzwKej5hCe8I_bHfFYC0y8CrjfhJi — Основы PyTorch](https://colab.research.google.com/drive/1_5JVzwKej5hCe8I_bHfFYC0y8CrjfhJi — Основы PyTorch)
#### Домашнее задание. Keras. Pytorch.
Примените нейросети для решения задачи классификации и регрессии.
Используйте фреимворки Keras и PyTorch (2 способа: на основе Sequential и Module)
#### 9. Представление данных

### Практики
#### 1. Метрики качества классификатора. Классификация с несбалансированной выборкой.
#### 3. Метод опорных векторов и k-ближайших соседей
#### 4. Деревья решений
#### 5. Комбинации моделей
#### Домашнее задание 8. Деревья. Ансамбли.
Примените методы в работах по классификации и регрессии, используйте поиск по сетке гиперпараметров:
- Решающее дерево
- Случайный лес
- Беггинг на основе решающих деревьев
- Комитет (простое или взвешенное голосование)
- Комментируйте код, дополняйте формулами и схемами
- Дополните таблицу с результатами качества моделей
- Дополните выводы

#### 6. Кластеризация. Метрики качества. Определение количества кластеров
#### Домашнее задание 7. Кластеризация
   Решите задачу кластеризации.
   - Используйте метод KMeans, подберите количество кластеров методом локтя и по коэффициенту силуэта.
   - Визуализируйте кластеры. Используйте PCA.
   - Приведите короткую справку про метод KMeans.
   - Примените 2-3 других метода из библиотеки sklearn. Чем они отличаются?
   - Напишите комментарии, документацию к коду и выводы.
   - <a href="https://raw.githubusercontent.com/SteffiPeTaffy/machineLearningAZ/master/Machine Learning A-Z Template Folder/Part 4 - Clustering/Section 25 - Hierarchical Clustering/Mall_Customers.csv">Датасет</a>

#### 7. Метод главных компонент PCA
#### 8. Работа с категориальными признаками. Классификация текстовых документов
#### Домашнее задание 8. Классификация текстов
Решите [задачу классификации текстовых документов](https://github.com/ivtipm/ML/blob/main/ML/text_classification.md)
#### 9. Рекомендательные системы
#### 10. Модели представления данных


# Экзамен
Консультация. 1 июня, 19:00 онлайн\
Экзамен. 3 июня 13:00 оффлайн\

Билет:
1. Теория.
2. Собеседование по одной из выполненных работ
3. Собеседование по одной из выполненных работ

Будьте готовы модифицировать и дополнить код.

## Примерный список темы и понятий
1. Понятие машинного обучения. Задачи. Типы алгоритмов. Регрессия vs классификация vs кластеризация. Разложение ошибки модели.
2. Метрики качества задач регрессии и классификации. Общая точность, точность, полнота, F beta, ROC AUC, R2, MSE, MAE, ...
3. Теория вероятностей и мат. статистика.
  - Вероятность. Закон больших чисел. Условная вероятность. Сложение и умножение событий. Теорема Байеса.
- Распределение. Числовые характеристики. Распределения: нормальное, биномиальное
- Выборка и генеральная совокупность. Бутстрэп.
  - Диаграмма размаха. Статистическая гипотеза. Гипотеза о равенстве (сравнении) средних. Гипотеза о соответствии распределению.  
  - Корреляция. КК Пирсона. Регрессия. Гипотеза о значимости КК Пирсона.
4. Анализ и подготовка данных. CRISP-DM.
  - Общий алгоритм анализа данных. Признаки, их виды. Пропуски. Выбросы. Ошибки.
  - Визуализация. Гистограмма. Диаграмма рассеяния. Тепловая карта. Диаграмма размаха.
  - Способы определения выбросов. Способы борьбы с пропусками, ошибками и выбросами.
  - Виды признаков. Способы кодирования с учётом и без учёта отношения порядка.
  - Модификация признаков. Приведение к нормальному распределению. Создание новых признаков. Отбор признаков.
  - Балансировка классов.  Андерсемплинг. Оверсемплинг. ADASYN. Tomek Links.
  - Нормализация и стандартизация.
  - Оценка качества модели. Переобучение и недообучение. Перекрёстная проверка.
  - Поиск по сетке гиперпараметров.
  - Примеры кода.
4. Метод наименьших квадратов.
5. Понятие методы оптимизации. Классификация. Метод стохастического градиентного спуска. Градиент. Производная сложной функции.\
Методы машинного обучения: параметры и гиперпараметры. Функции потерь. Преимущества и недостатки. Применение в задачах классификации и регрессии. Применение, примеры кода.
6. Линейная регрессия. Аналитическое решение. Регуляризации.
7. Метод опорных векторов. Модификации.
8. K ближайших соседей. Модификации.
9. Наивный байесовский классификатор.
10. Метод максимального правдоподобия. Вероятностная модель.
11. Логистическая регрессия.
12. Дерево решений.
13. Ансамбли. Голосование. Беггинг. Стэкинг. Блендинг. Адаптивный и градиентный бустинг.
14. Случайный лес.
16. Нейросеть (многослойный персептрон). Бинарная и многоклассовая классификация. Регрессия. Функции активации. Функции потерь. Обучение. Метод обратного распространения ошибки. Контроль переобучения. Раняя остановка.
17. Обучение без учителя. Кластеризация. Классификация алгоритмов. Показатели качества кластеризации. Метод kMeans. *Mean Shift. DBSCAN.*
18. Снижение размерности. PCA. UMAP. *SVD*
19. Обработка текста. Способы представления. Мешок слов. TF-IDF. Классификация.
20. Python. DataFrame. Nampy Array. Torch Tensor. Matplotlib. Plotly. Gradio. Конвейеры sklearn. Утилиты Linux для работы для получения сведений о аппаратном обеспечении, работы с файлами, простейшей обработки и анализа файлов. Google Colaboratory. Kaggle Notebook. Нейросети в Keras. Нейросети в pytorch.\ *wandb: Отслеживание показателей во время обучения, финальные измерения, диаграммы*\
Темы для дальнейшего самостоятельного изучения.
20. *Распределённые алгоритмы.* 
    Некоторые фреимворки для распределённых вычислений: PySpark (со свой ML бибилиотекой, dask)
21. *Рекомендательные системы*\
Бонус:
22. Портфолио участника соревнований по машинному обучению и примеры решения задач машинного обучения.


Подготовка конспекта-шпаргалки, интеллект-карты приветствуется.

Курсивом отмечены темы рекомендованые для дальнейшего изучения.
