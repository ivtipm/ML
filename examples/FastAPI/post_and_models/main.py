import yaml
from fastapi import FastAPI
from pydantic import BaseModel

# Инициализация приложения
app = FastAPI()


"""
=====================
Модели запроса и ответа

Модель — это Python-класс, который наследуется от pydantic.BaseModel и описывает, какие поля должны быть в данных, какие у них типы, и какие правила валидации применяются.

FastAPI автоматически:
* Проверит, что данные соответствуют этим типам.
* Сгенерирует документацию для Swagger UI.
* Преобразует входные данные в объект Python

Модели отделяют логику работы с данными от логики обработки запросов. Код становится аккуратным и поддерживаемым.
=====================
"""

# пример модели: описывает, что клиент должен отправить.
class UserRequest(BaseModel):
    name: str
    age: int

# описывает, что сервер вернёт
class UserResponse(BaseModel):
    message: str


# специальная функция, котора будет вызываться при старте сервера
@app.on_event("startup")
async def generate_openapi_yaml():
    # автоматическая генерации спецификации для API в yaml
    openapi_schema = app.openapi()
    with open("openapi.yaml", "w") as f:
        yaml.dump(openapi_schema, f, default_flow_style=False, allow_unicode=True)
    print("OpenAPI YAML сгенерирован при запуске сервера!")
    

# =====================
#  Эндпоинты
# =====================

@app.post("/greet", response_model=UserResponse,  summary="Приветствие пользователя")
async def greet_user(user: UserRequest) -> UserResponse:
    """
    Получает имя и возраст пользователя и возвращает приветствие.
    """
    # конвертирует земные годы в марсианские
    years_mars = user.age * 1.88
    return UserResponse(message=f"Привет, {user.name}! Тебе {years_mars} марсианских лет.")


# =====================
#  Запуск сервера
# =====================
# uvicorn main:app --reload --port 8888

# Документация будет доступна по следующим адресам:
# Swagger UI:
# 📌 http://127.0.0.1:8888/docs — Интерактивная документация.
# Там можно сразу протестировать запросы, отправить данные и посмотреть ответы.

# ReDoc:
# 📌 http://127.0.0.1:8888/redoc — Альтернативная, более минималистичная документация.

# Файл OpenAPI:
# 📌 http://127.0.0.1:8888/openapi.json — Спецификация в формате JSON.