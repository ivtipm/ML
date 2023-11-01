# pytorch
```python
import torch
```

# tensor
tensor -- многомерный массив, основной тип данных pytorch.

```python
x = torch.tensor([[4, 2, 3],
                 [2, 6, 8]])

x.shape                 # torch.Size([2, 3])
```

**Перестановка размерностей**
```python
x = torch.tensor([[4, 2, 3],
                 [2, 6, 8]])
# установка размерностей в порядке: 1 и 0
torch.permute(x, (1,0) )

# результат
tensor([[4, 2],
        [2, 6],
        [3, 8]])
```

**избавится от размерностей в 1**
```python
a = torch.tensor([ [[4], [2], [3]] ])
a.shape                 # torch.Size([1, 3, 1])  

a.squeeze()             # -> torch.Size([3])                 
# результат: 
tensor([4, 2, 3])

```

**вставка размерности**


**массив из многомерного массива**
```python
x.flatten()             
# результат
tensor([4, 2, 3, 2, 6, 8])
```

# Загрузка данных
`torch.utils.data.Dataset`.\
**`Dataset`** — класс для работы с датасетами, обязан иметь методы [[doc](https://pytorch.org/docs/stable/data.html#torch.utils.data.Dataset)]:
- `__getitem__()` — метод достпуа по ключу (например `my_dataset[0]`)
- `__len__()` — возвращает размер массива (например `len(my_dataset)`)


**`DataLoader`** — более высокоуровневый класс для работы с данными. Загружает данные в оперативную память, раделяет на батчи, преобразует перед подачей в модель
[[doc](https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader)]\
Основные аттрибуты:
- `dataset:Dataset` — датасет
- `batch_size:int` — размер батча
- `shuffle:bool` — перемешивать данные каждую эпоху?
- `num_workers:int = 0` — количество процессов для загрузки
- `collate_fn:Callable` — функция или объект, используемые для операций над датасетом.

(см. [специальные методы классов в Pyhton](https://coderpad.io/python-magic-methods-cheat-sheet/))


См. также класс `datasets.ImageFolder` для работы с датасетом из отдельных файлов.




# Слои

- `nn.Sequential( [ ... ] )`
- `nn.Linear(in_features=10, out_features=128, )` — 128 нейронов, 10 входов у каждого
- `nn.MaxPool2d(kernel_size=2)`
- `nn.Conv2d( in_channels=3  , out_channels=32, kernel_size=3)` — 32 свёртки, принимающих картинку с тремя каналами
- Активации:
    - `nn.LeakyReLU()`
    - `nn.Sigmoid()`
    - ...
- `nn.BatchNorm1d(64)` — батчнорм на 64 фичи
- ...

## Embedding
`torch.nn.Embedding` создаёт эмбеддинги (вектора) слов.
https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html

Как правило используются вектора размерностью 100-300. 


```python
import torch
from torch import nn

# текст, где каждое слово представлено числом -- его номером в словаре (см. класс Vocab)
# нули (число-заполнитель -- padding index) поставлены для выравнивания всех тектов по одной длине 
text = torch.tensor( [[12, 27, 4, 56, 3, 81, 0, 0, 0, 0 ]] ) 		# [batch_size = 1, sequence_len = 10]


emb = nn.Embedding(num_embeddings = 100, 	# размер словаря
				   embedding_dim = 128, 	# размерность вектора
				   padding_idx = 0 			# 
				   )

emb( text )			# -> [batch_size, seq_len, emb_dim]

```

Результат:
```python
tensor([[[ 0.6943,  1.0508, -1.8730,  ..., -0.2826,  0.2395,  1.0945],
         [ 0.3233,  1.6904,  0.2099,  ...,  0.5310, -1.2767,  2.1296],
         [ 0.9116, -0.6055,  1.3053,  ..., -2.3760,  1.9805, -0.3670],
         ...,
         [ 0.0000,  0.0000,  0.0000,  ...,  0.0000,  0.0000,  0.0000],
         [ 0.0000,  0.0000,  0.0000,  ...,  0.0000,  0.0000,  0.0000],
         [ 0.0000,  0.0000,  0.0000,  ...,  0.0000,  0.0000,  0.0000]]],
       grad_fn=<EmbeddingBackward0>)

```

# Работа с моделями

**общая информация**
```python
from torchsummary import summary        # для вывода основных сведений про нейросеть

summary( my_model, input_size = (3,28,28) ) 
```

## Сохранение и загрузка модели
```python
# сохранение
torch.save(my_model.state_dict(), "my_model.model")

# загрузка
my_model = MyModelClass()
my_model.load_state_dict(torch.load("my_model.model"))
my_model.eval()
```

## Обучение модели
```python
# перевод нейросети в режим обучения
model.train()

for ep in range( 10 ):                  # цикл по эпохам
    epoch_loss = 0                      # для подсчёта средней ошибки в эпохе
    
    for batch_idx, (xb, yb) in enumerate(train_loader):     # перебор батчей
        
        y_pred = model( xb.cuda() )                   # прямой проход

        loss = loss_fn(y_pred, yb.cuda())           # вычисление ошибки
        epoch_loss += loss.item()                   # .item() возвращает ошибку (число)

        model.zero_grad()                           # обнуление градиентов
        loss.backward()                             # вычисление градиентов
        optimizer.step()                            # обновление весов
     # todo: вычисление метрик качества
     # todo: лосс и качество на валидации
     # todo: вывод инф-и о ходу обучения или логирование в wandb
```


# torchvision

**Картинку в тензор**
```python
from torchvision.io.image import read_image                         # загрузка файла в тензор

img = read_image("image.png") 
```