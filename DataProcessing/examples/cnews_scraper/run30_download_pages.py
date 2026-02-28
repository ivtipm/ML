"""
Скачивает все 'new' страницы из таблицы URL БД
Добавляет HTML код страницы в новую таблицу PAGES_HTML_TABLE
"""

from time import sleep
import sqlite3
from os import path
import httpx
from hashlib import blake2s
from datetime import datetime

import config


PRINT_STATE_I = 50     # выводить статистику каждые ... итераций


def print_stat(n_done, n_error, n_to_process):
    """Выводит статистику по обработанным страницам"""
    print(f"Downloaded: {n_done}; {n_done/n_to_process*100:.0f}%")
    print(f"With error: {n_error}; {n_error/n_to_process*100:.0f}%")
    print(f"Total processed {(n_done+n_error)/n_to_process*100:.0f}%")



def upd_and_insert_page(page_id:int, url:str, page_content:str, con: sqlite3.Connection):
    """Обновляет таблицы в БД после скачивания страницы"""
    content_hash = blake2s(page_content.encode('utf-8')).hexdigest()
    dt = datetime.now().isoformat()
    con.execute(f"INSERT INTO {config.TABLE_HTML_PAGES} (id, content, url, content_hash, download_dt) VALUES (?, ?, ?, ?, ?)", (page_id, page_content, url, content_hash, dt))
    # Обновляем статус страницы на "Готово"
    con.execute(f"UPDATE  {config.URL_TABLE}  SET state = ? WHERE id = ?", (config.UrlStates.DONE, page_id,))
    con.commit()


def main():
    # открываем БД
    with sqlite3.connect(path.join(config.DATA_DIR, config.SQL_FILENAME)) as conn:

        # если нет таблицы для содержимого, то создаём
        conn.execute(config.CREATE_PAGES_TABLE)


        # Получаем все страницы со статусом "new"
        cursor = conn.execute(f"SELECT id, url FROM {config.URL_TABLE} WHERE state = ?", (config.UrlStates.TO_PROCESS,))
        n_to_process = cursor.fetchall()

        print(f"URLs in queue: {len(n_to_process)}")
        print(f"Expected time to download all {config.DELAY * (len(n_to_process)-1)} seconds")
        n_done = 0   # количество скаченных
        n_error = 0

        for i, (page_id, url) in enumerate(n_to_process):
            try:
                resp = httpx.get(url)
                if resp.status_code == 200:
                    html_content = resp.text
                    # Сохраняем HTML в другую таблицу
                    upd_and_insert_page(page_id, url, html_content, conn)
                    n_done = n_done+1
                    print(f"{url} [DONE]")
                elif resp.status_code in [404, 403]:
                    conn.execute(f"UPDATE  {config.URL_TABLE}  SET state = '{resp.status_code}' WHERE id = ?", (page_id,))
                    conn.commit()
                    print(f"{url}. [FAIL] Status code: {resp.status_code}")
                    n_error += 1
                else:
                    print(f"{url}. [FAIL] Status code: {resp.status_code}")
                    n_error += 1

            except KeyboardInterrupt:
                print_stat(n_done, n_error, len(n_to_process))
                break

            except Exception as e:
                print(f"Error downloading {url}: {e}")
            finally:
                sleep(config.DELAY)
                if i != 0 and i % PRINT_STATE_I == 0:
                    print_stat(n_done, n_error, len(n_to_process))


if __name__ == "__main__":
    main()

# TODO: логировать процесс работы
# TODO: добавить параметры запуска: интервал, количество страниц, ...
# TODO: печатать статистику по ходу скачивания: успешно, не успешно (с различными ошибками)
