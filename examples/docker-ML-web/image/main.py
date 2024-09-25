# Пример веб-сервера, который предоставляет интерфейс для рисования цифр для последующего распознавания случайным лесом

# Для моделей рекомендуются создавать сервер запросов, к которому можно обращаться через веб-API. 

import numpy as np
import gradio as gr                 # для интерфейса
from joblib import load, dump       # для загрузки файла модели

# файл обученной модели
MODEL_FILE = 'forest.joblib.lzma'


def predict(img: np.ndarray):
    """Обработчик отправки формы; Распознаёт по картинке число, выдаёт top1 лейбл класса;
    img — np.ndarray[28, 28]
    Model — модель с методом predict"""
    global Model
    # predict принимает список из объектов; возвращает тоже список из ответов
    return Model.predict( img.reshape(1,-1) ) 
    # img.reshape(1,-1)  -> shape[ 1, auto ]; здесь будет auto = 784



# обученная модель sklearn RandomForestClassifier сохранена так
# dump(forest, 'forest.joblib', compress=9) 
# загрузка модели; важно чтобы версии joblib для сохранения и загрузки совпадали
Model = load(MODEL_FILE)


# todo: изменить под новую версию gradio, где всё поменяли...
# панель для рисования; image_mode = L - ч/б изображение
canvas = gr.inputs.Image(shape=(28,28), image_mode="L", invert_colors=True, 
                         source="canvas", tool="editor", type="numpy")



demo = gr.Interface(fn=predict, inputs=canvas, outputs="text")
demo.launch(show_api=False, server_name="0.0.0.0", server_port=7860)   
# в основной ос: http://localhost:7860