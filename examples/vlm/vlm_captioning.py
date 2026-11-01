# %% [markdown]
# # Описание изображений. Vision LLM
#
# Задача аннотирования изображений (image captioning): модель получает изображение и текстовую инструкцию,
# а возвращает текстовое описание. В отличие от детекторов и сегментаторов,
# визуальная LLM (VLM) не обучена на фиксированном списке классов — она
# описывает изображение свободным текстом, а содержание ответа задаёт промпт.
#
# Модель Qwen3.5 мультимодальна во всех размерах (от 0.8b до 122b): принимает
# текст и изображение. Используем 2b — быстрый вариант для ноутбука.
# Требуется установленный Ollama: https://ollama.com/download
#
# Документация:
# - vision-модели в Ollama: https://docs.ollama.com/capabilities/vision
# - библиотека ollama для Python: https://github.com/ollama/ollama-python

# %% Cell 10
from pathlib import Path

from PIL import Image
import ollama

# %% [markdown]
# ### Модель

# %% Cell 20
MODEL = "qwen3.5:2b-q8_0"   # маленькая мультимодальная модель, 2.7 ГБ
# на слабом ноутбуке можно взять облачную модель — код не меняется, только имя:
# MODEL = "gemma4:31b-cloud"

# системный промпт задаёт поведение модели для всех запросов;
# без него маленькая модель иногда вставляет в русский текст слова на других языках
SYSTEM = {"role": "system", "content": "Ты помощник. Отвечай на русском."}

# %% [markdown]
# ### Изображение

# %% Cell 30
IMAGES_DIR = Path("../images/")   # общая папка с картинками для всех примеров
image_path = IMAGES_DIR / "peoples_and_dog.jpg"

Image.open(image_path)

# %% [markdown]
# ### Простое описание

# %% Cell 40
# изображение передаётся в поле images сообщения; библиотека принимает путь к файлу,
# байты или base64-строку (в REST API изображение кодируется base64)
response = ollama.chat(
    model=MODEL,
    messages=[SYSTEM, {
        "role": "user",
        "content": "Опиши изображение двумя-тремя предложениями.",
        "images": [str(image_path)],
    }],
    think=False,   # qwen3.5 умеет рассуждать перед ответом; для описания это не нужно
)
print(response.message.content)

# %% [markdown]
# ### Промпт управляет содержанием ответа
#
# Одно и то же изображение, разные инструкции — разная степень детальности
# и разные акценты. Так VLM удобно извлекать из картинки именно то, что нужно
# для задачи.

# %% Cell 50
# короткое описание одним предложением
response = ollama.chat(
    model=MODEL,
    messages=[SYSTEM, {
        "role": "user",
        "content": "Опиши изображение одним предложением.",
        "images": [str(image_path)],
    }],
    think=False,
)
print(response.message.content)

# %% Cell 60
# описание по заданному плану: модель отвечает на конкретные вопросы
response = ollama.chat(
    model=MODEL,
    messages=[SYSTEM, {
        "role": "user",
        "content": "Опиши изображение по плану, кратко — один пункт одно предложение: 1) где происходит сцена, "
                   "2) какие объекты и сколько их, 3) что делают люди.",
        "images": [str(image_path)],
    }],
    think=False,
)
print(response.message.content)

# %% Cell 70
# другой тип изображения
image_path2 = IMAGES_DIR / "Garage.webp"
Image.open(image_path2)

# %% Cell 80
response = ollama.chat(
    model=MODEL,
    messages=[SYSTEM, {
        "role": "user",
        "content": "Опиши изображение по плану, кратко — один пункт одно предложение: 1) что за помещение, "
                   "2) какие объекты и сколько их, 3) что вызывает вопросы.",
        "images": [str(image_path2)],
    }],
    think=False,
)
print(response.message.content)

# %% [markdown]
# ### Другая модель — другое описание
#
# Капченинг не имеет «единственно верного ответа»: разные модели описывают
# одну картинку по-разному. Сравним с Gemma 4 (мультимодальна, как и Qwen3.5,
# во всех размерах).

# %% Cell 90
MODEL2 = "gemma4:e2b-it-qat"   # 4.3 ГБ, модель должна быть скачана в Ollama

response = ollama.chat(
    model=MODEL2,
    messages=[SYSTEM, {
        "role": "user",
        "content": "Опиши изображение двумя-тремя предложениями.",
        "images": [str(image_path)],
    }],
    think=False,
)
print(response.message.content)

# %% [markdown]
# ### Вопрос по изображению (VQA)
#
# Та же модель отвечает и на конкретные вопросы по картинке — задача
# Visual Question Answering.

# %% Cell 100
response = ollama.chat(
    model=MODEL,
    messages=[SYSTEM, {
        "role": "user",
        "content": "Какая порода собаки на изображении? Ответь одним словом.",
        "images": [str(image_path)],
    }],
    think=False,
)
print(response.message.content)
