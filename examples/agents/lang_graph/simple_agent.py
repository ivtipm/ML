# %% Cell 01

from langchain.tools import tool
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode

MODEL = "qwen3.5:0.8b"


# @tool превращает функцию в инструмент LangChain: docstring становится
# описанием, которое модель видит при выборе инструмента
@tool
def get_weather(city: str) -> str:
    """Return the current weather in a city.

    Use this tool when the user asks about the weather.

    Args:
        city: name of the city, for example "Moscow"
    """
    fake_data = {"Moscow": "+5 °C, облачно", "Sochi": "+22 °C, солнечно"}
    return fake_data.get(city, f"нет данных о погоде в {city}")


@tool
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

# bind_tools передаёт модели описания инструментов — она может попросить их вызвать
llm = ChatOllama(model=MODEL, temperature=0.0, reasoning = True ).bind_tools(TOOLS)

# bind_tools(): -> Runnable


def llm_call(state: MessagesState):
    """LLM decides whether to call a tool or answer."""
    # Узел читает состояние и возвращает обновления; add_messages добавляет ответ в историю
    messages = state["messages"]
    result = llm.invoke(messages)
    return {"messages": [result]}


def should_continue(state: MessagesState):
    """Route to tools if the last message asks for a tool call."""
    # Условное ребро: по состоянию решает, в какой узел идти дальше
    return "tools" if state["messages"][-1].tool_calls else END



# %% Cell 10


# Собираем граф: узлы — это функции, рёбра — переходы
builder = StateGraph(MessagesState)

# добавление узлов
builder.add_node("llm", llm_call)
# "llm" -- задаёт имя узла в графе, оно может быть произвольным;
# llm_call -- функциональный объект, вызывающий LLM

# ToolNode выполняет все tool_calls из последнего сообщения (оба инструмента — в одном узле)
builder.add_node("tools", ToolNode(TOOLS))
builder.add_edge(START, "llm")
builder.add_conditional_edges("llm", should_continue, ["tools", END])
# Цикл: после инструментов управление возвращается модели
builder.add_edge("tools", "llm")

agent = builder.compile()       # -> CompiledStateGraph
agent

# %% Cell 20
Messages = [{'role': 'user', 'content': "Какая погода в Москве? И сколько будет 17 * 23?"}]
result = agent.invoke( { "messages": Messages } )
# Итоговое состояние хранит всю историю сообщений
for m in result["messages"]:
    m.pretty_print()
