# %% Cell 0

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from tqdm import tqdm

import ollama
from pydantic import BaseModel

data = pd.read_csv('../datasets/IMDB Dataset.csv').sample(100, random_state=0)
data['y'] = data['sentiment'].map({'positive': 1, 'negative': 0})

print(f"{len(data)=}")


MODEL = 'qwen3.5:0.8b'

class ClassLabel(BaseModel):
    label: int
schema = ClassLabel.model_json_schema()

system_prompt = 'Определи к какой категории относится данный текст. Категории на выбор: негативный (класс 0), позитивный (класс 1); Ответ дай в виде JSON, для обозначения класса используй 0 или 1 '

data




# %% Cell 5
# проверка
r = ollama.generate(model=MODEL, system=system_prompt, prompt="Ping!", think=False, format=schema)
label = ClassLabel.model_validate_json(r.response)
label.label

# %% Cell 10
y_pred = np.zeros_like( data['y'] )

for i, text in tqdm(enumerate( data['review'] )):
    r = ollama.generate(model=MODEL, system=system_prompt, prompt=text, think=False, format=schema)
    label = ClassLabel.model_validate_json(r.response)
    y_pred[i] = label.label
# TODO: асинхронные запросы

print(classification_report(data['y'], y_pred))
# %% Cell 20

print(classification_report(data['y'], y_pred))
