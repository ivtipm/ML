"""
Важные параметры работы скрапера
"""

from enum import Enum

SITE_URL = "https://www.cnews.ru/"

DATA_DIR = "data"
"""папка для сохранения всех данных"""


SQL_FILENAME = "database.sqlite"
"""Файл БД для хранения скаченных данных"""

# Таблицы из БД
URL_TABLE = "Url"
"""Таблица для хранения списка обработанных и ещё не обработанных URL """
PAGES_HTML_TABLE = "pages_content"
"""Таблица для содержимого HTML файлов"""
PAGES_HTML_TABLE = "news"
"""Таблица для хранения данных, полученных после парсинга HTML файлов"""

CREATE_URLS_TABLE = "CREATE TABLE IF NOT EXISTS " + URL_TABLE + '''(
     id INTEGER PRIMARY KEY AUTOINCREMENT
    ,url TEXT NOT NULL UNIQUE
    ,type TEXT
    ,state TEXT
    ,note TEXT
)'''

CREATE_PAGES_TABLE = "CREATE TABLE IF NOT EXISTS " + PAGES_HTML_TABLE + '''(
      id INTEGER PRIMARY KEY AUTOINCREMENT
     ,content TEXT
     ,url TEXT
     ,content_hash TEXT
     ,download_dt TEXT )'''
     #content_hash - хеш содержимого страницы
     #download_dt - время когда страница была скачена


class UrlStates(str, Enum):
    """перечисление для состояний обработки страниц (url)"""
    TO_PROCESS = "new"
    """Новый URL, добавлен но не обработан"""
    DONE = "done"
    """URL обработан - скачена страница"""
    # todo: другие состояния: ошибка при получении страницы, ...


class UrlTypes(str, Enum):
    """Перечисление для типов URL (связанных с ним HTML страниц)"""
    NEWS_ITEM = "item"
    """Это отдельная страница с новостью"""
    NEWS_CATALOG = "catalog"
    """станица с перечнем новостей (ссылками на полные тексты новостей)"""

# задержка в секундах между скачиванием отдельных страниц
DELAY = 3
# см. robots.txt
