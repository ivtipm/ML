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

При проблемах совместимости версий выполнение кода на GPU может быть возможным только после ручного задания переменной `HSA_OVERRIDE_GFX_VERSION=10.3.0`.
Например: `HSA_OVERRIDE_GFX_VERSION=10.3.0 jupyter lab` или `HSA_OVERRIDE_GFX_VERSION=10.3.0 python3 main.py`


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


## IDE - Jyputer \ Jyputer in VS Code
[Jupyter Lab](https://jupyter.org/) - IDE для анализа данных и МО, основной вид виде интерактивного блокнота (notebook, ipynb файл).
- Имеет веб-интерфейс, поэтому сервер может быть запущен не только локально но и на любой машине, к которой есть доступ.
- Основной типа файлов IDE - Блокнот (notebook, тетрадка). Может содержать код на Питоне (и не только); показывать статичные и интерактивные диаграммы, создаваемые на языке программирования; показывать текст в разметке markdown (включая структурирование с помощью заголовков), формулы в LaTeX.
Позволяет просматривать файлы с табличными данными.
- Jyputer Lab включает в себя возможности среды Jyputer Notebook. 
- Подобная Jyputer Notebook IDE (в качестве основы) используется в [Google Colaboratory](https://colab.research.google.com/), среде Kaggle, специальных сервисах для МО в Яндекс Облаке и др. местах
- Поддерживает плагины

**VS Code** тоже поддерживает работу с Jyputer Notebook, позволяет открывать и запускать Jyputer сервер прямо из окна редактора.
Есть возможность выполнять открытый локально ipynb файл на удалённом сервере: <kbd>F1</kbd> > `Notebook: Select notebook kernel` (или нажать на кнопку kernel справа вверху, в открытом блокноте) > Select another > Вставить URL сервера с Jupyter.


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


# Языковые модели с доступом к серверу по API
- OpenAI. ChatGPT (https://platform.openai.com/api-keys)
    - Доступ к API платный (хотя в веб-интерфейсе GPT3.5 доступен бесплатно)
    - Для получения ключа доступа требуется подтвердить номер телефона

# Запуск языковых моделей локально
Программы для работы с большими языковыми моделями (Large Language Models, LLM):
- скачивать модели (формат GGUF)
- запускать языковые модели локально
- предоставляет интерфейс чата для моделей
- ...

- **Jan** https://jan.ai/
- **LM Studio** https://lmstudio.ai/
- Llama.cpp (https://github.com/ggerganov/llama.cpp) и другие

**Модели**
Модели, которые можно запускать на обычном ПК с 16-32 Гб  оперативной памяти - это модели до нескольких миллиардов параметров.
Обычно эти параметры ещё и квантизированы, т.е. вместо исходных типов данных float (16 или 32 бита) параметры хранятся в типах занимающих 8 или даже 4 бита. Это снижает точность модели, но более значимо снижение требований к оперативной памяти.


Ключевые характеристики модели обычно указываются в её названии, например модель `Llama-3 8B Q4` (Large Language Model Meta AI, появилась в апреле 2024) - это модель с 8 мла. параметров, каждый из которых занимает 4 бита. Файл такой модели (формата GGUF) занимает около 4.6 Гб.


ToDo: temperature и др. параметры генерации


