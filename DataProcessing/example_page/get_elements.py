from bs4 import BeautifulSoup, ResultSet

url = 'example.html'

# загрузим содержимое HTML файлы
with open(url, "r", encoding="utf-8") as f:
    html = f.read()

# soup_example - экземпляр распашеной страницы
soup_example = BeautifulSoup(html, 'html.parser')

print(f"Заголовок страницы {soup_example.title}")
# см. также другие поля классов, представляющих страницу и элементы DOM

# 1. Запрос по тегу: выбрать все sections
sections: ResultSet = soup_example.find_all('section')

print(f"selected sections: {len(sections)}")
print(f"first section: {sections[0].text}")
# 1. Запрос по тегу: выбрать все элементы с тегом span
spans = soup_example.select('span')
print(f"selected spans: {len(spans)}")




# 2. Выбор по атрибутам
spans_price = soup_example.find_all('span', class_ = 'price')
print(f"selected divs: {len(spans_price)}")


# 3. Выбор по иерархии
items = soup_example.find("section", class_="products").find_all("li", class_="item")
print(f"selected items: {len(items)}")
print(f"first item: {items[0].text}")



# 4. Выборе по CSS селектору: выбрать все li c CSS классом item,
# которые находятся внутри ul c CSS классом items
# Шпаргалка: https://htmlacademy.ru/blog/css/selectors
items =  soup_example.select("ul.items > li.item")
print(f"selected items: {len(items)}")
print(f"first item: {items[0].text}")



# 5.
