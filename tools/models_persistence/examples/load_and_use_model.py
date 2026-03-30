# %% Cell 1
import numpy as np
import onnxruntime as rt

model_filename = "random_forest_50t_md2.onnx"

sess = rt.InferenceSession(model_filename, providers=["CPUExecutionProvider"])
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name


X_test = np.load("X_test_10.npy")
pred_onx = sess.run([label_name], {input_name: X_test})
assert (pred_onx == np.array([0, 1, 0, 1, 0, 0, 1, 0, 0, 0])).all()

print("Test Passed!")
