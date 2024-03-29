# О курсе
Курс посвящён машинному обучению, направлению искусственного интеллекта, где задачи решаются на основе анализа данных. Нередко большого количества данных. В курсе будут рассмотрены основные понятия машинного обучения, способы анализа и визуализации данных, преобразования данных в вид, подходящий для моделей машинного обучения. Будут рассмотрены классические модели машинного обучения, начиная от регрессий, заканчивая градиентным бустингом; методы обучения и оптимизации качества этих моделей. В конце курса будут рассмотренные полносвязные нейросети (многослойные персепторн). 

Задания будут посвящены преимущественно обработке табличных и текстовых данных на примере синтетических и реальных наборов данных.

Рассматриваемые не нейросетевые методы МО применяются на практике, не смотря на большую популярность нейросетей. Курс можно считать как самостоятельным, так и длинным, но во многом обязательным, введением в курс нейросетевого анализа данных. Последний будет проходить в следующем семестре.

## Требования для успешного усвоения курса.

Для успешного освоения курса необходимы знания языка программирования Python, основ линейной алгебры, математического анализа и методов оптимизации.


## Материалы
0. Шпаргалка по Python https://miro.com/app/board/uXjVNQC1rq8=/?share_link_id=860218532001
0. Теория вероятностей и математическая статистика
    - [raw.githubusercontent.com/VetrovSV/AppMathST/master/variables_1.pdf](https://raw.githubusercontent.com/VetrovSV/AppMathST/master/variables_1.pdf)
   - [raw.githubusercontent.com/VetrovSV/AppMathST/master/variables_2.pdf](https://raw.githubusercontent.com/VetrovSV/AppMathST/master/variables_2.pdf)
   - [raw.githubusercontent.com/VetrovSV/AppMathST/master/statistics.pdf](https://raw.githubusercontent.com/VetrovSV/AppMathST/master/statistics.pdf)
   - Примеры распределений и их вид в зависимости от параметров: [seeing-theory.brown.edu/probability-distributions/index.html#section3](https://seeing-theory.brown.edu/probability-distributions/index.html#section3)
   - Среднее значение (average) и дисперсия (variance), интерактивный пример: [seeing-theory.brown.edu/basic-probability/index.html#section3](https://seeing-theory.brown.edu/basic-probability/index.html#section3)

# План. Зочное 2024. Методы машинного обучения
0. Математическая статистика, основы numpy, pandas, matplotlib
    1. [Математические модели и вычислительные методы обработки экспериментальных данных](https://raw.githubusercontent.com/ivtipm/ML/main/%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%20%D0%B8%20%D0%B2%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8%20%D1%8D%D0%BA%D1%81%D0%BF%D0%B5%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.pdf)
    1. 6 способов значительно ускорить pandas с помощью пары строк кода: https://habr.com/ru/articles/503726/, https://habr.com/ru/articles/504006/

1. Введение: [docs.google.com/presentation/d/1mK9CfhwjQtAdJZENV3vU4nCGSkzI8_Ugkv_AavBVEaM/edit?usp=sharing](https://docs.google.com/presentation/d/1mK9CfhwjQtAdJZENV3vU4nCGSkzI8_Ugkv_AavBVEaM/edit?usp=sharing)

2. [EDA, предобработка, кодирование colab.research.google.com/drive/1kLfmJ4q81BNZtMs-oVX9cKJGsT3mYWmR](https://colab.research.google.com/drive/1kLfmJ4q81BNZtMs-oVX9cKJGsT3mYWmR)

2. [Линейная регрессия. МНК. Метод макс.правдоподобия. sklearn.ipynb colab.research.google.com/drive/1YadlNYk9_WkCQY6L-HKP9SI7xZjuzIMx](https://colab.research.google.com/drive/1YadlNYk9_WkCQY6L-HKP9SI7xZjuzIMx?usp=sharing)

3. [Логистическая регрессия. LogLoss. colab.research.google.com/drive/1AdbtsRkX0jRVByuAKJxchYPcciTgFpqh](https://colab.research.google.com/drive/1AdbtsRkX0jRVByuAKJxchYPcciTgFpqh?usp=sharing)

1. Метод опорных векторов и метод k-ближайших соседей
   - [colab.research.google.com/drive/1oh7-ID00MN-AoJtAm4uL-bj0sqf5ieuk?usp=sharing](https://colab.research.google.com/drive/1oh7-ID00MN-AoJtAm4uL-bj0sqf5ieuk?usp=sharing)
1. Байесовская линейная регрессия и наивный байесовский классификатор
   - [colab.research.google.com/drive/1xJPrNR-iU6hmsMyzJHQIwTyYxjkhW3nm#scrollTo=P-1-EUt4mAHS](https://colab.research.google.com/drive/1xJPrNR-iU6hmsMyzJHQIwTyYxjkhW3nm#scrollTo=P-1-EUt4mAHS)
1. Деревья решений и ансамбли методов
   - [colab.research.google.com/drive/1Bin_h7BPSfnxs4Pea7eibceNMkOEcKmg?usp=sharing](https://colab.research.google.com/drive/1Bin_h7BPSfnxs4Pea7eibceNMkOEcKmg?usp=sharing)
1. Кластеризация
   - [учебное пособие](https://raw.githubusercontent.com/ivtipm/ML/main/%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%20%D0%B8%20%D0%B2%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8%20%D1%8D%D0%BA%D1%81%D0%BF%D0%B5%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.pdf#page=111)
   - пример: [colab.research.google.com/drive/1OjrSLj2hWx-0AqZtTc4ydOH5d22DFDxf](https://colab.research.google.com/drive/1OjrSLj2hWx-0AqZtTc4ydOH5d22DFDxf)
1. Уменьшение размерности и метод главных компонент
   - Интерактивные графики и веб-формы: [colab.research.google.com/drive/1SzAlYDLpjf65nnRbTVRtFxUWuyJnA8_s?usp=sharing](https://colab.research.google.com/drive/1SzAlYDLpjf65nnRbTVRtFxUWuyJnA8_s?usp=sharing)
1. Нейронные сети
   - Слайды: [docs.google.com/presentation/d/1YCJhQIj2BV42sDLKtxmytcYW5W39EJceYfqrYT7bKNo/edit?usp=sharing](https://docs.google.com/presentation/d/1YCJhQIj2BV42sDLKtxmytcYW5W39EJceYfqrYT7bKNo/edit?usp=sharing)
   - [colab.research.google.com/drive/1YtK4an7UAhnxTmhmQzZd6Eo3esfv6TL3 — Пример полносвязной ести на PyTorch](https://colab.research.google.com/drive/1YtK4an7UAhnxTmhmQzZd6Eo3esfv6TL3 — Пример полносвязной ести на PyTorch)
   - [colab.research.google.com/drive/1_5JVzwKej5hCe8I_bHfFYC0y8CrjfhJi — Основы PyTorch](https://colab.research.google.com/drive/1_5JVzwKej5hCe8I_bHfFYC0y8CrjfhJi — Основы PyTorch)

## Задания
Приводите в начале работы ссылку на задание, источник данных, Фамилию и инициалы.

#### Регрессия.
##### 1. Предварительный анализ данных и визуализация:
- данные:[www.kaggle.com/competitions/california-house-prices/overview](https://www.kaggle.com/competitions/california-house-prices/overview)
   - После согласования с преподавателем можно использовать свои данные
   - или используйте синтетические данные: число строк от 3000 до 7000, число независимых признаков от 3 до 5. Задавайте random_state по номеру варианта.
       - максимальная оценка на экзамене - 4
0. Зарегистрируйтесь на Kaggle (не обязательно)
1. Изучите пропуски, дубликаты, числовые характеристики (7 point summary)
2. Постройте графики:
      - пропусков,
      - распределений,
      - диаграммы размаха для отдельных величин, диаграммы размаха для одной величины в зависимости от значения категориальной величины,
      - попарные диаграммы рассеяния
2. Подготовьте данные:
   - Избавьтесь от пропусков, дубликатов, выбросов и некорректных значений (если они есть)
   - Закодируйте не числовые признаки
2. Напишите несколько простых и составных запросов для DataFrame, используйте группировки
6. Напишите выводы. Что вы поняли о данных? Напишите выводы о проделанной работе.
5. Сдайте работу в виде ссылки на тетрадку (Notebook) Google Colaboratory или Kaggle


Создавайте функции обработки.
Комментируйте код, дополняйте пояснениями, формулами и схемами.

Подсказка: в черновой версии программы можно удалить большую часть признаков (столбцов) с пропусками или с данными, которые не несут существенной информации. Так будет проще на практике изучить всю последовательность действий предварительного анализа и обработки данных. После, можно подумать какие из удалённых признаков стоит оставить и как заполнить пропуски, выбросы и ошибочные значения.
##### 2. Регрессия
1. Решите задачу регрессии для набора данных.
Используйте модели:
- линейная регрессия
- SVM
- Деревья решений
- Градиентный бустинг
- другие модели по желанию
Комментируйте код, дополняйте пояснениями, формулами и схемами. Поясняйте сильные и слабые стороны моделей.
1. Используйте поиск по сетке гиперпараметров (2 или более) для как минимум одной модели
2. Напишите выводы.
    1. Представьте результаты тестирования моделей в отдельной таблице. Рекомендуется использовать сервис wandb
    2. Объяснить различия в качестве предсказания у разных моделей.
    1. Опишите процесс улучшения качества из п.2.
    1. Предложите пути улучшения качества предсказаний.
    1. Опишите свой опыт.

#### Классификация текстов.
Решите [задачу классификации текстовых документов](https://github.com/ivtipm/ML/blob/main/ML/text_classification.md)

# Экзамен
Допуск на экзамен - собеседование по работам.
