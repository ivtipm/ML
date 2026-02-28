"""
Парсит HTML страницы (из БД) с новостями
Сохраняет в БД
"""

# %% Cell 1

import sqlite3
from dataclasses import astuple, dataclass
from os import path

import config
from config import TABLE_NEWS, TABLE_HTML_PAGES
from bs4 import BeautifulSoup
from tqdm import tqdm  # чтобы рисовать индикатор прогресса


# выбрать только новые скаченные страницы, из которых ещё не извлечены новости
SELECT_NEW_HTML_PAGES = """
select    t1.id, t1.url, t1.content
from      {table_html_pages} t1
left join {table_news} t2
on t1.id = t2.id
where t2.id is NULL
"""


@dataclass
class NewsItem:
    """Новость. В экземпляры этого класса нужно записывать новость после парсинга HTML страницы с текстом новости"""
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
        # todo: обработка рекламных статей, там другие элементы
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



def parse_all_news(html_pages:list[str]):
    """Парсит все html страницы (тексты страницы) из списка html_pages и записывает извлечённые данные в таблицу с новостями"""
    for id, url,content in tqdm(new_pages):
        item = parse_page(content, url, id)
        # запрос с ? имеет защиту от SQL инъекций, строки экранируются и передаются в таблицу как байты
        if item:
            conn.execute(f"INSERT INTO {config.TABLE_NEWS}"\
                "(id,   url, title, text,   date, author, topics,   note) VALUES (?,  ?,?,?,  ?,?,?,  ? )"
                ,astuple(item)  )
        # astuple - делает кортеж из экземпляра dataclass
        # conn.commit()  тут не нужно каждый раз выполнять по одной операции, т.к. в отличии от скрапинга очень низкая вероятность завершиться с ошибкой (исключением)
        # print( astuple(item) )


# %% Cell 2
with sqlite3.connect( path.join(config.DATA_DIR, config.SQL_FILENAME) ) as conn:
    # если нет таблицы для содержимого, то создаём
    conn.execute(config.CREATE_NEWS_TABLE)

    # cursor = conn.execute(f"SELECT id, url, content from {config.HTML_TABLE_PAGES}")
    cursor = conn.execute( SELECT_NEW_HTML_PAGES.format(table_news=TABLE_NEWS, table_html_pages = TABLE_HTML_PAGES))
    new_pages = cursor.fetchall()

    print(f"Pages to process: {len(new_pages)}")
    parse_all_news( new_pages )


# Часть новостей - рекламные. У них другая компоновка и парсер их не может обработать
#TODO разобраться с рекламными новостями
#TODO повторно не парсить уже добавленные в таблицу news новости
