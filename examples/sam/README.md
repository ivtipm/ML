# Коротко SAM

SAM (Segment Anything Model) — семейство моделей Meta для сегментации объектов. В отличие от YOLO,
SAM не распознаёт классы объектов: он выделяет тот объект, который указан подсказкой (prompt).

| Модель | Подсказки | Что находит |
| --- | --- | --- |
| SAM 2 | точка, рамка, маска | один объект, указанный подсказкой; трекинг объекта в видео |
| SAM 3 | текст («all dogs»), пример-картинка (exemplar), точка, рамка | все экземпляры концепции на изображении или в видео |

## Файлы в папке

- `sam2_prompt_segmentation.py` — SAM 2: сегментация по подсказке (точка или рамка), уточнение маски точками.
- `sam3_text_prompt_segmentation.py` — SAM 3: сегментация всех экземпляров концепции по текстовому промпту.
- `models/` — веса `.pt` (при отсутствии файла модель скачается автоматически; веса `sam3.pt` — исключение, см. ниже).
- `../images/` — общая папка с тестовыми изображениями для всех примеров.

## Базовый инференс

```python
from ultralytics import SAM

model = SAM("models/sam2.1_t.pt")   # при отсутствии файла скачается

# подсказка точкой: [x, y] — пиксель внутри объекта, labels=[1] — положительная точка
results = model("../images/peoples_and_dog.jpg", points=[[480, 300]], labels=[1])

# подсказка рамкой: [x1, y1, x2, y2]
results = model("../images/peoples_and_dog.jpg", bboxes=[[600, 350, 850, 600]])

r = results[0]
r.masks.data   # бинарные маски [N, H, W]
r.masks.xy     # контуры объектов в координатах изображения
r.plot()       # картинка BGR с масками
```

Структура результата (`Results`) та же, что у YOLO-моделей, но без `boxes.cls` и `boxes.conf`:
SAM выделяет указанный объект, даже если не знает, как он называется.

Документация: https://docs.ultralytics.com/models/sam-2/

## SAM 3: сегментация по текстовому промпту

SAM 3 находит **все** экземпляры концепции по короткой фразе — пиксель указывать не нужно.
Для текстовых промптов используется отдельный класс `SAM3SemanticPredictor`:

```python
from ultralytics.models.sam import SAM3SemanticPredictor

overrides = {"conf": 0.25, "task": "segment", "mode": "predict", "model": "models/sam3.pt", "verbose": False}
predictor = SAM3SemanticPredictor(overrides=overrides)

predictor.set_image("../images/silicon-valley-season-4.webp")
results = predictor(text=["person"])   # все люди на картинке
results[0].plot()
```

Веса `sam3.pt` (около 3.5 Гб) не скачиваются автоматически: нужно запросить доступ на
https://huggingface.co/facebook/sam3 , дождаться одобрения и скачать файл в `models/`.

Точки и рамки из SAM 2 в SAM 3 тоже работают (`SAM("models/sam3.pt")`), но выделяют
один объект, а не все экземпляры концепции.

Документация: https://docs.ultralytics.com/models/sam-3/
