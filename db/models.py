from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from .database import Base

class DetectionLog(Base):
    __tablename__ = "detections"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    result = Column(JSON)


class FeedbackLog(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    detection_id = Column(Integer, ForeignKey("detections.id"))
    corrected_label = Column(String)
    comment = Column(String)