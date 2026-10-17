"""
На сколько LLM способна справляться с задачей генерации случайных чисел?
"""

# %% Cell 01
import ollama

import seaborn
import matplotlib.pyplot as plt
from tqdm import tqdm


MODEL = "qwen3.5:0.8b"
PROMPT = "generate random number from 1 to 10 inclusive. Answer with only a number."

N = 1000

Messages = [ {'role':'user', 'content':PROMPT}]
Numbers = {}
NumbersOther = []
Errors_n = 0
client = ollama.Client(host='http://192.168.1.8:11434')
# client = ollama.Client(host='http://127.0.0.1:11434')



# %% Cell 10
for t in [0.5, 1.0, 1.5, 2.0]:
    print(f"=== t = {t:4.2f} ===")
    Numbers[t] = []
    i = 0
    with tqdm(total=N//50) as pbar:
        while i < N:
            r = client.chat(model=MODEL, messages=Messages, options={'temperature': t}, think=False )
            try:
                x = int(r.message.content);
                if 1 <= x <= 10:
                    Numbers[t].append(x)
                    # print(x, end = " " if i%50 != 0 else "\n");
                    i = i + 1;
                    if i%50 == 0: pbar.update(1)
                else: NumbersOther.append(x)
            except Exception as e: Errors_n += 1

    seaborn.histplot(Numbers[t], bins=10, discrete=True); plt.savefig("random_numbers_t{t}.png");
    plt.show();
    print(f"\nt = {t}\nmean = {sum(Numbers[t])/N}\n\n")


# %% Cell 20
import pandas as pd

df = pd.DataFrame(Numbers)
df.to_csv("random_numbers.txt")
print(df)

seaborn.histplot(NumbersOther); plt.show()
