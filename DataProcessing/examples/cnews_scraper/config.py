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
HTML_TABLE_PAGES = "pages"
"""Таблица для содержимого HTML файлов"""
HTML_TABLE_NEWS = "news"
"""Таблица для хранения данных, полученных после парсинга HTML файлов"""

CREATE_URLS_TABLE = "CREATE TABLE IF NOT EXISTS " + URL_TABLE + '''(
     id INTEGER PRIMARY KEY AUTOINCREMENT
    ,url TEXT NOT NULL UNIQUE
    ,type TEXT
    ,state TEXT
    ,note TEXT
)'''

CREATE_PAGES_TABLE = "CREATE TABLE IF NOT EXISTS " + HTML_TABLE_PAGES + '''(
      id INTEGER PRIMARY KEY AUTOINCREMENT
     ,content TEXT
     ,url TEXT
     ,content_hash TEXT
     ,download_dt TEXT )'''
     #content_hash - хеш содержимого страницы
     #download_dt - время когда страница была скачена


CREATE_NEWS_TABLE = "CREATE TABLE IF NOT EXISTS " + HTML_TABLE_NEWS + '''(
      id INTEGER PRIMARY KEY AUTOINCREMENT
     ,url TEXT
     ,title TEXT
     ,text TEXT
     ,date TEXT
     ,author TEXT
     ,topics TEXT
     ,note TEXT
)'''
     # text - полный текст новости
     # date - дата публикации
     # topics - темы/теги, можно хранить через запятую или в виде JSON

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
DELAY = 2
# см. robots.txt
