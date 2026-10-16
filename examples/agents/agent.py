"""
Минимальный ИИ-агент: LLM + инструменты + цикл.

Агент — это цикл, в котором языковая модель решает, какой инструмент
вызвать, программа выполняет вызов, а результат возвращается модели.
Так продолжается до финального ответа:

    вопрос -> LLM -> (инструмент -> результат -> LLM)* -> ответ

Этот пример призван _проиллюстрировать_ то, как работает ИИ агент,
поэтому здесь не используются фреймворки для создания таких агентов

Запуск:
    ollama serve                        # в отдельном терминале
    ollama pull qwen3.5:0.8b              # модель, обученная вызывать инструменты
    pip install ollama
    python agent.py
"""

import ollama


# --- 1. Модель ---------------------------------------------------------
# Нужна модель, обученная вызывать инструменты (в библиотеке ollama такие
# модели помечены тегом `tools`): например qwen2.5, llama3.1, mistral.
MODEL = "qwen3.5:0.8b"

# Режим размышлений. Требует модель с тегом `thinking` (qwen3, deepseek-r1,
# gpt-oss). У обычных моделей оставьте False.
THINK = False


# --- 2. Инструменты ----------------------------------------------------
# Инструмент — это обычная функция Python. ollama сама превращает её
# docstring и аннотации типов в JSON-схему, которую видит модель.
# Docstring пишем в стиле Google: он служит инструкцией для модели —
# что делает функция и когда её вызывать.

def get_weather(city: str) -> str:
    """Return the current weather in a city.

    Use this tool when the user asks about the weather.

    Args:
        city: name of the city, for example "Moscow"
    """
    # Заглушка: в настоящем агенте здесь был бы запрос к погодному API.
    fake_data = {
        "Moscow": "+5 °C, облачно",
        "Sochi": "+22 °C, солнечно",
    }
    return fake_data.get(city, f"нет данных о погоде в {city}")


def calculate(expression: str) -> str:
    """Evaluate an arithmetic expression and return the result.

    Use this tool for any calculations instead of computing in your head.

    Args:
        expression: arithmetic expression, for example "2 + 2 * 3"
    """
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:
        return "ошибка: допустимы только цифры и знаки + - * / ( )"
    return str(eval(expression, {"__builtins__": {}}, {}))


TOOLS = [get_weather, calculate]
TOOLS_BY_NAME = {tool.__name__: tool for tool in TOOLS}


# --- 3. Системный промпт ----------------------------------------------
# Задаёт роль и правила. Здесь полезно напомнить модели, что она должна
# опираться на результат инструментов, а не выдумывать данные.
SYSTEM_PROMPT = (
    "Ты — полезный ассистент. Отвечай кратко. "
    "Если нужны данные или вычисления, используй инструменты "
    "и опирайся на их результат, а не на собственные догадки."
)


# --- 4. Цикл агента ----------------------------------------------------
def run_agent(user_message: str, max_steps: int = 5) -> str:
    """Один запуск агента: от вопроса пользователя до финального ответа."""
    print(f"вопрос: {user_message}")

    # Память агента — это просто список сообщений, который мы дополняем.
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]

    for step in range(1, max_steps + 1):
        print(f"\n--- шаг {step} ---")

        # Запрос к LLM: передаём историю сообщений и список инструментов.
        response = ollama.chat( model=MODEL, messages=messages, tools=TOOLS, think=THINK )
        message = response.message

        # Размышления модели (если включены и поддерживаются моделью).
        if message.thinking:
            print(f"[размышление] {message.thinking.strip()}")

        # Нет запроса на инструмент — значит, это финальный ответ.
        if not message.tool_calls:
            print(f"[ответ] {message.content}")
            return message.content

        # Модель просит вызвать инструмент(ы). Добавляем её ход в историю:
        # без этого модель не поймёт, откуда взялся результат.
        messages.append(message)

        for call in message.tool_calls:
            name = call.function.name
            args = call.function.arguments
            print(f"[действие] {name}({args})")

            # Выполняем инструмент сами — модель лишь попросила об этом.
            tool = TOOLS_BY_NAME.get(name)
            result = tool(**args) if tool else f"ошибка: неизвестный инструмент {name}"
            print(f"[наблюдение] {result}")

            # Возвращаем результат модели как сообщение роли "tool".
            messages.append({
                "role": "tool",
                "tool_name": name,
                "content": str(result),
            })

    return "агент не завершил работу за отведённое число шагов"


if __name__ == "__main__":
    run_agent("Какая сейчас погода в Москве? И сколько будет 17 * 23?")
