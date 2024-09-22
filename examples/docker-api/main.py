"""
Пример сервера, который отвечает на запросы по API
Используется модель классификатор ирисов
"""
from random import randint
from fastapi import FastAPI


app = FastAPI()

# get запрос для корневого эндпоинта
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/classificate")
async def calc_sum(sep_len: float, sep_width:float, pet_len:float, pet_width:float):
    """Возвращает класс (ирис) для заданных значений длины и ширины лепестка и чашелистика"""
    Classes = ["Iris-Setosa", "Iris-Versicolour", "Iris-Virginica"]
    return {"class": Classes[randint(0,2)]}


# эндпоинты / и /calc_sum в терминах FastAPI называются маршрутами

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

Вариант 2
   fastapi dev main.py
   В режиме dev автоперезагрузка включена
   В режиме run - для продакшина, нет.
   https://fastapi.tiangolo.com/fastapi-cli/
"""


# Проверить:
"""

curl -X 'GET' \
  'http://localhost:8880/classificate?sep_len=2&sep_width=2&pet_len=2&pet_width=2' \
  -H 'accept: application/json'

или зайти на страницу /doc и сформировать запрос там

"""