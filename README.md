````markdown
# iPhone OR Samsung

A minimal image classifier that determines whether a photo shows an **iPhone** or a **Samsung** phone.  
This repository contains everything you need to run the classifier locally or in Google Colab.
 

---

## 1. Local Setup & Usage

1. **Clone the repository**  
   ```bash
   git clone https://github.com/MohammedBosaid/iPhone-OR-Samsung.git
   cd iPhone-OR-Samsung
````

2. **Install Python dependencies**
   (You can skip this if you already have them installed.)

   ```bash
   python3 -m venv env
   source env/bin/activate      # Windows: .\env\Scripts\activate
   pip install --upgrade pip
   pip install tensorflow pillow numpy
   ```

3. **Run the classifier**

   ```bash
   python classify_phone.py path/to/your_image.jpg
   ```

   * Replace `path/to/your_image.jpg` with the path to the image you want to classify.
   * You will see output like:

     ```
     path/to/your_image.jpg → iPhone
     ```

     or

     ```
     path/to/your_image.jpg → Samsung
     ```

---

## 2. Google Colab Usage

1. **Open a new Colab notebook** at [https://colab.research.google.com](https://colab.research.google.com)
2. **Upload** these files into Colab’s Files pane:

   * `classify_phone.py`
   * `labels.txt`
   * `keras_model.h5`
   * your test image(s)
3. **Install dependencies & classify** in one cell:

   ```python
   !pip install tensorflow pillow numpy

   from google.colab import files
   from classify_phone import predict_phone

   uploaded = files.upload()      # choose one or more phone images
   for fname in uploaded.keys():
       predict_phone(fname)
   ```
4. **View your results**: each filename prints its predicted class:

   ```
   your_image.jpg → Samsung
   ```

---

## 3. File Details

* **`classify_phone.py`**
  Loads `keras_model.h5`, reads `labels.txt`, then prints:

  ```
  <image-path> → <PredictedLabel>
  ```

* **`labels.txt`**
  Must list classes in the same order the model was trained:

  ```
  iPhone
  Samsung
  ```

* **`Model Test.png`**
  A screenshot showing the script classifying an image (no confidence score).

---

Enjoy testing your model! If you encounter any issues, double-check that your filenames match exactly and that `labels.txt` aligns with your model’s output indices.

```
```
