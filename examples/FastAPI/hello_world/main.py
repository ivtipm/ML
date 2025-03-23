"""
Пример сервера, который отвечает на запросы по HTTP API

"""
from random import randint
from fastapi import FastAPI



app = FastAPI()


# get-запрос для корневого эндпоинта, используется в качестве health-check
@app.get("/")
async def root():
    """health-check; в норме выдаёт Ok"""
    # docstring будет виден в /doc
    return {"status": "Ok"}


@app.get("/number")
async def number():
    """Выдаёт случайное число от 0 до 100 включительно"""
    return {"number":  randint(0,100)}

# специальные параметры (summary и description) декоратора станут частью документации
@app.get("/number_with_params", summary="тут короткое описание эндпоинта", description="а тут детальное")
async def number(min:int, max:int):
    """Выдаёт случайное число от min до max включительно"""
    # todo: проверить: min < max
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
  'http://127.0.0.1:8880/number_with_params?min=-50&max=0' \
  -H 'accept: application/json'

или зайти на страницу /doc и сформировать запрос там

"""