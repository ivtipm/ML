"""
Скачивает все 'new' страницы из таблицы URL БД
Добавляет HTML код страницы в новую таблицу PAGES_HTML_TABLE
"""

from time import sleep
from turtle import delay
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
         ,content_hash TEXT
         ,download_dt TEXT )''')
        #hash - хеш содержимого страницы
        #content_hash - хеш содержимого страницы
        #download_dt - время скачивания страницы


    # Получаем все страницы со статусом "new"
    cursor = conn.execute("SELECT id, url FROM " + config.URL_TABLE + " WHERE state = 'new'")
    new_pages = cursor.fetchall()

    print(f"URLs in queue: {len(new_pages)}")
    print(f"Expected time to download all {config.DELAY * (len(new_pages)-1)} seconds")
    n = 0
    for page_id, url in new_pages:
        try:
            resp = httpx.get(url)
            if resp.status_code == 200:
                html_content = resp.text
                # Сохраняем HTML в другую таблицу
                content_hash = blake2s(html_content.encode('utf-8')).hexdigest()
                dt = datetime.now().isoformat()
                conn.execute("INSERT INTO " + config.PAGES_HTML_TABLE + " (id, content, url, content_hash, download_dt) VALUES (?, ?, ?, ?, ?)", (page_id, html_content, url, content_hash, dt))
                # Обновляем статус страницы на "Готово"
                conn.execute(f"UPDATE  {config.URL_TABLE}  SET state = '{config.UrlStates.DONE}' WHERE id = ?", (page_id,))
                conn.commit()
                n = n+1
                print(f"{url} [DONE]")
            elif resp.status_code in [404, 403]:
                conn.execute(f"UPDATE  {config.URL_TABLE}  SET state = '{resp.status_code}' WHERE id = ?", (page_id,))
                conn.commit()
                print(f"{url}. [FAIL] Status code: {resp.status_code}")
            else:
                print(f"{url}. [FAIL] Status code: {resp.status_code}")

        except KeyboardInterrupt as e:
            print(f"Downloaded: {n}")
        # todo: обработка отдельных видов исключений
        except Exception as e:
            print(f"Error downloading {url}: {e}")

        finally:
            sleep(config.DELAY)


# todo: логировать процесс работы
# todo: добавить параметры запуска: интервал, количество страниц, ...
#
