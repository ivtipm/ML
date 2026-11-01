# %% [markdown]
# # Классификация изображений с открытым словарём. Vision LLM
#
# Zero-shot классификация: список классов задаётся в промпте, модель не
# дообучалась на них. Это открытый словарь (open vocabulary) — классы можно
# менять без переобучения, в отличие от CNN и YOLO-cls.
#
# VLM (Visual Language Model) генерирует
# ответ, поэтому может назвать класс вне списка или спорный. Structured output
# (структурированный вывод) заставляет модель вернуть JSON по заданной схеме:
# `enum` гарантирует, что ответ — один из заданных классов.
#
# Требуется установленный Ollama: https://ollama.com/download
# Смю также decision models

# %% Cell 10
import json
from pathlib import Path

from PIL import Image
import ollama

# %% [markdown]
# ### Модель и изображения

# %% Cell 20
MODEL = "qwen3.5:2b-q8_0"   # маленькая мультимодальная модель, 2.7 ГБ
# для слабых ноутбуков: "gemma4:31b-cloud" — код не меняется, только имя

IMAGES_DIR = Path("../images/")   # общая папка с картинками для всех примеров

image_path = IMAGES_DIR / "peoples_and_dog.jpg"
Image.open(image_path)

# %% [markdown]
# ### Классификация со структурированным выводом
#
# Обычный ответ VLM — свободный текст: модель может написать лишнее или назвать
# класс вне списка. Параметр `format` передаёт модели JSON-схему, и она обязана
# вернуть JSON, соответствующий этой схеме.
#
# Схема описывает структуру ответа:
#
# - `type: "object"` — ответ должен быть JSON-объектом (словарь в Python);
# - `properties` — какие поля должны быть в объекте, и какого они типа:
#   поле `class` — строка, причём `enum` перечисляет единственные допустимые
#   значения (наши классы); поле `explanation` — тоже строка, без ограничений;
# - `required` — какие поля обязательны; без этого списка модель могла бы
#   вернуть только часть полей.
#
# Модель генерирует не произвольный текст, а токены, из которых собирается
# валидный JSON: недопустимое значение класса физически не может появиться.
# Просим краткое обоснование, чтобы ответ можно было проверить.

# %% Cell 30
classes = ["dog", "person", "cat", "car"]

schema = {
    "type": "object",   # ответ — JSON-объект (словарь)
    "properties": {
        "class": {"type": "string", "enum": classes},   # enum — только классы из списка
        "explanation": {"type": "string"},   # краткое обоснование, тип строка
    },
    "required": ["class", "explanation"],   # без этого поля модель может опустить
}

response = ollama.chat(
    model=MODEL,
    messages=[{
        "role": "user",
        "content": "Which class does the image show? Choose exactly one: "
                   + ", ".join(classes),
        "images": [str(image_path)],
    }],
    format=schema,   # структурированный вывод: ответ будет JSON по этой схеме
    think=False,
)

result = json.loads(response.message.content)
print(result)

# %% [markdown]
# ### Несколько изображений

# %% Cell 40
def classify(image_path, classes):
    # та же схема, что и выше; параметры — чтобы вызывать для разных классов
    schema = {
        "type": "object",
        "properties": {
            "class": {"type": "string", "enum": classes},
            "explanation": {"type": "string"},
        },
        "required": ["class", "explanation"],
    }
    response = ollama.chat(
        model=MODEL,
        messages=[{
            "role": "user",
            "content": "Which class does the image show? Choose exactly one: "
                       + ", ".join(classes),
            "images": [str(image_path)],
        }],
        format=schema,
        think=False,
    )
    return json.loads(response.message.content)


# %%
# изображения для проверки
for name in ["Garage.webp", "silicon-valley-season-4.webp"]:
    Image.open(IMAGES_DIR / name)

# %%
# результаты классификации
for name in ["peoples_and_dog.jpg", "Garage.webp", "silicon-valley-season-4.webp"]:
    print(name, "→", classify(IMAGES_DIR / name, classes))

# %% [markdown]
# ### Ограничение фиксированного списка
#
# На Garage.webp нет ни одного из заданных классов, но enum заставил модель
# выбрать car — с обоснованием, что машины на картинке нет. Если класс может
# отсутствовать, его стоит добавить в список явно.

# %%
result = classify(IMAGES_DIR / "Garage.webp", classes + ["none of the above"])
print(result)

# %% [markdown]
# ### Открытый словарь
#
# Классы не обязаны быть именами объектов — это могут быть любые свойства
# сцены, которые можно сформулировать словами. CLIP с таким справится хуже:
# ему нужна короткая фраза-метка, а рассуждение о сцене он не умеет.

# %% Cell 50
scene_classes = ["сделано на улице", "сделано в помещении"]

for name in ["peoples_and_dog.jpg", "Garage.webp"]:
    print(name, "→", classify(IMAGES_DIR / name, scene_classes))

# %% [markdown]
# ### Ограничения
#
# - VLM медленнее CLIP: генерация текста вместо одного прохода энкодера.
# - Уверенность модели не откалибрована, как вероятности CLIP; поле
#   `explanation` показывает основание решения, но не вероятность.
# - Модель может ошибаться на редких классах и галлюцинировать в обосновании —
#   ответ всегда стоит проверять на своих данных.
