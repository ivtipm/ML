from bs4 import BeautifulSoup, ResultSet

url = 'example.html'

# загрузим содержимое HTML файлы
with open(url, "r", encoding="utf-8") as f:
    html = f.read()

soup_example = BeautifulSoup(html, 'html.parser')

print(f"Заголовок страницы {soup_example.title}")

# 1. Запрос по тегу: выбрать все sections
divs: ResultSet = soup_example.select('section')

print(f"selected sections: {len(divs)}")
print(f"first section: {divs[0].text}")
# 1. Запрос по тегу: выбрать все div
divs = soup_example.select('div')
print(f"selected divs: {len(divs)}")




# 2. Выбор по атрибутам
