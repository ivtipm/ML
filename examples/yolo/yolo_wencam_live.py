# %% Cell 1
import cv2
from ultralytics import YOLO

# Загружаем предобученную модель (n - nano, самая быстрая для реального времени)
model = YOLO("yolo26n.pt")


# %% Cell 10

# Открываем поток с веб-камеры (0 — индекс камеры по умолчанию)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    #- stream=True позволяет эффективно обрабатывать видеопоток
    #- conf=0.5 фильтрует уверенность детекции
    results = model.predict(frame, stream=True, conf=0.5)

    for r in results:
        # .plot() возвращает изображение с отрисованными рамками и подписями
        annotated_frame = r.plot()
        cv2.imshow("YOLO Real-time Detection", annotated_frame)

    # Выход по нажатию клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
