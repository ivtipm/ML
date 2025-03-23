"""
Пример сервера, который отвечает на запросы по HPTP API

"""
from random import randint
from fastapi import FastAPI



app = FastAPI()


# get-запрос для корневого эндпоинта, используется в качестве health-check
@app.get("/")
async def root():
    return {"ststus": "Ok"}


@app.get("/number")
async def number():
    return {"number":  randint(0,100)}


@app.get("/number_with_params")
async def number(min:int, max:int):
    return {"number":  randint(min,max)}


# эндпоинты /, /number и .number_with_params в терминах FastAPI называются маршрутами

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


# Проверить работоспособность:
"""

curl -X 'GET' \
  'http://127.0.0.1:8888/number_with_params?min=-50&max=0' \
  -H 'accept: application/json'

или зайти на страницу /doc и сформировать запрос там

"""