# Подготовка и классификация текста в Keras

```python
# X_doc -- Pandas Series с предварительно очищенными тектами;

from keras.preprocessing.text import Tokenizer

# объект для создания и преобразования токенов (в днном случае токен = слово)
t = Tokenizer()

# составление словаря, подсчёт частот слов, ....
t.fit_on_texts(X_doc.values)

print("Словарь", t.word_index)
# print("Слово - число документов, содержащих это слово",t.word_docs)
# print("Частоты слов", t.word_counts)
```
