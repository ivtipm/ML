"""
Парсит HTML страницы (из БД) с новостями
Сохраняет в БД
"""

%pwd

import httpx

from os import path
from bs4 import BeautifulSoup
import sqlite3

import config

with sqlite3.connect( path.join(config.DATA_DIR, config.SQL_FILENAME) ) as conn:
    # todo: create news table

    cursor = conn.execute(f"SELECT id, url, content from {config.PAGES_HTML_TABLE}")

    pages = cursor.fetchall()

    print(f"Pages to process: {len(pages)}")

    for id, url,content in pages:

        page_soup = BeautifulSoup(content, 'html5lib')

        print(f"page title {id} {url}")
        print(page_soup.title)
        # todo:
