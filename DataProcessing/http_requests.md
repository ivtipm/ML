# Библиотеки
### для HTTP‑запросов
- `requests`. Простой. Есть поддержка сессий, cookies, headers, прокси.
- `httpx`. Асинхронный. Поддержка HTTP2. Подходит для высоконагруженных скраперов.
- `aiohttp`. Во многом похож на httpx.
- `urllib3`. Низкоуровневый.
- 
### HTML‑парсеры и извлечение данных
- `BeautifulSoup` (bs4). Высокоуровневый HTML/XML‑парсер, удобный API (find, select), устойчив к "грязному" HTML.
- `html5lib`
- `lxml`. Высокопроизводительный парсер HTML/XML с поддержкой XPath и CSS‑селекторов (через cssselect).
- `parsel` -- обёртка над lxml
- `selectolax`. Очень быстрый
- `Requests‑HTML`. Объединяет HTTP‑запросы и парсинг HTML (CSS/XPath), умеет при необходимости рендерить JS
- `MechanicalSoup`
Обёртка вокруг requests + BeautifulSoup с интерфейсом, похожим на «браузер» (формы, навигация по ссылкам)

### Фреймворки для краулинга
- `Scrapy`. Полноценный фреймворк для краулинга: spiders, очереди, pipelines, middlewares, throttling, экспорт данных.
- `feedparser`. Парсер RSS/Atom‑лент, удобен для сбора структурированных новостных данных.

### Для получения динамического контента
- `Requests`‑HTML (как «комбайн»)
- `Selenium`
- `Playwright`

### Разное
- `w3lib`. Набор вспомогательных функций для работы с URL, HTML и текстом (нормализация, очистка); часто используется вместе со Scrapy.
- `pyquery`. jQuery‑подобный интерфейс к HTML на базе lxml, позволяет использовать знакомый синтаксис селекторов.



## Категории ответов HTTP

HTTP-ответы классифицируются по первой цифре кода (status code) на 5 категорий


| Категория | Коды | Значение |
|-----------|------|----------|
| 1xx (Informational) | 100–199 | Информационные: запрос принят, обработка продолжается (e.g. 100 Continue).  [firstvds](https://firstvds.ru/technology/chto-takoe-kod-otveta-ot-servera) |
| 2xx (Success) | 200–299 | Успех: запрос выполнен (e.g. 200 OK — ресурс получен).  [hostkey](https://hostkey.ru/blog/89-spisok-vsekh-kodov-sostoyaniya-http-otveta-servera/) |
| 3xx (Redirection) | 300–399 | Перенаправление: клиент должен перейти по новому адресу (e.g. 301 Moved Permanently).  [mixtelecom](https://mixtelecom.ru/blog/kody-otvetov-i-oshibki-servera) |
| 4xx (Client Error) | 400–499 | Ошибка клиента: неверный запрос.  [rush-analytics](https://www.rush-analytics.ru/blog/kody-otvetov-servera-kody-oshibok-http) |
| 5xx (Server Error) | 500–599 | Ошибка сервера: проблема на стороне сайта.  [firstvds](https://firstvds.ru/technology/chto-takoe-kod-otveta-ot-servera) |


## Типичные ошибки при скрейпинге


| Код | Значение | Вероятная причина  | Решение |
|-----|----------|-----------------------|---------|
| 403 Forbidden | Доступ запрещён | Бот детектирован (User-Agent, IP, fingerprinting). | Ротация прокси (proxy rotation), подмена User-Agent/headers, stealth-библиотеки (undetected-chromedriver). |
| 429 Too Many Requests | Превышен лимит запросов | Rate limiting, слишком частые запросы. | Задержки (sleep 1–10 с), exponential backoff, мониторинг X-RateLimit headers. |
| 404 Not Found | Страница не найдена | Неверный URL, удалён контент, динамические пути. | Валидация URL, обработка редиректов (301/302), парсинг sitemap.xml. |
| 500 Internal Server Error | Внутренняя ошибка сервера | Перегрузка от скрейпера, сбой сайта. | Retry с backoff, исключить URL из очереди, логировать. |
| 503 Service Unavailable | Сервис недоступен | Временная перегрузка, maintenance. | Retry после паузы (5–30 мин), ротация IP. |
| 401 Unauthorized | Не авторизован | Требуется логин/cookies. | Сессии с cookies, API-токены, симуляция авторизации. |
| 400 Bad Request | Неверный запрос | Некорректные headers/query params, CSRF-токен отсутствует. | Корректные headers (Referer, Origin), извлечение CSRF из HTML. |
| 502 Bad Gateway | Ошибка шлюза | Проблемы с upstream-серверами (CDN). | Retry, смена endpoint/IP. |
| 504 Gateway Timeout | Таймаут шлюза | Медленный backend, CDN. | Увеличить timeout, headless-браузер для JS. |
| 418 I'm a teapot | Шуточный отказ | Защита от ботов (RFC 7168). | Обход как 403: прокси, headers. |
