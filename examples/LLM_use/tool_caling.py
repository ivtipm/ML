"""
Пример вызова инструментов (tools / function calling) для LLM.

Здесь рассматривается очень простая задача -- генерация случайного числа,
с которой легко справляется код на питоне (или на другом языке программирования),
но плохо справляется LLM.

LLM способна определить когда нужно вызывать функцию, сгенерировать текстовую команду вызора,
а сам вызов сделает программа. Затем результат возвращается модели,
и она формулирует ответ пользователю.
Один шаг выглядит так:
  user  ->  LLM решает вызвать функцию  ->  tool_calls
        ->  наш код выполняет функцию   ->  результат
        ->  результат уходит обратно в LLM  ->  финальный ответ
"""

from ollama._utils import convert_function_to_tool
from random import randint
import ollama


# Docstring функции важен: ollama-python превращает его в JSON-схему инструмента
# (описание + параметры). Чем понятнее описание и примеры, тем точнее модель
# выбирает функцию и её аргументы.
def dice(max: int) -> int:
    """Roll a die and return a random integer from 1 to max.

    Use this function when the user asks to roll a die, throw dice,
    or get a random number up to a given maximum.

    Examples:
           "roll a die with 12 sides"    -> max = 12
           "roll a d20"                  -> max = 20
           "roll a die with 6 sides"     -> max = 6
           "roll a die"                  -> max = 6
           "throw a dice 10"             -> max = 10
           "random number from 1 to 100" -> max = 100
           "🎲"                          -> max = 10

    Args:
        max (int): maximum number of sides / the upper bound of the roll
    """
    if max == 0:
        # Заглушка для теста "roll d0": randint(1, 0) упал бы с ValueError.
        return 9999
    else:
        return randint(1, max)


# Используем две модели: одна выбирает инструмент (должна быть обучена этому), другая формулирует ответ.
# Так можно взять быструю модель для tools и модель получше для текста.
# Но модели могут быть и одинаковыми, тогда главное чтобы обе были обучены на вызов инструментов и могли отвечать обычным текстом
# MODEL_TOOLS = "granite4.2:3b"
MODEL_TOOLS = "functiongemma:latest"
MODEL_ANSWER = "lfm2.5-thinking:1.2b"


def test_call(message: str = "roll d20") -> str:
    messages = [
        # Системный промпт задаёт роль и просит опираться на результат инструмента.
        # {'role': 'system', 'content': 'You are a helpful assistant. Use the tool result to answer the user.'},
        {'role': 'user', 'content': message},
    ]

    # Первый вызов: передаём список инструментов в параметре tools.
    # tools есть только у chat (у generate такого параметра нет),
    # поэтому используем именно chat.
    r = ollama.chat(model=MODEL_TOOLS, messages=messages, tools=[dice], options={'temperature': 0.0} )
    # если передавать tools, то в системный прмпт будет добавлено опсиание того, что LLM должна вызывать инструмент

    if r.message.tool_calls:
        # Модель не выполнила функцию, а попросила нас это сделать.
        # В tool_calls лежат имя функции и аргументы.
        call = r.message.tool_calls[0]
        print(f"> вызываем функцию с аргументом {call.function.arguments}; ", end="")

        # Выполняем функцию сами и получаем результат.
        result = dice(**call.function.arguments)
        print(f"> Функция выдала: {result}")

        # Возвращаем модели ход диалога: сначала её ответ с tool_calls,
        # затем результат работы функции. Без сообщения ассистента модель
        # не поймёт, откуда взялся результат, и ответ может быть пустым.
        messages.append(r.message)
        messages.append({'role': 'tool', 'tool_name': call.function.name, 'content': str(result)})

        # Второй вызов: просим сформулировать ответ. Инструменты больше не нужны,
        # иначе модель может вызвать функцию повторно вместо ответа.
        # Если модель reasoning-типа, ответ может уйти в thinking — тогда
        # помогает think=False.
        r = ollama.chat(model=MODEL_ANSWER, messages=messages)
        print("===Ответ===")
        print(r.message.content)
        return r.message.content

    # Модель не захотела вызывать функцию.
    raise Exception("No function call")


# Прогоняем несколько формулировок, чтобы увидеть, как модель выбирает
# функцию и аргументы. "roll d0" — крайний случай (некорректный аргумент).
TEST_PROMPTS = ["roll a die with 12 sides", "throw a dice 10", "roll a die", "🎲", "roll d20", "roll d20", "roll d2", "roll d6", "roll d0"]
Errors = 0
for prompt in TEST_PROMPTS:
    print(f"prompt: {prompt}")
    try: test_call(prompt)
    except Exception as e: print(f"\nerror: {e}"); Errors += 1
    print("\n")


print(f"всего вызовов {len(TEST_PROMPTS)}, ошибок {Errors}")
