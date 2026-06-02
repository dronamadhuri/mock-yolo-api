# 🧠 Mock YOLO Detection API (FastAPI + SQLite + Feedback System)

A lightweight **computer vision API simulation** built using FastAPI that mimics YOLO object detection.  
It supports image uploads, fake object detection, history tracking, and a feedback loop for improving predictions.

---

## 🚀 Features

- 📤 Upload images via API (Postman supported)
- 🧠 Mock YOLO object detection (simulated bounding boxes)
- 🗄️ SQLite database integration
- 📊 Detection history storage
- 🔁 Feedback system for correcting predictions
- ⚡ Async file handling using aiofiles
- 🧪 Fully testable using Postman or Swagger UI

---

## 🏗️ Tech Stack

- **FastAPI** – Backend framework
- **Uvicorn** – ASGI server
- **SQLAlchemy** – ORM for database
- **SQLite** – Lightweight database
- **Pydantic** – Data validation
- **aiofiles** – Async file uploads
- **Python 3.11+**

---

## 📁 Project Structure


mock-yolo-api/
│
├── main.py # FastAPI app
├── ml/
│ └── mock_yolo.py # Mock YOLO inference
│
├── db/
│ ├── database.py # DB connection
│ └── models.py # DB models
│
├── schemas/
│ └── detection.py # Pydantic schemas
│
├── uploads/ # Uploaded images
├── database.db # SQLite database
└── requirements.txt


---

## ⚙️ Installation

### 1. Clone repository
```bash
git clone https://github.com/dronamadhuri/mock-yolo-api.git
cd mock-yolo-api
2. Create virtual environment
py -3.11 -m venv venv
3. Activate environment

Windows (PowerShell):

.\venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
🚀 Run the server
uvicorn main:app --reload --port 8001
🌐 API Endpoints
🟢 Health Check
GET /
📤 Upload Image + Detect Objects
POST /upload

Form-data:

Key	Type	Description
file	File	Upload image
📊 Get Detection History
GET /history
📌 Get Single Detection
GET /history/{id}
🔁 Submit Feedback
POST /feedback

JSON Body:

{
  "detection_id": 1,
  "corrected_label": "dog",
  "comment": "Model misclassified object"
}
📋 Get All Feedback
GET /feedback
🧪 Example Response
{
  "filename": "image.jpg",
  "detections": [
    {
      "label": "dog",
      "confidence": 0.87,
      "x": 0.45,
      "y": 0.32,
      "w": 0.2,
      "h": 0.25
    }
  ]
}
📌 Future Improvements
🔥 Replace mock YOLO with real YOLOv8 model
📸 Return annotated images with bounding boxes
🌐 Add frontend dashboard (React)
📊 Analytics for detection trends
🐳 Dockerize the application
☁️ Deploy to cloud (Render / AWS / Railway)
👨‍💻 Author

Drona Madhuri Dadi

⭐ If you like this project

Give it a ⭐ on GitHub and contribute improvements!
