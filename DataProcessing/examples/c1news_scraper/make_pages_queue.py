"""
Заполняет БД (SQLIte) адресами страниц из sitemap.xml
Эта БД будет использована потом для скачивания страниц
"""

import sqlite3
from os import path
from config import DATA_DIR, SQL_FILENAME, PAGES_URL_TABLE

SITEMAP_FILENAME = path.join(DATA_DIR, "sitemap.xml")

# открываем или создаём файл БД
with sqlite3.connect(path.join(DATA_DIR, SQL_FILENAME)) as conn:
    print (f"Создана БД {SQL_FILENAME}")
    # Создаем таблицу с для списка страниц
    conn.execute("CREATE TABLE IF NOT EXISTS " + PAGES_URL_TABLE + '''(
         id INTEGER PRIMARY KEY AUTOINCREMENT
        ,url TEXT NOT NULL UNIQUE
        ,type TEXT
        ,state TEXT
        ,note TEXT
    )''')
    conn.commit()

    print (f"Создана таблица {PAGES_URL_TABLE}")

    # Добавляем страницы из sitemap в БД
    with open(path.join(SITEMAP_FILENAME), "r") as f:
        for line in f:
            if "<loc>" in line:
                url = line.split("<loc>")[1].split("</loc>")[0].strip()
                try:
                    utl_state = "new"   # ещё не обработана
                    url_type = "item"   # отдельная статья, не страница со статьями (catalog)
                    conn.execute("INSERT INTO pages (url, type, state) VALUES (?, ?, ?)", (url, url_type, url_type))
                except sqlite3.IntegrityError:
                    print(f"URL {url} already exists in the database.")

# для проверки БД: подключиться из терминала и сразу выполнить запрос
# sqlite3 database.sqlite  "select count(*) from pages;"
