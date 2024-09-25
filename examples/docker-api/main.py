"""
Пример сервера, который отвечает на запросы по API
Используется модель классификатор ирисов
"""
from random import randint
from fastapi import FastAPI
import joblib


app = FastAPI()
Model = joblib.load("rand_forest_model_sk150_joblib142.joblib")
Labels = ["Iris-Setosa", "Iris-Versicolour", "Iris-Virginica"]
print("Model Loaded")


# get-запрос для корневого эндпоинта, используется в качестве health-check
@app.get("/")
async def root():
    return {"ststus": "Ok"}


@app.get("/classify")
async def classify_iris(sep_len: float, sep_width:float, pet_len:float, pet_width:float):
    """Возвращает класс (ирис) для заданных значений длины и ширины лепестка и чашелистика"""
    global Model, Labels
    
    answer = Model.predict( [[sep_len, sep_width, pet_len, pet_width]] )
    return {"class": Labels[int(answer[0])]}


# эндпоинты / и /classify в терминах FastAPI называются маршрутами

# автоматически по пути /docs доступна документация к API в формате фреимворка Swagger
# тут же можно и выполнить запрос чтобы протестировать

"""
Запуск

Вариант 1
    uvicorn main:app --reload --port 8880
    - main - название файла
    - app - название объекта FastAPI
    - --reload - перезапускать сервер если исходники изменились

    uvicorn - это легковесный сервер. 
    FastAPI предоставляет обёртку над обработчиками событий, но ещё нужен сервер, который будет принимать входящее подключение, 
    работать с HTTP соединениями.
"""


# Проверить:
"""

curl -X 'GET' \
  'http://localhost:8880/classificate?sep_len=2&sep_width=2&pet_len=2&pet_width=2' \
  -H 'accept: application/json'

или зайти на страницу /doc и сформировать запрос там

"""