"""
Заполняет БД (SQLIte) адресами страниц из sitemap.xml
Эта БД будет использована потом для скачивания страниц
"""

import sqlite3
from os import path
from config import DATA_DIR, SQL_FILENAME, URL_TABLE, UrlStates, UrlTypes

SITEMAP_FILENAME = path.join(DATA_DIR, "sitemap.xml")

# открываем или создаём файл БД
with sqlite3.connect(path.join(DATA_DIR, SQL_FILENAME)) as conn:
    print (f"Создана БД {SQL_FILENAME}")
    # Создаем таблицу с для списка страниц
    conn.execute("CREATE TABLE IF NOT EXISTS " + URL_TABLE + '''(
         id INTEGER PRIMARY KEY AUTOINCREMENT
        ,url TEXT NOT NULL UNIQUE
        ,type TEXT
        ,state TEXT
        ,note TEXT
    )''')
    conn.commit()

    print (f"Создана таблица {URL_TABLE}")

    dub_n = 0   # количество вставок дубликатов

    # Добавляем страницы из sitemap в БД
    with open(path.join(SITEMAP_FILENAME), "r") as f:
        for line in f:
            if "<loc>" in line:
                url = line.split("<loc>")[1].split("</loc>")[0].strip()
                try:
                    utl_state = UrlStates.TO_PROCESS   # ещё не обработана
                    url_type = UrlTypes.NEWS_ITEM   # отдельная статья, не страница со статьями (catalog)
                    conn.execute(f"INSERT INTO {URL_TABLE} (url, type, state) VALUES (?, ?, ?)", (url, url_type, utl_state))
                except sqlite3.IntegrityError:
                    print(f"URL {url} already exists in the database.")
                    dub_n += 1

    # общий итог по страницам
    total_urls = conn.execute(f"SELECT COUNT(*) FROM {URL_TABLE}").fetchone()[0]
    print (f"Total number of URLs in the database: {total_urls}")
    print(f"Number of attempts to insert duplicate URLs: {dub_n}")

    # итог по статусам
    url_states = conn.execute(f"SELECT state, COUNT(*) FROM {URL_TABLE} GROUP BY state").fetchall()
    print (f"URL states distribution:")
    for state in url_states:
        print(f"{state[0]}: {state[1]}")


# для проверки БД: подключиться из терминала и сразу выполнить запрос
# sqlite3 database.sqlite  "select count(*) from pages;"
