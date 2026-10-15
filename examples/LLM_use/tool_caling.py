# Пример вызова инструментов LLM

from random import randint
import ollama


def dice(max: int) -> int:
    """Roll a die and return a random integer from 1 to max.

    Use this function when the user asks to roll a die , throw dice,
    or get a random number up to a given maximum.
    Examples: "roll a dice 10", max = 10; "roll d20", max = 20

    Args:
        max (int): maximum number of sides / the upper bound of the roll

    Returns:
        int: random integer from 1 to max
        if max == 0, return 9999

    """
    if max == 0:
        return 9999
    else:
        return randint(1, max)


# MODEL_TOOLS = "functiongemma:latest"
# qwen3.5:0.8b
MODEL_TOOLS = "granite4.2:3b"
MODEL_ANSWER = "granite4.2:3b"


def test_call(message: str = "roll d20") -> list[dict]:
    Messages = [{'role': 'user', 'content': message}]

    r = ollama.chat(model=MODEL_TOOLS, messages=Messages, tools=[dice])
    # Используем chat, а не generate так как будет несколько обращений к LLM

    if r.message.tool_calls:
        # print(r.message)
        call = r.message.tool_calls[0]
        # print( f"Вызовы: {r.message.tool_calls}")
        # print( f"Аргументы: {call.function.arguments}")
        print(f"> вызываем функцию с аргументом {call.function.arguments}")
        result = dice(**call.function.arguments)      # выполняем сами
        print(f"> Функция выдала: {result}")

        Messages.append(r.message)      # LLM важно видеть не только результат (что ниже), но и сам факт вызова функции
        Messages.append({'role': 'tool', 'content': str(result)})
        r = ollama.chat(model=MODEL_ANSWER, messages=Messages, tools=[dice])
        print("===Ответ:")
        print(r.message.content)
        print("===")
        return Messages
    else:
        print("> Нет вызова функции :(")
        return Messages



TEST_PROMPTS = ["roll a die with max=10 and tell me the result.",
                "roll d20",
                "roll d2", "roll d0",
                "tell me a joke",
                "rolling stones"]

for prompt in TEST_PROMPTS:
    print(f"prompt: {prompt}")
    chat_history = test_call(prompt)
    print(chat_history)
    print("\n")
