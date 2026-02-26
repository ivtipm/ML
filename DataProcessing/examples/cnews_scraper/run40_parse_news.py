"""
Парсит HTML страницы (из БД) с новостями
Сохраняет в БД
"""

# %% Cell 1

from dataclasses import astuple, dataclass
from os import path
from bs4 import BeautifulSoup
import sqlite3
from tqdm import tqdm   # чтобы рисовать индикатор прогресса

import config


@dataclass
class NewsItem:
    """Новость"""
    id:int = 0
    url:str = ""
    title:str = ""
    text:str = ""
    date:str = ""
    author:str = ""
    themes:str = ""
    notes:str = ""


def parse_page(html_content:str, url:str, id:int) -> NewsItem | None:
    """Парсит одну страницу с новостью
    Возвращает: (заголовок, текст, заглушка_дата,заглушка_автор, заглушка_темы, заглушка_прим)"""
    # todo: обработка ошибок
    page_soup = BeautifulSoup(html_content, 'lxml')

    try:
        title = page_soup.title.getText(strip=True)
        # .getText(strip=True) - получить текстовое содержимое элемента DOM (тега), с обрезкой пробельных символов (strip)
        text_div = page_soup.select_one(".news_container")  # выборе элемента по CSS классу; этот элемент содержит параграфы (<p>) с текстом статьи

        # извлечение текста из параграфов, getText также обработает ссылки внутри p, отбросив адрес
        paragraphs_list = []
        for p in text_div.select("p"):
            paragraphs_list.append( p.getText(strip=True) )


        text = " ".join( paragraphs_list )
        # print(text)

        return NewsItem(id, url,title, text, "-", "-", "-", "-")
    except Exception as e:
        print(f"{id}: {url}. {e}")
        return None



# %% Cell 2
with sqlite3.connect( path.join(config.DATA_DIR, config.SQL_FILENAME) ) as conn:

    # если нет таблицы для содержимого, то создаём
    conn.execute(config.CREATE_NEWS_TABLE)

    cursor = conn.execute(f"SELECT id, url, content from {config.HTML_TABLE_PAGES}")
    pages = cursor.fetchall()

    print(f"Pages to process: {len(pages)}")

    for id, url,content in tqdm(pages):
        item = parse_page(content, url, id)
        # запрос с ? имеет защиту от SQL инъекций, строки экранируются и передаются в таблицу как байты
        if item:
            conn.execute(f"INSERT INTO {config.HTML_TABLE_NEWS}"\
                "(id,   url, title, text,   date, author, topics,   note) VALUES (?,  ?,?,?,  ?,?,?,  ? )"
                ,astuple(item)  )
        # astuple - делает кортеж из экземпляра dataclass
        # conn.commit()  тут не нужно каждый раз выполнять по одной операции, т.к. в отличии от скрапинга очень низкая вероятность завершиться с ошибкой (исключением)
        # print( astuple(item) )

        # todo: парсинг данных с веб страниц


# Часть новостей - рекламные. У них другая компоновка и парсер их не может обработать
# todo: разобраться с рекламными новостями
