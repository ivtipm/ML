BERTopic - это фреимворк, реализующий технику моделирования тем, которая использует трансформеры (для более глубокого понимания текста) и c-TF-IDF вместе с алгоритмом кластеризации HDBSCAN для создания плотных кластеров, позволяющих легко интерпретировать темы, сохраняя при этом важные слова в описаниях тем.

**Альтернативы**
1. LDA (Latent Dirichlet Allocation) - классический статистический метод
2. Top2Vec - использует векторные представления документов
3. CTM (Contextualized Topic Models) - комбинирует нейронные сети и вероятностные модели
4. Neural Topic Models
5. ...


**Плюсы**:**
- Лучше понимает семантику и контекст текста
- Языковая независимость благодаря предобученным моделям BERT
- Более устойчив к шуму в данных
- Автоматически определяет количество тем, можно задавать начальные темы
- Встроенная возхможность визуализации кластеров из тем

**Минусы**:
- Вычислительно затратный, требует значительных ресурсов
- Может быть сложен в настройке для оптимальной производительности

**Структура модели**
1. Модель эмбеддингов на основе трансформеров (энкодер - вариант BERT)
2. Уменьшение размерности с помощью UMAP
3. Кластеризация с использованием HDBSCAN (иерархическая кластеризация, на основе DBSCAN, без начального задания числа кластеров)
4. Маркировка кластеров с помощью c-TF-IDF (с в название означает, что метод адаптирован для классов\кластеров )

Все компоненты фреимворка настраиваются.


**Принцип работы**
1. Документы преобразуются в векторные представления с помощью модели BERT
2. UMAP сжимает высокоразмерные векторы до 2-3 измерений
3. HDBSCAN кластеризует сжатые векторы
4. c-TF-IDF используется для выделения ключевых слов, характеризующих каждый кластер

**Важные гиперпараметры**
- **n_neighbors** и **n_components** в UMAP: влияют на сжатие векторов
- **min_cluster_size** и **min_samples** в HDBSCAN: определяют размер и плотность кластеров
- **language** в BERTopic: выбор языковой модели (задаёт список стоп-слов, но это можно и отдельно сделать)
- **calculate_probabilities**: включение расчета вероятностей принадлежности к темам

## Пример
```py
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer

# Данные
docs = [
    "Текст документа 1",
    "Текст документа 2",
    "Текст документа 3"
]

# Использование своей модели для эмбеддингов
sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
# можно использовать уже предвариетльно созданные вектора, они передаётся в fit_transform

# если необходимо, задать ключевые слова, составляющие темы в качестве затравки для выявления тем
seed_topic_list = [
    ["слово1", "слово2"],
    ["слово11", "слово22", "слово33"]
]

# Создание модели BERTopic
topic_model = BERTopic(language="russian", seed_topic_list=seed_topic_list, embedd)
# Обучение модели; получени метод для тем
topics, probs = topic_model.fit_transform(docs)
# topics, probs = topic_model.fit_transform(docs, groups_ed_emb)        # если уже есть векторные представления документов

topics, probabilities = topic_model.fit_transform(docs)


# Вывод тем и их меток (DataFrame)
print(topic_model.get_topic_info())
```


**Стоп слова**
```py
STOPWORDS_RUSSIAN = []
count_model=CountVectorizer(ngram_range=(1, 2), stop_words=STOPWORDS_RUSSIAN)
topic_model_ts = BERTopic(language="russian", vectorizer_model=count_model )
```

### Сохранение и загрузка

Модели UMAP, Count Vectorizer и HDBSCAN не воспроизводимы, если для каждой их них не задан инициализатор для генератора случайных чисел.

Поэтому для воспроизводимости модель нужно сохранять:
```py
# в этом примере используется отдельная модель эмбеддингов, как и список эмбеддингов текстов
topic_model.fit( texts, texts_embeddings)

# сохранение в папку, сохранится в том числе список тем
topic_model.save("folder_name", serialization="safetensors", save_ctfidf=True, save_embedding_model=False)

# загрузка
topic_model = BERTopic.load("folder_name")
```

 ### Визуализации
**Диаграмма рассеяния для тем (topics)**
..

**Диаграмма рассеяния для документов (nтекстов)**
```py
topic_model.visualize_documents(docs, embeddings=embeddings)
```
Диаграмма строится на освное пакета plotly.

https://maartengr.github.io/BERTopic/getting_started/visualization/visualize_documents.html

# Ссылки
- https://maartengr.github.io/BERTopic/index.html 