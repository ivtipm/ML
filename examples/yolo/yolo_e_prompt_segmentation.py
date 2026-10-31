# %% Cell 10
from pathlib import Path
from ultralytics import YOLOE
# дополнительно, для YOLOE требуется CLIP; может быть установлен автоматически после запуска модели
# git+https://github.com/ultralytics/CLIP.git

MODELS_DIR = Path("models/")
IMAGES_DIR = Path("images/")
MODEL = "yoloe-26l-seg.pt"

model = YOLOE(MODELS_DIR / MODEL)


# %% Cell 20
# "double-decker bus" is not a COCO class; YOLOE resolves it from the words alone
model.set_classes(["lab flask", "wall calender", "wall pinboard", "box", "lab equipment", "orange fluid", "blue chair", "brown chair", "note", "paper", "box", "can", "crown", "weapon", "time", "door", "lamp", "thrash can"] )

# image_path = IMAGES_DIR / "Garage.webp"
image_path = IMAGES_DIR / "Garage2.png"

results = model.predict(image_path, conf=0.1)
results[0].show()
