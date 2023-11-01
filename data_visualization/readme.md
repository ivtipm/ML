# Визуализация данных
## Темы и понятия
1. Визуальные переменные
  - каналы
  - виды переменных
  - простота восприятия, закон Стивенса
2. Типы диаграмм
1. Таблицы
1. Уменьшение размерности
  - PCA, t-SNE
3. Эстетика и минимализм (Эдвард Тафти и Наджел Холмс)
  - коэффициент информативности (data-ink ratio)
  - DataArt


## Инструменты
- Excel
- Python и библиотеки
- Power BI
- Tableau
- D3.js
- Yandex DataLens


## Библиотеки Python
- matplotlib
- seaborn
- plotly
- Folium
- bokeh

### Seaborn
#### Настройка внешнего вида
https://seaborn.pydata.org/tutorial/aesthetics.html

```python
seaborn.set_theme()       # сбросить все настройки отображения

seaborn.despine()         # удалить рамку
```

Тема, в отличии от стиля, определяет в основном размеры элементов. Полезно если нужно создать графики для презентации (большие подписи) и для статьи (маленькие).

| `set_style` || `set_theme` |
| :------------- || :------------- |
| darkgrid (default) || - paper|
| whitegrid || - notebook |
| dark || - talk |
| white || - poster |
| ticks ||  |


# Литература
- Stephen Few
  - Show Me the Numbers: Designing Tables and Graphs to Enlighten, Second Edition, June 2012 и др. книги
  - http://perceptualedge.com
- Эдвард Тафти (Edward R. Tufte)
  - The Visual Display of Quantitative Information, Graphics Press, 2001. 200 p. и другие книги
- https://datavizcatalogue.com/RU/ -- Каталог Визуализации Данных
