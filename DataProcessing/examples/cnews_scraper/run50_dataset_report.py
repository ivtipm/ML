# %% Cell 1

from os import path
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

import config

# %% Cell 2
with sqlite3.connect( path.join(config.DATA_DIR, config.SQL_FILENAME) ) as conn:
    # Создаем DataFrame из таблицы news
    df = pd.read_sql_query(f"SELECT * FROM {config.HTML_TABLE_NEWS}", conn)

    # Выводим статистику: количество записей
    print(f"Total number of records in the news table: {len(df)}")

    # Строим гистограмму по длинам текстов
    text_lengths = df['text'].apply(len)
    text_lengths.plot(kind='hist', bins=30, figsize=(12, 6))
    plt.grid(True)
    plt.title('Длины текстов в символах')
    plt.xlabel('Длина текста в символах')
    plt.ylabel('Количество текстов')
    plt.savefig(path.join( config.DATA_DIR, "hist.png") )
