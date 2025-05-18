# Классификация текстов

Решите задачу классификации текстов представленных с помощью TF-IDF.
1. Изучите и подготовьте тексты. Удалите лишние слова символы и обозначения, знаки пунктуации.
2. Подготовьте TF-IDF матрицу: определитесь с размером и составом словаря, критериями попадания слова в словарь, размером n-грамм и т. д.
3. В качестве моделей используете логистическую регрессию, метод опорных векторов или *модели на основе байесовского классификатора (дополнительно)* и другие методы. Подберите гиперпараметры.
4. Оцените модели на тестовой выборке. Сравните результаты.
5. Напишите выводы о проделанной работе и полученном  опыте.
4. *Бонус: Решите аналогичную задачу используя векторные представления слов.*
5. Решите задачу классификации используя векторные представления текстов. Используйте пакет sentence transformers


Используйте предложенные датасеты или датасет, который вы создали самостоятельно скачивая данные сайтов в задании по языкам программирования для больших данных (+1 балл).

## Датасеты
0. https://github.com/ivtipm/ML/blob/main/datasets/news.zip
1. Коллекция датасетов разного вида, в том числе текстовых:
    1. https://kaggle.com/datasets
    2. https://huggingface.co/datasets. Для поиска датасетов с размеченными классами выбрать тег “text classification”. Есть русскоязычные датасеты. 
2. Текстовые датасеты для классификации в коллекции pytorch (в основном модельные датасеты) 
https://pytorch.org/text/stable/datasets.html#text-classification 
3. Русскоязычные NLP датасеты (в основном диалоги и специальные задачи) https://github.com/Koziev/NLP_Datasets 
4. Ещё русскоязынче датасеты: https://github.com/natasha/corus   
5. https://github.com/ivtipm/ML/tree/main/datasets


## Ссылки
- Слайды: https://docs.google.com/presentation/d/1o1TN-hI9BhVakKm4xI_S9ZS-lGV68iBUt6h3cX-DWQg/edit#slide=id.p 
- Пример [анализ теста, подготовка текста для TF-IDF, Word2vec, SVM, классификация]:  https://colab.research.google.com/drive/1yOnvYUbbu7b2sgnh4vn1csis9PWAss_f
- Извлечение признаков (эмбеддингов) текста [feature extraction, BERT, sentence embedding]: https://colab.research.google.com/drive/1XDLKd42U5UcDSfwXtDgR3uJuFND9xCvS#scrollTo=671c40ae
- Шпаргалка по обработке и подготовке текстов: https://github.com/ivtipm/ML/blob/main/examples/text/text.md
- Короткая шпаргалка по использованию Sentence Embedding: https://miro.com/app/board/uXjVNQC1rq8=/?moveToWidget=3458764608088989698&cot=14
