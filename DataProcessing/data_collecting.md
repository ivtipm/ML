# Источники данных

# Требования к датасету
полнота, репрезентативность, метки, метаданные.

[Kaggle, Common Crawl, COCO](https://github.com/ivtipm/ML/tree/main/datasets
https://huggingface.co/datasets
https://www.kaggle.com/datasets
https://pytorch.org/text/stable/datasets.html#text-classification — текстовые дастасеты pytorch
UC Irvine Machine Learning Repository — большая коллекция датасетов
https://commoncrawl.org/overview - текстовые датасеты собранные со всего интернета, терабайты данных
Дополнительно
Портал открытых данных РФ http://data.gov.ru/
Пакеты открытых данных https://hubofdata.ru/datase)


# Сбор через HTTP / REST API

Протоколы, методы HTTP, коды состояния, аутентификация (API keys, OAuth).

Библиотеки: httpx (включая async), requests (для синхронных задач), работа с JSON. Рекомендация: httpx — современный клиент с async и HTTP/2 поддержкой.

Политика использования API: rate limits, backoff, retry, pagination


## Веб-скрейпинг: статические страницы
Парсинг HTML: BeautifulSoup, lxml, CSS/XPath селекторы.
Этикет и правила (robots.txt, ai.txt, условия использования), соблюдение rate limit; правовые риски — обзор EU/EDPB-рекомендаций по обработке персональных данных и последние замечания регуляторов (важно для использования данных в ML).


## Веб-скрейпинг: динамические сайты и браузерная автоматизация

Причины использовать браузерную автоматизацию (JS-рендеринг, SPA): когда простой HTTP-запрос не помогает.

Инструменты: Playwright (рекомендую для современных задач, headless, поддержка async), Selenium (старше — всё ещё используется).

Практика: защита от ботов, CAPTCHAs, легальные и технические ограничения.


## Крупномасштабный краулинг и фреймворки

Архитектура краулера: очереди URL, дедупликация, politeness, распределённость.

Инструменты: Scrapy (фреймворк для робастного краулинга), интеграция с async инструментами.

Хранение промежуточных результатов (message queues, Redis).


## Хранение, форматы и качество данных
Форматы: CSV, JSON, Parquet, TFRecord — когда что удобно (Parquet для столбцовых операций и больших объёмов).

Метаданные: schema, provenance, timestamp, source URL.

Валидация качества: контроль пропусков, типы, аномалии; инструменты для валидации (например, Great Expectations — опционально).


## Управление версиями датасетов и пайплайны данных

Почему versioning важен (репродуцируемость, откат): инструменты DVC / lakeFS для версионирования больших наборов данных.

Оркестрация и автоматизация: Airflow, Prefect (управление ETL/ELT).

Ингест и интеграция: Airbyte / custom connectors (кратко).



## Разметка / аннотация данных, этика, лицензии

Инструменты разметки: Label Studio (open-source) — поддержка изображений, текста, аудио; рабочие процессы аннотации, multi-user.

Практики: guidelines для аннотаторов, контроль качества разметки, меж-аннотатное согласие.

Этические вопросы: приватность, лицензии, права на изображения/текст, использование персональных данных для обучения моделей (GDPR/локальные правила)


## Короткий список библиотек и инструментов

HTTP / async: httpx, requests (для простых задач).

HTML parsing: BeautifulSoup, lxml.

Browser automation: playwright, selenium.

Crawling framework: Scrapy.

Data versioning: DVC, lakeFS.

Labeling: Label Studio.

Storage/formats: CSV, JSON, Parquet, TFRecord.

Validation: Great Expectations (или самописные проверки).
