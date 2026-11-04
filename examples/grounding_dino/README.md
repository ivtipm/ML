# Коротко Grounding DINO

Grounding DINO (IDEA Research, 2023) — open-set детектор: объекты задаются текстом
в момент инференса, а не фиксированным списком классов при обучении. На вход — изображение
и фразы вида «person. dog.», на выходе — рамки с оценками уверенности. 52.5 AP zero-shot
на COCO без дообучения на аннотациях COCO.

Отличие от YOLO: классический YOLO детектирует только классы из обучающего набора,
Grounding DINO — любые объекты, которые можно описать текстом. Отличие от YOLOE и
YOLO-World: те ставят на скорость (реальное время, edge), Grounding DINO — на точность
и обобщение, ценой медленного трансформерного инференса.

## Версии

| Версия | Доступ | Точность (COCO zero-shot) |
| --- | --- | --- |
| Grounding DINO (2023) | открытые веса, Apache 2.0 | 52.5 AP |
| Grounding DINO 1.5/1.6 Pro | только API IDEA Research | 54.3–55.4 AP |
| DINO-X / DINO-X Pro | только API | 56.0 AP |

Локально запускается только оригинальная модель — её и используем. Свежие версии
закрыты, развитие серии ушло в API и мультимодальные LLM (Rex-Omni).

## Файлы в папке

- `grounding_dino_detection.py` — zero-shot детекция по текстовому промпту: промпты, пороги, визуализация.
- `../images/` — общая папка с тестовыми изображениями для всех примеров.

## Базовый инференс

Реализация из Hugging Face `transformers`, веса скачиваются с Hub автоматически.

```python
import torch
from transformers import AutoModelForZeroShotObjectDetection, AutoProcessor

model_id = "IDEA-Research/grounding-dino-tiny"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForZeroShotObjectDetection.from_pretrained(model_id)

image = Image.open("../images/peoples_and_dog.jpg").convert("RGB")
text = "person. dog."   # строчные буквы, фразы через точку

inputs = processor(images=image, text=text, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

results = processor.post_process_grounded_object_detection(
    outputs,
    inputs.input_ids,
    threshold=0.4,          # порог уверенности детекции
    text_threshold=0.3,     # порог привязки слов промпта к объекту
    target_sizes=[image.size[::-1]],
)
results[0]["boxes"]        # рамки (x1, y1, x2, y2) в пикселях
results[0]["scores"]       # оценки уверенности
results[0]["text_labels"]  # текстовые метки из промпта
```

Документация: https://huggingface.co/docs/transformers/model_doc/grounding-dino

## Пайплайн авторазметки

Классическая связка Grounded SAM: Grounding DINO находит рамки по тексту, рамки подаются
в SAM как box-промпты, на выходе — маски. Так размечали датасеты до появления SAM 3,
который находит все экземпляры концепции по тексту одной моделью
(см. [/examples/sam/sam3_text_prompt_segmentation.py](/examples/sam/sam3_text_prompt_segmentation.py)).
Для реального времени вместо этой связки проще взять YOLOE
(см. [/examples/yolo/yolo_e_prompt_segmentation.py](/examples/yolo/yolo_e_prompt_segmentation.py)).
