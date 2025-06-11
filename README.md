## 📸 Face, Eye, and Smile Detection using Haarcascade & OpenCV

This project demonstrates how to detect **faces**, **eyes**, and **smiles** using OpenCV and Haarcascade classifiers in Python.
It includes multiple scripts that handle detection from both **webcam** and **image files**, and each detection task can be run separately or together.

---

### 🧠 Features

* ✅ Face detection (from webcam or image)
* 👁️ Eye detection (from webcam or image)
* 😄 Smile detection (from webcam or image)
* 🎯 Combined detection (face + eyes + smile)
* 💻 Real-time detection via webcam
* 🖼️ Static detection via uploaded images

---

### 🛠 Requirements

Install the required libraries via pip:

```bash
pip install opencv-python
```

---

### 📂 File Structure

| File Name         | Description                               |
| ----------------- | ----------------------------------------- |
| `face_webcam.py`  | Detect faces using webcam                 |
| `face_image.py`   | Detect faces in an image                  |
| `eyes_webcam.py`  | Detect eyes using webcam                  |
| `eyes_image.py`   | Detect eyes in an image                   |
| `smile_webcam.py` | Detect smiles using webcam                |
| `smile_image.py`  | Detect smiles in an image                 |
| `all_webcam.py`   | Detect face, eyes, and smile using webcam |
| `all_image.py`    | Detect face, eyes, and smile in an image  |

---

### 📸 Haarcascade Files Used

All Haarcascade classifiers are loaded directly from OpenCV’s built-in paths:

```python
cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
cv2.data.haarcascades + 'haarcascade_eye.xml'
cv2.data.haarcascades + 'haarcascade_smile.xml'
```

No need to download anything manually!

---

### ▶️ How to Run

#### Example (Face Detection from Webcam):

```bash
python face_webcam.py
```

#### Example (Face + Eyes + Smile Detection from Image):

```bash
python all_image.py
```

Make sure to replace `'your_image.jpg'` in the code with the actual path to your image.

---

### 📌 Notes

* Press **ESC** to exit any webcam detection window.
* You can modify the scale factor and minNeighbors in `detectMultiScale()` to improve detection accuracy.

---

### 📜 License

This project is free to use under the MIT License.


