"""
Скачивает все new страницы из БД
Добавляет HTML код страницы в новую таблицу
"""

from time import sleep
import config
import sqlite3
from os import path
import httpx

from hashlib import blake2s

from datetime import datetime


# открываем БД
with sqlite3.connect(path.join(config.DATA_DIR, config.SQL_FILENAME)) as conn:

    # если нет таблицы для содержимого, то создаём
    conn.execute("CREATE TABLE IF NOT EXISTS " + config.PAGES_HTML_TABLE + '''(
          id INTEGER PRIMARY KEY AUTOINCREMENT
         ,content TEXT
         ,url TEXT
         ,hash TEXT
         ,datetime TEXT )''')
        #hash - хеш содержимого страницы
        #datetime - время скачивания страницы


    # Получаем все страницы со статусом "new"
    cursor = conn.execute("SELECT id, url FROM " + config.PAGES_URL_TABLE + " WHERE state = 'new'")
    new_pages = cursor.fetchall()

    for page_id, url in new_pages:
        try:
            response = httpx.get(url)
            if response.status_code == 200:
                html_content = response.text
                # Сохраняем HTML в другую таблицу
                hash = blake2s(html_content.encode('utf-8')).hexdigest()
                dt = datetime.now().isoformat()
                conn.execute("INSERT INTO " + config.PAGES_HTML_TABLE + " (id, content, url, hash, datetime) VALUES (?, ?, ?, ?, ?)", (page_id, html_content, url, hash, dt))
                # Обновляем статус страницы на "downloaded"
                conn.execute("UPDATE " + config.PAGES_URL_TABLE + " SET state = 'downloaded' WHERE id = ?", (page_id,))
                conn.commit()
                print(f"Page {url} downloaded and saved successfully.")
            else:
                print(f"Failed to download {url}. Status code: {response.status_code}")
            sleep(config.DELAY)

        # todo: обработка отдельных видов исключений
        except Exception as e:
            print(f"Error downloading {url}: {e}")
            sleep(config.DELAY)
