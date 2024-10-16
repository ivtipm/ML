```bash
pip install langchain
```

```python
import langchain_community
```

## Основные концепции

- Chains: Цепочки выполняют последовательные задачи, комбинируя несколько вызовов LLM и обработки данных. Класс `LLMChanin`
- Agents: Агенты принимают решения о том, какие действия предпринимать на основе пользовательских запросов.
- Memory: Механизм хранения данных между запросами, который полезен для создания диалогов.
- Промпт: Позволяет создавать и настраивать объекты для промптов. Класс `PromptTemplate`.

### Адаптеры для LLM

**OpenAI**
```py
from langchain.llms import OpenAI

# создание и настройка адаптера
llm = OpenAI(temperature=0.9)
# обращение к LLM
response = llm("What is the capital of France?")
```

**Для моделей с HuggingFace**
```py
from langchain.llms import HuggingFaceHub
llm = HuggingFaceHub(repo_id="facebook/llama", model_kwargs={"temperature": 0.7})
```


**OLLAMA**
```bash
pip install -U langchain-ollama
```

```py
from langchain_ollama import OllamaLLM                  # для одиночных запросов

ollama = OllamaLLM(
    base_url="http://your-server-address:11434",
    model="llama3,2:1b",
    # параметры со значениями по умолчанию
    temperature=0.7,
    num_ctx=4096,
    num_gpu=1,
    num_thread=4
)

resp = ollama.invoke("What is lama? Give me a short answer")


from langchain_ollama.chat_models import ChatOllama         # для чатов (с запоминанием контекста из чата и т.п.)
ollama_chat = ChatOllama(
    base_url="http://your-server-address:11434",
    model="llama3.2:1b"
)
resp = ollama_chat.invoke("What is lama? Give me a short answer")
print(resp.content)
```

**YandexGPT**
```py
from langchain_community.llms import YandexGPT

yandex_gpt = YandexGPT(
    
    iam_token="your_iam_token",     # использовать одно из двух 
    api_key="your_api_key",         # использовать одно из двух

    folder_id="your_folder_id"
)
```


### PromptTemplate

Простые запросы к LLM можно писать непосредственно, но для более сложных, например с контекстом и system prompt можно использовать PromptTemplate.  

```py
from langchain_core.prompts import PromptTemplate

# создание простого промпта
# todo: ...

# структура промпта
template = """
System: {system_message}
Human: {user_message}
Context: {context}
AI: Please respond to the human's message.
"""

# Последний раздел (AI) можно использовать по необходимости, когда запрос может быть не вполне очевиден или требует дополнительных уточнений.

prompt = PromptTemplate(
    template=template,
    input_variables=["system_message", "user_message", "context"]           # названия переменных из текста template
)

formatted_prompt = prompt.format(
    system_message="You are a helpful AI assistant.",
    user_message="What's the capital of France?",
    context="France is a country in Western Europe."
)
```

## Цепочки LLMChain

Самый частый сценарий использования цепочки - настройки промпта и обращения к LLM.


```py


```