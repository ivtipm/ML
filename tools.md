# Инструменты для МО

[Jupyter Lab](https://jupyter.org/) - IDE для анализа данных и МО, основной вид виде интерактивного блокнота (notebook, ipynb файл).
- Имеет веб-интерфейс, поэтому сервер может быть запущен не только локально но и на любой машине, к которой есть доступ.
- Основной типа файлов IDE - Блокнот (notebook, тетрадка). Может содержать код на Питоне (и не только); показывать статичные и интерактивные диаграммы, создаваемые на языке программирования; показывать текст в разметке markdown (включая структурирование с помощью заголовков), формулы в LaTeX.
Позволяет просматривать файлы с табличными данными.
- Jyputer Lab включает в себя возможности среды Jyputer Notebook. 
- Подобная Jyputer Notebook IDE (в качестве основы) используется в [Google Colaboratory](https://colab.research.google.com/), среде Kaggle, специальных сервисах для МО в Яндекс Облаке и др. местах
- Поддерживает плагины

**VS Code** тоже поддерживает работу с Jyputer Notebook, позволяет открывать и запускать Jyputer сервер. 


### Некоторые горячие клавиши
- <kbd>Esc</kbd> - перейти из режима редактирования ячейки в режим выделения ячеек.
- <kbd>Enter</kbd> - перейти в режим редактирования ячейки.
- <kbd>Tab</kbd> - автодополнение (может работать не мгновенно)
- <kbd>Shift</kbd> + <kbd>Tab</kbd> - показать документацию для идентификатора под курсором
- <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>C</kbd> - открыть окно команд.

Горячие клавиши для режима выделения ячеек:
- <kbd>Shift</kbd>+<kbd>Enter</kbd> - выполнить выделенные ячейки и перейти в ячейку ниже
 - <kbd>СCtrl</kbd>+<kbd>Enter</kbd> - выполнить выделенные ячейки
- <kbd>a</kbd> -  добавить ячейку выше (**a**bove) 
- <kbd>b</kbd> -  добавить ячейку выше (**b**elow)
- <kbd>d</kbd> <kbd>d</kbd> -   удалить выбранную ячейку или ячейки(**d**elete)
- <kbd>y</kbd> - перевести ячейку в формат Code
- <kbd>m</kbd> - перевести ячейку в формат Markdown
- <kbd>l</kbd> - скрыть\показать номера строк

### Плагины
Настройки плагинов недоступны из панели плагинов, но в общих настройках Jupyter Lab есть разделы соответствующие плагинам.

- https://jupyterlab-contrib.github.io/jupyterlab-cell-flash.html
- https://github.com/jupyter-server/jupyter-resource-usage
- [jupyterlab-execute-time](https://github.com/deshaw/jupyterlab-execute-time): Execute Time Plugin for Jupyter Lab
- https://github.com/jtpio/jupyterlab-theme-toggle