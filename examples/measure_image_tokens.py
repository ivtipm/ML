import ollama
from ollama import chat

# выведем список доступных LLM

response = ollama.list()
Models = [model.model for model in response.models]
# print(Models)
for model in ollama.list().models:
    name = model.model
    info = ollama.show(name)

    if "vision" in (info.capabilities or []):
        print(name)
print()

model = "qwen3.5:2b-q8_0"  # нужна модель Ollama с поддержкой vision

def run(images=None):
    response = chat(
        model=model,
        messages=[{
            "role": "user", "content": "Кратко опиши изображение.",
            **({"images": images} if images else {}), }],
        options={"num_predict": 40},
    )
    return {
        "prompt_eval_count": response.prompt_eval_count,
        "prompt_eval_duration": response.prompt_eval_duration,
        "eval_count": response.eval_count,
    }

img_filename = "../NLP/prompt_enginering/grumpy_cat.jpg"
print("Только текст:", run())
print("С картинкой:", run([ img_filename ]))
