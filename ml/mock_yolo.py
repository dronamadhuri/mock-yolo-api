import random

CLASSES = ["person", "car", "dog", "cat", "bottle", "laptop", "chair"]

def run_mock_yolo(image_path: str):
    detections = []
    num_boxes = random.randint(1, 4)

    for _ in range(num_boxes):
        detections.append({
            "label": random.choice(CLASSES),
            "confidence": round(random.uniform(0.5, 0.99), 2),
            "x": round(random.uniform(0, 0.7), 2),
            "y": round(random.uniform(0, 0.7), 2),
            "w": round(random.uniform(0.1, 0.3), 2),
            "h": round(random.uniform(0.1, 0.3), 2),
        })

    return detections