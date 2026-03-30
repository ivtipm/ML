# %% Cell 1
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.datasets import make_classification

import skl2onnx

# создание данных
X, y = make_classification(n_samples=1000, n_features=20, class_sep=0.6, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=43)

# обучение модели
model = RandomForestClassifier(n_estimators=50, max_depth=2, random_state=44)
model.fit(X_train, y_train)

# оценка модели
yp_train = model.predict(X_train)
yp_test = model.predict(X_test)

print("Train")
print(classification_report(y_train, yp_train))
print("\nTest")
print(classification_report(y_test, yp_test))

print(model.predict(X_test[:10]))
assert (model.predict(X_test[:10])  == np.array([0, 1, 0, 1, 0, 0, 1, 0, 0, 0]) ).all()
# сохраним X_test[:10] в файл для последующих тестов
np.save("X_test_10.npy", X_test[:10])

# сохранение модели
onx_model = skl2onnx.to_onnx( model, X_train[:1])
model_filename = f"random_forest_{model.n_estimators}t_md{model.max_depth}.onnx"
# ONNX нужен пример входных данных, чтобы определить размерность входа. Поэтому передадим X_tran[:1]
# сами данные в модель не сохраняются
with open(model_filename, "wb") as f:
    f.write(onx_model.SerializeToString())
print(f"Model saved: {model_filename}")
