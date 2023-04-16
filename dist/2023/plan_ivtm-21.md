# Интеллектуальные системы
## Занятие 1. Повторение. Свёрточные нейросети
8 апреля
- Повторение
  - Многослойный персептрон. Функция активации. Функция потерь. Обучение.
  - https://docs.google.com/presentation/d/1YCJhQIj2BV42sDLKtxmytcYW5W39EJceYfqrYT7bKNo/edit?usp=sharing
  - https://colab.research.google.com/drive/1YtK4an7UAhnxTmhmQzZd6Eo3esfv6TL3#scrollTo=aWdUxy4n62Ii
  - Батчи. Отслеживание обучения. Валидационная выборка. Переобучение. Подбор гиперпараметров.
- CNN
  - слайды: https://docs.google.com/presentation/d/1i41kqGwZqW_sSRz9Bopoq7AZf_Zuo6OaRSeCKYIH_80/edit#slide=id.g175db6f31f84d48d_0
  - пример: https://colab.research.google.com/drive/1kqSiP9IpPmW8dw9NxV5Sm5pMLMqfINZb

#### Задание. CNN
Решите задачу классификации изображений на популярном наборе данных:
**CIFAR10 dataset**
- 60,000 изображений,
- 10 классов объектов
- изображения предварительно обработаны:
    - размер приведён к 32х32 пикселя
- дастасет разделён на 2 части:
    - для обучения нейросети (train) - 50 000 картинок
    - для оценки работы нейросети (test) - 10 0000 картинок

Скачать данные можно с помощью библиотеки Keras
```python
from tensorflow.keras import datasets
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
```

# Занятие 2. Представление текста. Рекуррентные нейронные сети
16 апреля
- Повторение
- Обработка и представление текста. TF-IDF
  - https://github.com/ivtipm/ML/blob/main/examples/text/text_preprocess.md
  - https://github.com/ivtipm/ML/blob/main/examples/text/text_keras.md
- RNN. LSTM. GRU.
  - https://colab.research.google.com/drive/1XXQgLdECny8MvO8VVcEn3-cM1TW8pdHK#scrollTo=HfPTJMS7BTey
- Представление текста. RNN. LSTM. https://colab.research.google.com/drive/1YYk4fVlVDghrzEj_q_F-smbuSFMmhSK_#scrollTo=APohB_f101Ek


#### Задание RNN.


# Занятие 3. Защита работ.
15 апреля?

# Экзамен
18 апреля
- Защита работ
