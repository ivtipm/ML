"""
Обучает модель RandomForestClassifier решать задачу классификации, сохраняет в файл
Имя файла содержит названия версий sklearn и joblib
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load

import joblib
import sklearn

print("joblib version  " + joblib.__version__)
print("sklearn version " + sklearn.__version__)


data = load_iris()
y = data.target
X = data.data

X_train, X_test, y_train, y_test =  train_test_split(X,y, test_size=0.2)
forest = RandomForestClassifier(3)


forest.fit(X_train,y_train)
y_pred_train = forest.predict(X_train)
y_pred_test  = forest.predict(X_test)

print("Train")
print(classification_report(y_train, y_pred_train))
print("\n\nTest")
print(classification_report(y_test, y_pred_test))

# сохранение модели
dump(forest, 'rand_forest_model_sk150_joblib142.joblib')
# загрузка модели
forest2 = load('rand_forest_model_sk150_joblib142.joblib')

# для проверки
# todo: add asserts
y_pred_train = forest2.predict(X_train)
y_pred_test  = forest2.predict(X_test)

print("Train")
print(classification_report(y_train, y_pred_train))
print("\n\nTest")
print(classification_report(y_test, y_pred_test))