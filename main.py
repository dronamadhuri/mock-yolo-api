import os
import uuid
import aiofiles

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import Optional, List

from sqlalchemy.orm import Session

from ml.mock_yolo import run_mock_yolo
from db.database import Base, engine, SessionLocal
from db.models import DetectionLog, FeedbackLog


# -----------------------------
# App Initialization
# -----------------------------
app = FastAPI(title="Mock YOLO API + Feedback System")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Create database tables
Base.metadata.create_all(bind=engine)


# -----------------------------
# Pydantic Schemas (local use)
# -----------------------------
class FeedbackInput(BaseModel):
    detection_id: int
    corrected_label: str
    comment: Optional[str] = None


class DetectionResponse(BaseModel):
    filename: str
    detections: List[dict]


# -----------------------------
# Health Check
# -----------------------------
@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Mock YOLO API + Feedback System 🚀"
    }


# -----------------------------
# Upload Image + Run Mock YOLO
# -----------------------------
@app.post("/upload", response_model=DetectionResponse)
async def upload_image(file: UploadFile = File(...)):

    # Generate unique file name
    file_id = str(uuid.uuid4())
    file_path = f"{UPLOAD_DIR}/{file_id}_{file.filename}"

    # Save file asynchronously
    async with aiofiles.open(file_path, "wb") as f:
        content = await file.read()
        await f.write(content)

    # Run mock YOLO inference
    detections = run_mock_yolo(file_path)

    # Save to database
    db: Session = SessionLocal()

    log = DetectionLog(
        filename=file.filename,
        result=detections
    )

    db.add(log)
    db.commit()
    db.refresh(log)
    db.close()

    return {
        "filename": file.filename,
        "detections": detections
    }


# -----------------------------
# Get All Detection History
# -----------------------------
@app.get("/history")
def get_history():

    db: Session = SessionLocal()
    logs = db.query(DetectionLog).all()
    db.close()

    return [
        {
            "id": log.id,
            "filename": log.filename,
            "result": log.result
        }
        for log in logs
    ]


# -----------------------------
# Get Single Detection
# -----------------------------
@app.get("/history/{detection_id}")
def get_single_detection(detection_id: int):

    db: Session = SessionLocal()
    log = db.query(DetectionLog).filter(DetectionLog.id == detection_id).first()
    db.close()

    if not log:
        return {"error": "Detection not found"}

    return {
        "id": log.id,
        "filename": log.filename,
        "result": log.result
    }


# -----------------------------
# Submit Feedback (NEW 🔥)
# -----------------------------
@app.post("/feedback")
def submit_feedback(data: FeedbackInput):

    db: Session = SessionLocal()

    feedback = FeedbackLog(
        detection_id=data.detection_id,
        corrected_label=data.corrected_label,
        comment=data.comment
    )

    db.add(feedback)
    db.commit()
    db.close()

    return {
        "message": "Feedback saved successfully",
        "detection_id": data.detection_id
    }


# -----------------------------
# Get All Feedback
# -----------------------------
@app.get("/feedback")
def get_feedback():

    db: Session = SessionLocal()
    logs = db.query(FeedbackLog).all()
    db.close()

    return [
        {
            "id": f.id,
            "detection_id": f.detection_id,
            "corrected_label": f.corrected_label,
            "comment": f.comment
        }
        for f in logs
    ]