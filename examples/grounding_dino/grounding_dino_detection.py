# %% [markdown]
# # Zero-shot детекция по текстовому промпту. Grounding DINO
#
# Классический детектор (YOLO, Faster R-CNN) ищет объекты из фиксированного набора классов,
# заданного при обучении. Grounding DINO (IDEA Research, 2023) — open-set детектор: классы
# не фиксированы, объекты задаются текстом в момент инференса. На вход — изображение и фразы
# вида «person. dog.», на выходе — рамки с оценками уверенности.
#
# Архитектурно это DETR-подобный трансформер, в который встроен текстовый энкодер (BERT):
# признаки изображения и текста сливаются на нескольких уровнях (feature enhancer),
# а декодер сопоставляет объектные запросы со словами промпта. За счёт этого модель
# достигает 52.5 AP zero-shot на COCO — без дообучения на аннотациях COCO.
#
# Типичное применение — автоматическая разметка данных: детектор находит объекты по тексту,
# а сегментатор (SAM) дорисовывает маски. Эта связка известна как Grounded SAM.
#
# Здесь используется реализация из Hugging Face `transformers`. Открыты веса оригинальной
# модели; более новые версии (Grounding DINO 1.5/1.6, DINO-X) доступны только через API.
#
# Документация: https://huggingface.co/docs/transformers/model_doc/grounding-dino


# %%
import torch
from PIL import Image, ImageDraw
from transformers import AutoModelForZeroShotObjectDetection, AutoProcessor

# %% [markdown]
# ### Загрузка модели
#
# Веса `grounding-dino-tiny` (около 0.2 млрд параметров) скачиваются с Hugging Face Hub
# автоматически при первом запуске и кэшируются локально. Есть ещё `grounding-dino-base` —
# точнее, но тяжелее. Для инференса желателен GPU, на CPU тоже работает, но медленно.


# %%
MODEL_ID = "IDEA-Research/grounding-dino-tiny"

device = "cuda" if torch.cuda.is_available() else "cpu"
processor = AutoProcessor.from_pretrained(MODEL_ID)
model = AutoModelForZeroShotObjectDetection.from_pretrained(MODEL_ID).to(device)

# %% [markdown]
# ### Изображение
#
# Общая папка с тестовыми картинками для всех примеров.


# %%
IMAGE_PATH = "../images/peoples_and_dog.jpg"
img = Image.open(IMAGE_PATH).convert("RGB")
print(f"resolution: {img.width}x{img.height}")
img

# %% [markdown]
# ### Детекция по текстовому промпту
#
# Промпт — перечисление классов строчными буквами, разделённых точкой: `"a person. a dog."`.
# Процессор сам объединяет список меток в такую строку, поэтому можно передать и список.
# Два порога: `threshold` отсекает слабые детекции по общей уверенности, `text_threshold`
# определяет, какие слова промпта считать описанием найденного объекта.


# %%
PROMPT = "person. dog."

inputs = processor(images=img, text=PROMPT, return_tensors="pt").to(device)
with torch.no_grad():
    outputs = model(**inputs)

results = processor.post_process_grounded_object_detection(
    outputs,
    inputs.input_ids,
    threshold=0.4,
    text_threshold=0.3,
    target_sizes=[img.size[::-1]],   # PIL хранит (width, height), модели нужен (height, width)
)
result = results[0]
result

# %%
# визуализация: рамки и подписи рисуем средствами PIL
def draw_detections(image, det):
    draw = ImageDraw.Draw(image)
    for box, score, label in zip(det["boxes"], det["scores"], det["text_labels"]):
        x1, y1, x2, y2 = box.tolist()
        draw.rectangle([x1, y1, x2, y2], outline="red", width=3)
        draw.text((x1, max(y1 - 14, 0)), f"{label} {score:.2f}", fill="red")
    return image


draw_detections(img.copy(), result)

# %%
# у каждой детекции рамка в пикселях (x1, y1, x2, y2), оценка уверенности и текстовая метка,
# извлечённая из промпта
for box, score, label in zip(result["boxes"], result["scores"], result["text_labels"]):
    x1, y1, x2, y2 = box.tolist()
    print(f"{label:<10} score={score:.2f}  box=({x1:.0f}, {y1:.0f}, {x2:.0f}, {y2:.0f})")

# %% [markdown]
# ### Другой промпт на той же картинке
#
# Классы не фиксированы: меняем текст — детектируем другое, без переобучения и без
# повторной загрузки модели. Формулировка влияет на результат: «dog» и «a black dog»
# могут дать разные рамки.


# %%
PROMPT = "a dog."

inputs = processor(images=img, text=PROMPT, return_tensors="pt").to(device)
with torch.no_grad():
    outputs = model(**inputs)

result = processor.post_process_grounded_object_detection(
    outputs,
    inputs.input_ids,
    threshold=0.4,
    text_threshold=0.3,
    target_sizes=[img.size[::-1]],
)[0]

draw_detections(img.copy(), result)

# %% [markdown]
# ### Пороги уверенности
#
# При низком `threshold` модель начинает находить лишнее — типичная проблема zero-shot
# детекторов: они выдают гипотезы почти для любого текста. Пороги подбирают под задачу:
# для авторазметки берут пониже и фильтруют вручную, для автоматической работы — повыше.


# %%
PROMPT = "person. dog. chair. bottle."

inputs = processor(images=img, text=PROMPT, return_tensors="pt").to(device)
with torch.no_grad():
    outputs = model(**inputs)

result = processor.post_process_grounded_object_detection(
    outputs,
    inputs.input_ids,
    threshold=0.2,          # низкий порог: больше детекций, больше шума
    text_threshold=0.25,
    target_sizes=[img.size[::-1]],
)[0]

draw_detections(img.copy(), result)

# %% [markdown]
# ### Что дальше
#
# Grounding DINO выдаёт только рамки. В классическом пайплайне авторазметки поверх него
# запускают SAM: рамки подаются как box-промпты, и на выходе получаются маски. См.
# `grounding_dino_sam_pipeline.py`. Для сравнения: YOLOE делает open-vocabulary детекцию
# и сегментацию одной моделью в реальном времени, а SAM 3 находит все экземпляры концепции
# по тексту без отдельного детектора.
