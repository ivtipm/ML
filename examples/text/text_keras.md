# Подготовка и классификация текста в Keras

### Подготовка текста для дальнейшей обработки моделью
```python
# X_doc -- Pandas Series с предварительно очищенными текстами;

from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence            # модуль для обработки последовательностей

# объект для создания и преобразования токенов (в данном случае токен = слово)
tokenizer = Tokenizer()

# составление словаря, подсчёт частот слов, ....
tokenizer.fit_on_texts(X_doc.values)

print("Словарь", tokenizer.word_index)
# print("Слово - число документов, содержащих это слово",t.word_docs)
# print("Частоты слов", t.word_counts)

# замена слов их номерами из словаря
# номера начинаются с 1
X_doc_indexes = tokenizer.texts_to_sequences(X_doc.values)

# дополнение\обрезка текста до указанного размера maxlen
X_doc_indexes = sequence.pad_sequences(X_doc_indexes, maxlen=maxlen,
                                       value=0,                     # значение для заполнения
                                       padding='pre')               # как заполнять: с начала
```

### Простая модель с LSTM нейроном для классификации текстов (2 класса)

```python
from keras.models import Sequential                 # для создания модели, соединения слоёв
from keras.layers import Dense, Embedding           # полносвязный слой, слой создания векторных представлений
from keras.layers import LSTM                       # рекуррентный слой

# размер словаря (словарь + нулевой заполняющий символ)
vocab_size = list(tokenizer.word_index.values())[-1] + 1

model = Sequential()
model.add( Embedding(vocab_size, emb_dim) )     # создаёт векторные представления;
                                                # vocab_size -- входная размерность (one-hot вектора),
                                                # hidden_dim -- выходная размерность (размерность вектора)

model.add( LSTM(hidden_dim,             # 128 -- размерность выхода
                dropout=0.2,            # отключать 0.2 размерности входа (препятствует переобучению)
                recurrent_dropout=0.2)) # отключать 0.2 размерности внутр. состояния

model.add( Dense(1, activation='sigmoid') )
```

#### Обучение
```python
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(x_train,                # x_train -- последовательности слов закодированных числами
          y_train,                # метки классов (0 или 1)
          batch_size=batch_size,
          epochs=3)

# лосс и метрика точности
score, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)
```
