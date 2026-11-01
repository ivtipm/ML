# %% [markdown]
# # Сегментация по текстовому промпту. SAM 3
#
# В SAM 2 объект нужно было указывать вручную — точкой или рамкой. SAM 3 (Meta, ноябрь 2025)
# умеет больше: по короткой текстовой фразе («person», «yellow school bus») он сам находит
# и выделяет **все** экземпляры концепции на изображении. Пиксель выбирать не нужно.
#
# Такой режим называется Promptable Concept Segmentation (PCS). Точки и рамки из SAM 2
# тоже остались — они выделяют один конкретный объект, а текстовый промпт — все похожие.
#
# Документация: https://docs.ultralytics.com/models/sam-3/


# %%
from pathlib import Path

from PIL import Image
from ultralytics.models.sam import SAM3SemanticPredictor

# %% [markdown]
# ### Загрузка модели
#
# Веса `sam3.pt` (около 3.5 Гб) не скачиваются автоматически: нужно запросить доступ
# на странице https://huggingface.co/facebook/sam3 , дождаться одобрения, скачать файл
# и положить его в папку `models/`. Для инференса желателен GPU — модель заметно
# больше и медленнее SAM 2.


# %%
MODELS_DIR = Path("models/")
IMAGES_DIR = Path("../images/")   # общая папка с картинками для всех примеров
MODEL = MODELS_DIR / "sam3.pt"

overrides = {
    "conf": 0.25,        # порог уверенности, как у детекторов
    "task": "segment",
    "mode": "predict",
    "model": str(MODEL),
    "verbose": False,
}
predictor = SAM3SemanticPredictor(overrides=overrides)

# %%
image_path = IMAGES_DIR / "silicon-valley-season-4.webp"
img = Image.open(image_path)
print(f"resolution: {img.width}x{img.height}")
img

# %% [markdown]
# ### Сегментация по текстовому промпту
#
# Изображение загружается в предсказатель один раз (`set_image`), затем можно задавать
# несколько запросов — признаки картинки считаются заново только при смене изображения.
# Промпт — простая именная группа на английском: модель обучена на фразах вида
# «red apple», «person wearing a hat».


# %%
predictor.set_image(str(image_path))

results = predictor(text=["person"])   # найти всех людей на картинке

Image.fromarray(results[0].plot()[:, :, ::-1])   # BGR -> RGB

# %%
# у каждого найденного экземпляра своя маска и своя рамка
result = results[0]
print(f"найдено объектов: {len(result.masks.data)}")
print(f"рамки (x1, y1, x2, y2):\n{result.boxes.data[:, :4].cpu().numpy().round().astype(int)}")

# %% [markdown]
# ### Другая концепция на той же картинке
#
# Меняя промпт, ищем другие объекты без повторной загрузки изображения.
# Формулировка влияет на результат: «laptop» и «computer monitor» дадут разные маски.


# %%
results = predictor(text=["laptop"])

Image.fromarray(results[0].plot()[:, :, ::-1])

# %%
results = predictor(text=["computer monitor"])

Image.fromarray(results[0].plot()[:, :, ::-1])

# %% [markdown]
# ### Несколько промптов одним запросом
#
# Можно передать список фраз сразу — вернётся результат для каждой из них.


# %%
results = predictor(text=["person", "bottle", "keyboard"])

for prompt, r in zip(["person", "bottle", "keyboard"], results):
    n = 0 if r.masks is None else len(r.masks.data)
    print(f"{prompt}: {n} объектов")

# %% [markdown]
# ### Что дальше
#
# Текстовый промпт находит только простые визуальные концепции. Сложные запросы
# («человек, который не держит коробку») SAM 3 сам не решает — для них модель
# комбинируют с мультимодальной LLM (SAM 3 Agent): LLM переводит вопрос в набор
# простых фраз и выбирает подходящие маски из ответа.
