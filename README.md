# 🛣️ Pothole Detection with YOLO & FastAPI

Building a robust **computer vision pipeline** to automatically detect potholes in road images using fine-tuned YOLO models. This project covers the full lifecycle: data collection, annotation, training, and deployment via a FastAPI backend.

---

## 📌 Overview

This project demonstrates how to:

- Train multiple YOLO models for object detection
- Work with datasets from Roboflow
- Build a real-time inference API using FastAPI
- Serve model predictions as images

---

## 🚀 Features

- ⚡ Two trained models:
  - YOLO Nano (fast inference)
  - YOLO Small (higher accuracy)
- 🧠 End-to-end ML pipeline (data → training → deployment)
- 🌐 FastAPI backend for real-time predictions
- 🖼️ Image-based inference with bounding box visualization

---

## 📊 Dataset

### 1. Pothole Detection Dataset
https://universe.roboflow.com/yolov8-uav/potholes-detect-uytky  

Add your API key in `.env`:

```
api=YOUR_ROBOFLOW_API_KEY
```
to download the dataset faster

---

### 2. Custom Dataset
you can try different dataset like :
https://app.roboflow.com/karim-mgcry/dogs-vs-cats-ydlkh  

---





## ▶️ Run API

```
uvicorn main:app --reload
```

Docs:
http://127.0.0.1:8000/docs

---

## 🔌 Endpoints

### POST /predict_small  
### POST /predict_nano  

