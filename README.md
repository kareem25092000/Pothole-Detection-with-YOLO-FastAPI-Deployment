# 🛣️ Pothole Detection with YOLO & FastAPI

A complete **computer vision pipeline** for detecting potholes in road images using fine-tuned YOLO models, deployed through a **FastAPI** backend for real-time inference.

---

## 📌 Overview

This project demonstrates an end-to-end workflow:

* 📦 Data collection & annotation (Roboflow)
* 🧠 Training YOLO object detection models
* ⚙️ Model evaluation & comparison
* 🌐 Deployment via FastAPI
* 🖼️ Real-time image inference with bounding boxes

---

## 🚀 Features

* ⚡ Two optimized YOLO models:

  * **YOLO Nano** → faster inference, lower accuracy
  * **YOLO Small** → slower but more accurate
* 🔁 Full ML lifecycle (data → training → deployment)
* 🌐 REST API for real-time predictions
* 🖼️ Returns annotated images with detected potholes

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <repo-name>
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure environment variables

Create a `.env` file:

```env
api=YOUR_ROBOFLOW_API_KEY
```

---

### 4. Update Model Paths ⚠️

Make sure to update the model paths inside your code (e.g., `main.py`):

```python
MODEL_SMALL_PATH = "path/to/yolo_small.pt"
MODEL_NANO_PATH = "path/to/yolo_nano.pt"
```

---

## 📊 Dataset

### 🔹 Pothole Detection Dataset

Roboflow dataset:
https://universe.roboflow.com/yolov8-uav/potholes-detect-uytky

Used for training pothole detection models.

---

### 🔹 Custom Dataset (Optional)

You can experiment with other datasets, for example:
https://app.roboflow.com/karim-mgcry/dogs-vs-cats-ydlkh

---

## ▶️ Run the API

```bash
uvicorn main:app --reload
```

---

## 📚 API Documentation

Once running, open:

```
http://127.0.0.1:8000/docs
```

Interactive Swagger UI will allow you to test endpoints.

---

## 🔌 API Endpoints

### 📍 `POST /predict_small`

* Uses **YOLO Small**
* Higher accuracy
* Slower inference

---

### 📍 `POST /predict_nano`

* Uses **YOLO Nano**
* Faster inference
* Lower accuracy

---

## 🧪 Example Workflow

1. Upload an image via API
2. Model processes the image
3. Returns:

   * Detected potholes
   * Image with bounding boxes

---

## 🛠️ Notes

* Ensure your model files (`.pt`) are correctly loaded
* GPU is recommended for faster inference
* Roboflow API key speeds up dataset download
