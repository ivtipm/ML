# Вычисления для GPU
## ROCm
ROCm (изначально Radeon Open Compute) - это открытая платформа (драйвер + средства разработки) для вычислений на GPU производства AMD.
CUDA - аналогичная, но проприетарная, платформа для вычислений на GPU производства Nvidia. В настоящий момент ROCm как более молодая технология поддерживает меньшее количество видеокарт, версий ОС и другого программного обеспечения, имеет меньше возможностей.

Существует специальная версия PyTorch для ROCm.

### Установка в Ubuntu
Основная инструкция: https://rocm.docs.amd.com/_/downloads/install-on-linux/en/latest/pdf/

0. Проверить поддержку ROCm видеокартой.\
Некоторые видеокарты, например AMD 6600, фактически поддерживают технологию, но официально об этом не сообщается.
0. Выполнить предварительную настройку
Добавить текущего пользователя в группы render и video
```bash
sudo usermod -a -G render $LOGNAME
sudo usermod -a -G video $LOGNAME
```
1. Установить драйвер для AMD GPU. 
Скачать и установить программу установки драйвера видеокарты `amdgpu-install`.
```
wget https://repo.radeon.com/amdgpu-install/6.1.1/ubuntu/jammy/amdgpu-install_6.1.60101-1_all.deb
sudo apt install ./amdgpu-install_6.1.60101-1_all.deb
```
Версия файла актуальна на момент мая 2024 г. Новая версия указана в инструкции, причём она может быть новее, чем предоставленная на сайте AMD.
```bash
sudo apt update
sudo apt install amdgpu-dkms
sudo apt install rocm
```
Перезапустить ОС.
2. Установить необходимые библиотеки, например (pytorch)[https://pytorch.org/].
Рекомендуется устанавливать в созданное виртуальное окружение или в Докер-контейнер (`docker pull rocm/pytorch:latest`) (раздел инструкции)[https://rocm.docs.amd.com/_/downloads/install-on-linux/en/latest/pdf/#section.10.1].
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.0
```

3. Дополнительно:
> Make sure before running any program in either TensorFlow or PyTorch, run the following command:
`HSA_OVERRIDE_GFX_VERSION=10.3.0`

[https://github.com/alfinauzikri/ROCm-RX6600XT]

При проблемах совместимости с аппаратным обеспечением (GPU не имеет полной поддерки ROCm) выполнение кода на GPU может быть возможным только после подмены переменной `HSA_OVERRIDE_GFX_VERSION=10.3.0` - версии графического ядра.
Например: `HSA_OVERRIDE_GFX_VERSION=10.3.0 jupyter lab` или `HSA_OVERRIDE_GFX_VERSION=10.3.0 python3 main.py`

Корректная работы всех функций не гарантируется.

**Отображение информации о ROMc устройствах и их состоянии GPU**
```bash
# информация про все устройства (включая поддерживаемые CPU)
rocminfo

# состояние устройств
rocm-smi
```

Пример вывода информации о состоянии
```text
======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp   AvgPwr  SCLK    MCLK   Fan  Perf  PwrCap  VRAM%  GPU%  
0    36.0c  4.0W    800Mhz  96Mhz  0%   auto  100.0W   61%   0%    
================================================================================
============================= End of ROCm SMI Log ==============================
```

Для постоянного мониторинга удобнее всего циклически запускать программу rocm-smi используя утилиту watch. Например, запускать каждые полсекунды:
```bash
watch -n 0.5 rocm-smi
```

Мониторинг загрузки видеопамити и GPU доступен также в программе btop++, еслли установлен пакет rocm-smi
<img src="assets\btop_gpu.png" width=600 > 

**Пример для быстрой проверки работоспособности ROCm**

```python
import torch

Device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print("Device: ", Device)

# общая информация
print(torch.__version__)
print(torch.version.cuda)
print(torch.backends.cudnn.version())
print(torch.cuda.get_device_name(0))
print(torch.cuda.get_device_properties(0))

# коротка проверка
print( torch.ones(2).to(torch.device(0)) )

# проверка перемножением матриц
N = 20_000
a = torch.rand( (N, N) ).to(Device)
b = torch.rand( (N, N) ).to(Device)

d = a @ b
```


**Вывод полной технической информации:** https://gist.github.com/damico/484f7b0a148a0c5f707054cf9c0a0533

# Инструменты МО


## IDE - Jupyter \ Jupyter in VS Code
[Jupyter Lab](https://jupyter.org/) - IDE для анализа данных и МО, основной вид виде интерактивного блокнота (notebook, ipynb файл).
- Имеет веб-интерфейс, поэтому сервер может быть запущен не только локально но и на любой машине, к которой есть доступ.
- Основной типа файлов IDE - Блокнот (notebook, тетрадка). Может содержать код на Питоне (и не только); показывать статичные и интерактивные диаграммы, создаваемые на языке программирования; показывать текст в разметке markdown (включая структурирование с помощью заголовков), формулы в LaTeX.
Позволяет просматривать файлы с табличными данными.
- Jupyter Lab включает в себя возможности среды Jupyter Notebook. 
- Подобная Jupyter Notebook IDE (в качестве основы) используется в [Google Colaboratory](https://colab.research.google.com/), среде Kaggle, специальных сервисах для МО в Яндекс Облаке и др. местах
- Поддерживает плагины

**VS Code** тоже поддерживает работу с Jupyter Notebook, позволяет открывать и запускать Jupyter сервер прямо из окна редактора.
Есть возможность выполнять открытый локально ipynb файл на удалённом сервере: <kbd>F1</kbd> > `Notebook: Select notebook kernel` (или нажать на кнопку kernel справа вверху, в открытом блокноте) > Select another > Вставить URL сервера с Jupyter.
Работа, при этом будет по своему принципу похожа на работу в google colaboratory. Все файлы, к которым обращается код должны быть на удалённом сервере. Но файл ipynb может быть локальным.

**Запуск Jupyter сервера**
Короткий вариант, без создания файла конфигурации:
```bash
jupyter notebook --no-browser --port=8888 --ip=0.0.0.0

# для докального запуска без контроля доступа к серверу
jupyter lab --no-browser --ip=127.0.0.1 --NotebookApp.token=''

```
Если не указать `--ip=0.0.0.0` то, по умолчанию сервер будет запущен на 127.0.0.1 и будет недоступен из сети.

URL, по которому будет доступе сервер, можно видеть в выводе после запуска.





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


### Расширения VS Code
- Jupyter, Jupyter Notebbok Renderer
- Data Wrangler - для удобного просмотра таблиц DataFrame
- RainbovCSV - для подсветки колонок в CVS файлах

# [Локальный запуск LLM](tools/llm_servers/llm.md)

# Детекторы текстов, написанных большими языковыми моделями

- https://developers.sber.ru/portal/products/gigacheck

- https://www.zerogpt.com/
