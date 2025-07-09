# 1) Imports (Colab already has TensorFlow)
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from google.colab import files

# 2) Load your model (assumes keras_model.h5 is in the Files pane)
model = tf.keras.models.load_model('keras_model.h5', compile=False)
print(f"✅ Model loaded. Input shape: {model.input_shape}")

# 3) Load labels (one per line: iPhone, Samsung)
with open('labels.txt', 'r') as f:
    class_names = [line.strip() for line in f if line.strip()]
print("✅ Labels:", class_names)

# 4) Preprocessing + prediction helpers
def preprocess_image(path):
    H, W = model.input_shape[1:3]
    img = image.load_img(path, target_size=(H, W))
    arr = image.img_to_array(img).astype('float32') / 255.0
    return np.expand_dims(arr, axis=0)

def predict_phone(path):
    x     = preprocess_image(path)
    preds = model.predict(x)[0]
    idx   = np.argmax(preds)
    label = class_names[idx]
    print(f"{path} → Predicted phone type: {label}")

# 5) Upload & classify
print("▶️ Please upload phone images (JPEG/PNG):")
uploaded = files.upload()
for fn in uploaded.keys():
    predict_phone(fn)
