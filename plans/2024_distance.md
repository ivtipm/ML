# План. Зочное 2024. Методы машинного обучения

## Материалы
0. Теория вероятностей и математическая статистика
    - [raw.githubusercontent.com/VetrovSV/AppMathST/master/variables_1.pdf](https://raw.githubusercontent.com/VetrovSV/AppMathST/master/variables_1.pdf)
   - [raw.githubusercontent.com/VetrovSV/AppMathST/master/variables_2.pdf](https://raw.githubusercontent.com/VetrovSV/AppMathST/master/variables_2.pdf)
   - [raw.githubusercontent.com/VetrovSV/AppMathST/master/statistics.pdf](https://raw.githubusercontent.com/VetrovSV/AppMathST/master/statistics.pdf)
   - Примеры распределений и их вид в зависимости от параметров: [seeing-theory.brown.edu/probability-distributions/index.html#section3](https://seeing-theory.brown.edu/probability-distributions/index.html#section3)
   - Среднее значение (average) и дисперсия (variance), интерактивный пример: [seeing-theory.brown.edu/basic-probability/index.html#section3](https://seeing-theory.brown.edu/basic-probability/index.html#section3)

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
#### Регрессия.


#### Классификация текстов.
