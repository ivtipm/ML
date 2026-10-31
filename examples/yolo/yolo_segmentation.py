# %% [markdown]
# # Сегментация объектов. YOLO26
#
# Задача instance segmentation: для каждого объекта находится маска.
#
# Модель YOLO26 вышла в январе 2026 года (пример детекции — в ноутбуке `yolo.ipynb`).
# Для сегментации используются модели с суффиксом `-seg`, предобученные на датасете COCO.
#
# Документация:
# - задача сегментации: https://docs.ultralytics.com/tasks/segment/
# - класс Results: https://docs.ultralytics.com/reference/engine/results/



# %% Cell 10
from urllib.request import urlretrieve
import numpy as np

from PIL import Image, ImageDraw
from ultralytics import YOLO

from pathlib import Path

# %% [markdown]
# ### Загрузка предварительно обученной модели


# %% Cell 20
MODELS_DIR = Path("models/")
IMAGES_DIR = Path("images/")
MODEL = "yolo26n-seg.pt"   #  nano (n) — самая маленький и быстрый вариант модели, есть ещё s / m / l / x
model = YOLO( MODELS_DIR / MODEL )
# если модели по заданному пути нет, то она скачается и сохранится в этой папке

# %%
# имена классов, которые распознаёт обученная модель (те же 80 классов COCO, что и при детекции)
LabelNames = model.names
LabelNames

# %% [markdown]
# ### Распознавание на изображении

# %%
# изображение для проверки
image_path = IMAGES_DIR / "test-image3.jpg"
image_path = IMAGES_DIR / "silicon-valley-season-4.webp"

Image.open(image_path)

# %%
# применение модели
result = model(image_path)   # возвращает список из объектов Results, длина списка = кол-во изображений

# классы найденных объектов
print("классы:  ", [LabelNames[int(c)] for c in result[0].boxes.cls])
print("уверенность:", [f"{c:.2f}" for c in result[0].boxes.conf])

# У сегментации к рамкам (result[0].boxes) добавляются маски (result[0].masks):
#   result[0].masks.data — бинарные маски (тензор [N, H, W], 1 — пиксель принадлежит объекту)
#   result[0].masks.xy   — контуры объектов в координатах изображения (списки точек-полигонов)
# result[0].plot() — картинка (numpy array, порядок каналов BGR) с рамками, масками и метками


# %% [markdown]
# ### Работаем с масками

# %%
# просмотрим все маски
# result[0].masks.data — тензор [N, H, W]: N бинарных масок, 1 — пиксель принадлежит объекту
masks = result[0].masks.data.cpu().numpy()
print("размерность тензора масок:", masks.shape)
# первая размерность -- количество обнаруженных объектов
# порядок масок в result[0].masks такой же как и в result[0].boxes.cls

masks_combined = masks.sum(axis=0)  # сложим все маски
masks_combined = np.clip( masks_combined*255, a_min=0, a_max=255, dtype=np.uint8)           # приведём сумму масок к яркостям пикселей 0 или 255
Image.fromarray( masks_combined )

# %%
# маски только людей (класс person, id 0), без картинки в фоне
image = Image.open(image_path).convert("RGB")

person_canvas = Image.new("RGB", image.size, "white")
draw = ImageDraw.Draw(person_canvas, "RGBA")

for i, polygon in enumerate(result[0].masks.xy):
    if int(result[0].boxes.cls[i]) == 0:   # 0 — person
        draw.polygon([tuple(p) for p in polygon], fill=(255, 0, 0, 150), outline=(255, 0, 0, 255))

person_canvas

# %%
# все маски сразу, без картинки — каждому объекту свой цвет
colors = [(255, 0, 0), (0, 200, 0), (0, 100, 255), (255, 200, 0), (200, 0, 255), (0, 220, 220)]

masks_canvas = Image.new("RGB", image.size, "black")
draw = ImageDraw.Draw(masks_canvas, "RGBA")

for i, polygon in enumerate(result[0].masks.xy):
    draw.polygon([tuple(p) for p in polygon], fill=colors[i % len(colors)])

masks_canvas

# %%
# какой вид сегментации выполнен?
# Instance segmentation: у каждого объекта своя маска — на картинке выше объекты одного класса,
# например люди, выделены разными цветами.
# Если объединить маски объектов одного класса, получится семантическая сегментация — один цвет на класс:

classes = [int(c) for c in result[0].boxes.cls]
class_colors = {c: colors[i % len(colors)] for i, c in enumerate(sorted(set(classes)))}
print("цвета классов:", {LabelNames[c]: class_colors[c] for c in sorted(class_colors)})

semantic = Image.new("RGB", image.size, "black")
draw = ImageDraw.Draw(semantic, "RGBA")
for i, polygon in enumerate(result[0].masks.xy):
    draw.polygon([tuple(p) for p in polygon], fill=class_colors[int(result[0].boxes.cls[i])])

semantic

# %% [markdown]
# ### Нарисовать маски

# %%
# готовая визуализация
annotated = result[0].plot()
Image.fromarray(annotated[:, :, ::-1])   # BGR -> RGB

# %%
# своя отрисовка: полупрозрачные маски + подписи
image = Image.open(image_path).convert("RGB")
draw = ImageDraw.Draw(image, "RGBA")

for i, polygon in enumerate(result[0].masks.xy):
    if len(polygon) < 3:   # контур из менее чем 3 точек не нарисовать
        continue
    color = colors[i % len(colors)]
    draw.polygon([tuple(p) for p in polygon], fill=color + (100,), outline=color, width=3)

    class_id = int(result[0].boxes.cls[i])
    confidence = float(result[0].boxes.conf[i])
    x, y = polygon.min(axis=0)
    draw.text((x, y - 20), f"{LabelNames[class_id]} {confidence:.2f}", fill="red")

image
