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
    browser = p.chromium.launch(headless=False,
        args=["--blink-settings=imagesEnabled=false"]       # не загружать картинки
    )
    page = browser.new_page()
    page.goto("https://www.chita.ru/", timeout=120_000)

    print(page.title())

    # клик на кнопку чтобы закрыть всплывающее окно "Подписка на уведомления"
    page.locator("#onesignal-slidedown-cancel-button").click()

    # клик на ссылку "Все новости"
    page.click('text=Все новости')  # ссылка выбирается по атрибуту id

    input("Press Enter to close...")

    browser.close()
