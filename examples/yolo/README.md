# Коротко YOLO

YOLO (You Only Look Once) — семейство одностадийных детекторов объектов на изображении.
Библиотека `ultralytics` даёт единый API для нескольких задач:

| Задача | Суффикс модели | Что возвращает |
| --- | --- | --- |
| Детекция | `yolo26n.pt` | рамки `result.boxes` |
| Instance segmentation | `yolo26n-seg.pt` | рамки + маски `result.masks` |
| Pose / keypoints | `yolo26n-pose.pt` | скелеты `result.keypoints` |
| Классификация | `yolo26n-cls.pt` | вероятности `result.probs` |
| OBB (повёрнутые рамки) | `yolo26n-obb.pt` | `result.obb` |

Размер модели задаётся буквой: `n` (nano) → `s` → `m` → `l` → `x`. Чем больше буква, тем выше точность и ниже скорость. Для real-time обычно берут `n` или `s`.

## Файлы в папке

- `yolo.ipynb` — детекция: загрузка модели, инференс на изображении, доступ к `boxes`, своя отрисовка рамок, детекция с веб-камеры.
- `yolo_detection_webcam_live.py` — real-time детекция с камеры: FPS, время инференса, подсчёт объектов по классам.
- `yolo_segmentation.py` — instance segmentation: работа с масками (`masks.data`, `masks.xy`), семантическая сегментация, своя отрисовка.
- `models/` — веса `.pt` (при отсутствии файла модель скачается автоматически).
- `../images/` — общая папка с тестовыми изображениями для всех примеров.
- `requirements.txt` — зависимости (`ultralytics`, `opencv-python`, `pillow`).

## Базовый инференс

```python
from ultralytics import YOLO

model = YOLO("models/yolo26n.pt")   # при отсутствии файла скачается
results = model("../images/peoples_and_dog.jpg")   # список Results, по одному на изображение

r = results[0]
r.boxes.xyxy    # координаты рамок [x1, y1, x2, y2]
r.boxes.conf    # уверенность
r.boxes.cls     # индексы классов
model.names     # {индекс: имя класса}
r.plot()        # картинка BGR с рамками и метками
```

## Параметры `predict()`

#### `conf`

Минимальная уверенность детекции, по умолчанию `0.25`. Ниже — больше находок и ложных срабатываний, выше — только уверенные детекции.

```python
model.predict(source, conf=0.5)
```

#### `iou`

Порог IoU для Non-Maximum Suppression — отбора перекрывающихся рамок, по умолчанию `0.7`. Меньше значение → агрессивнее удаляются дубли, больше → остаётся больше рамок.

```python
model.predict(source, iou=0.5)   # строже к перекрытиям, меньше дублей
```

#### `imgsz`

Размер входа, по умолчанию `640`. Меньше — быстрее и грубее, больше — точнее и медленнее. Можно задать прямоугольник кортежем `(h, w)`.

#### `device`

Устройство вычислений. Если не указать, ultralytics сам выберет GPU, если он доступен, иначе CPU.

```python
model.predict(source, device="cpu")       # CPU
model.predict(source, device=0)           # первая CUDA-видеокарта
model.predict(source, device="cuda:1")    # вторая CUDA-видеокарта
model.predict(source, device="xpu")       # Intel GPU (Arc)
model.predict(source, device="mps")       # Apple Silicon
```

#### `half` / `quantize`

FP16-инференс. Считает в половинной точности: примерно вдвое быстрее и меньше памяти, точность падает незначительно. Имеет смысл на GPU при real-time. На CPU выигрыша нет (там FP32). Более сильное сжатие — INT8, но оно настраивается при экспорте, а не в `predict`.

```python
model.predict(source, half=True)      # FP16 (флаг ultralytics)
model.predict(source, quantize=16)    # FP16 в свежих версиях (half устарел)
```

#### `augment`

Test-time augmentation, по умолчанию `False`. Модель прогоняет несколько вариантов входа (отражения, масштабы) и объединяет результаты: точность растёт, скорость падает в несколько раз. Для разового прогона на сложных изображениях, не для real-time.

```python
model.predict(source, augment=True)
```

#### `rect`

Rectangular inference, по умолчанию `True`. Изображение масштабируется под `imgsz` и дополняется (padding) только до ближайшего кратного stride, а не до полного квадрата: меньше лишних пикселей → быстрее. Работает, когда все изображения в батче одного размера. `rect=False` всегда приводит вход к полному `imgsz` — это нужно для экспортированных моделей с фиксированным входом (ONNX, TensorRT).

#### `classes`, `max_det`, `agnostic_nms`

Фильтр по классам (`classes=[0, 41]`), лимит объектов на изображение (`max_det`, по умолчанию `300`), NMS без учёта класса (`agnostic_nms`).

#### `stream`, `verbose`

`stream=True` возвращает генератор вместо списка — экономит память на видео. `verbose=False` отключает логи на каждом кадре.

## Форматы инференса

Примеры в этой папке используют `.pt` (PyTorch) — так удобно учиться. В промышленной эксплуатации модель экспортируют в формат ONNX и загружают так же:

```python
model.export(format="onnx")          # создаст yolo26n.onnx
model = YOLO("yolo26n.onnx")         # инференс через ONNX Runtime
```

ONNX выгоден тем, что статический граф исполняется специализированным рантаймом (ONNX Runtime, TensorRT, OpenVINO), который заранее оптимизирует вычисления: сливает операции, убирает лишние узлы и подбирает ядра под железо. Это даёт ускорение в разы на CPU и убирает зависимость от PyTorch при развёртывании. Плюс формат хранит веса в FP16/INT8, что снижает трафик памяти.

Популярные форматы: ONNX (универсальный), TensorRT (NVIDIA), OpenVINO (Intel).

## Отслеживание объектов

```python
results = model.track(source, persist=True)   # присваивает объектам id между кадрами
```

## Полезные приёмы

```python
# только нужные классы (0 — person, 41 — cup)
model.predict(source, classes=[0, 41])

# видео: генератор вместо списка, экономит память
for r in model.predict("video.mp4", stream=True):
    frame = r.plot()

# отключить логи на каждом кадре
import logging
logging.getLogger("ultralytics").setLevel(logging.CRITICAL)
```

Документация: https://docs.ultralytics.com
