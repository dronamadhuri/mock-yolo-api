from pydantic import BaseModel
from typing import List, Optional

class Box(BaseModel):
    label: str
    confidence: float
    x: float
    y: float
    w: float
    h: float


class DetectionResponse(BaseModel):
    filename: str
    detections: List[Box]


class FeedbackInput(BaseModel):
    detection_id: int
    corrected_label: str
    comment: Optional[str] = None