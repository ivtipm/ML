"""
Пример запуска браузера в переходом на страницу;
Браузер закроется после того как пользователь в консоли, откуда запущена программа нажмёт Enter
"""

from playwright.sync_api import sync_playwright
# дополнительно потребуется установить компоненты (драйверы) для управления браузерами
# playwright install
# или только одним браузером
# playwright install chromium


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")

    print(page.title())

    input("Press Enter to close...")

    browser.close()
