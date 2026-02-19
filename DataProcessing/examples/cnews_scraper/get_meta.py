"""
Получает robots.txt и карту сайта
"""
import requests
from lxml import etree  # для парсинга XML файла с картой сайта  # pyright: ignore[reportAttributeAccessIssue]
from os import path

from config import DATA_DIR, SITE_URL


def print_sitemap_info(sitemap_filename:str):
    """
    Выводит информацию о сайте из карты сайта: количество ссылок, самая поздняя и самая ранняя правка страницы и т.п. Использует пакет xlml
    """
    tree = etree.parse(sitemap_filename)
    root = tree.getroot()

    nsmap = { 'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9' }

    print(f"==={sitemap_filename}")
    # страницы
    locs = root.findall('.//sm:url/sm:loc', namespaces=nsmap)
    print(f"Number of links: {len(locs)}")

    print(locs[0].text)
    # todo:  самая первая и последняя дата изменения



# 1. получить и скачать robots.txt
RobotsURL = SITE_URL + "robots.txt"
robots_filename = path.join(DATA_DIR, "robots.txt")
response = requests.get(RobotsURL)
# проверка

if response.status_code != 200:
    print(f"Failed to download robots.txt. Status code: {response.status_code}")
else:
    # сохранить в файл
    with open(robots_filename, "w") as f:
        f.write(response.text)
    print("robots.txt downloaded successfully")


# 2. Получить адрес карты сайта из robots.txt
robots_content = response.text
SitemapURLs = []
for line in robots_content.splitlines():
    if "Sitemap:" in line:
        url = line.split("Sitemap:")[1].strip()
        SitemapURLs.append ( url )
        print(f"Sitemap URL: {url}")
        break


# 3. Скачать карту сайта
SitemapFilenames = []
for sitemap_url in SitemapURLs:
    response = requests.get(sitemap_url)
    tmp = sitemap_url.split("/")
    sitemap_filename = path.join(DATA_DIR, tmp[-1])
    SitemapFilenames.append ( sitemap_filename )
    if response.status_code == 200:
        with open(sitemap_filename, "wb") as f:
            f.write(response.content)
        print(f"{sitemap_filename} downloaded successfully")
    else:
        print(f"Failed to download {sitemap_filename}. Status code: {response.status_code}")



sitemap_filename = "data/sitemap.xml"
# 4. информация о сайте из карты
for sitemap_filename in SitemapFilenames:
    print_sitemap_info(sitemap_filename)
