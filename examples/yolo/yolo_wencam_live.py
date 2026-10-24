# %% Cell 01

import cv2
import time
from ultralytics import YOLO
from collections import Counter

# Загружаем модель (nano - самая быстрая для real-time)
model = YOLO("yolo26s.pt")


def show_info(annotated_frame):
    COLOR_BACKGROUND = (0, 0, 0)
    COLOR_TEXT = (255, 255, 255)
    TEXT_HEIGHT = 0.5
    # 3. Рисуем информационную панель
    # Фон для текста (черный прямоугольник для читаемости)
    cv2.rectangle(annotated_frame, (0, 0), (170, 65), COLOR_BACKGROUND, -1)

    # Вывод FPS и времени инференса
    cv2.putText(annotated_frame, f"FPS: {int(fps)}", (5, 15),
                cv2.FONT_HERSHEY_SIMPLEX, TEXT_HEIGHT, COLOR_TEXT, 1)
    cv2.putText(annotated_frame, f"Inference: {inference_time:.1f}ms", (5, 35),
                cv2.FONT_HERSHEY_SIMPLEX, TEXT_HEIGHT, COLOR_TEXT, 1)

    # Вывод списка объектов (например: "person: 2, cup: 1")
    stats_text = ", ".join([f"{k}: {v}" for k, v in counts.items()])
    if len(stats_text) > 50: stats_text = stats_text[:47] + "..."

    cv2.putText(annotated_frame, stats_text, (5, 55),
                cv2.FONT_HERSHEY_SIMPLEX, TEXT_HEIGHT, COLOR_TEXT, 1)


# %% Cell 10
# Открываем веб-камеру
cap = cv2.VideoCapture(0)

# Для расчета FPS
prev_time = 0

print("Запуск детектора... Нажмите 'q' для выхода.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # 1. Инференс
    # stream=True возвращает генератор, что эффективнее по памяти для видео
    results = model.predict(frame, stream=True, conf=0.4, verbose=False)

    # Обрабатываем результаты
    for r in results:
        # Отрисовка рамок и подписей стандартными средствами YOLO
        annotated_frame = r.plot()

        # Извлекаем время инференса (в мс)
        # speed['inference'] - время чистого прохода через нейросеть
        inference_time = r.speed['inference']

        # Считаем количество найденных объектов
        # r.boxes.cls содержит индексы классов всех найденных объектов
        classes = [model.names[int(cls)] for cls in r.boxes.cls]
        counts = Counter(classes)

    # 2. Расчет FPS
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    show_info(annotated_frame)
    cv2.imshow("YOLOv8 Real-time Analysis", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
