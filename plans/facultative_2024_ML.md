# ДПО. Модуль: машинное обучение

# Занятие 1. Введение в МО.
3 февраля
1. Понятие МО. Задачи МО: классификация и регрессия.
2. Представление данных. Виды признаков по природе значений (числовой, номинальный, категориальный). \
Виды признаков по задаче (независимые, зависимые (целевые))
3. Пример проекта в среде Jupyter Notebook в сервисе Google Colaboratory: обучение модели линейной регрессии с помощью библиотеки SKLearn [[подробнее про линейную регрессию](https://colab.research.google.com/drive/1YadlNYk9_WkCQY6L-HKP9SI7xZjuzIMx?usp=sharing#scrollTo=pxeShTXsN2xZ)]

- Слайды: https://docs.google.com/presentation/d/1mK9CfhwjQtAdJZENV3vU4nCGSkzI8_Ugkv_AavBVEaM/edit?usp=sharing
- Пример: https://colab.research.google.com/drive/18YGaumubomt-Rtg_9_VT_nf1GwbMlEx8?usp=sharing

См. запись занятия в чате группы


### Домашнее задание 0. Основы Google colab (будет дополнено на следующем занятии)
1. Освойтесь в google colaboratory
    - Как создавать ячейки? Какие виды ячеек бывают?
    - Какие способы запуска ячеек есть? Как ячейки с кодом влияют друг на друга?
    - Что такое markdown? Как создавать заголовки (и просматривать их в Google Colaboratory), делать текст жирным, курсивом, приводить фрагменты кода с подсветкой синтаксиса, приводить формулы в записи LaTeX?
    - Как делиться проектом (тетрадкой - notebook)?
1. Изучите пример. Попробуйте обучить модель (линейную регрессию) для другого числа объектов и признаков. Проверьте полученное уравнение.
2. Разделите исходные данные на выборку для обучения (train) и отложенную выборку (test) для проверки результатов обучения. Оцените качество модели на этих выборках. Почему результаты могут отличаться?
    - Вычисляйте ошибку MSE, MAE. Используйте встроенные в sklearn функции. 
    - Вычислите стандартное отклонение ошибки.
    - Реализуйте эти вычисления самостоятельно, используя массив NumPy, но не используйте никакие методы кроме суммы.
    - Вычислите 7-point summary для всех независимых признаков. Используйте numpy, только методы sum, min, max, quantile.
3. Напишите пояснения и комментарии к коду. Поясняйте общий алгоритм, смысл действий, понятия (std, mean, ) параметры вызываемых функций, записанные в коде формулы (приведите их в LaTeX). Комментарии к коду можно оставлять в ячейках с кодом, остальные пояснения можно давать в ячейках с текстом.



# Занятие 2. Введение в МО
1. Повторение. Опрос.
    - Что такое МО? Чем оно отличается от решения задач традиционным программированием?
    - Какие задачи может решать МО? На какие подвиды делиться задача прогнозирования (предсказания)? Чем они отличаются?
    - Как представляют данные в МО? Какие виды признаков бывают?
    - Какая модель МО была рассмотрена на прошлом занятии? Как её можно описать? Как её обучить?
    - Что такое Jupyter Notebook? Что такое Google Colaboratory? Как в тетрадке (notebook) сделать заголовки? Как поделиться? Как форматировать текст?
1. Показатели качества моделей [[Слайды](https://docs.google.com/presentation/d/1mK9CfhwjQtAdJZENV3vU4nCGSkzI8_Ugkv_AavBVEaM/edit?usp=sharing)] регрессии. 

1. Основы математической статистики:
   - [raw.githubusercontent.com/VetrovSV/AppMathST/master/variables_1.pdf](https://raw.githubusercontent.com/VetrovSV/AppMathST/master/variables_1.pdf)
   - [raw.githubusercontent.com/VetrovSV/AppMathST/master/variables_2.pdf](https://raw.githubusercontent.com/VetrovSV/AppMathST/master/variables_2.pdf)
   - [raw.githubusercontent.com/VetrovSV/AppMathST/master/statistics.pdf](https://raw.githubusercontent.com/VetrovSV/AppMathST/master/statistics.pdf)
   - Примеры распределений и их вид в зависимости от параметров: [seeing-theory.brown.edu/probability-distributions/index.html#section3](https://seeing-theory.brown.edu/probability-distributions/index.html#section3)
   - Среднее значение (average) и дисперсия (variance), интерактивный пример: [seeing-theory.brown.edu/basic-probability/index.html#section3](https://seeing-theory.brown.edu/basic-probability/index.html#section3)

1. NumPy. Pandas.
    - [Математические модели и вычислительные методы обработки экспериментальных данных](https://github.com/ivtipm/ML/blob/2c81049c9f1056d3be594642fde8c70d2d268d25/%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8%20%D0%B8%20%D0%B2%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8%20%D1%8D%D0%BA%D1%81%D0%BF%D0%B5%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D1%85%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.pdf)


- Пример: https://colab.research.google.com/drive/18YGaumubomt-Rtg_9_VT_nf1GwbMlEx8?usp=sharing