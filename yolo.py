from ultralytics import YOLO

class YOLOModel:
    def __init__(self) -> None:
         
        self.model1 = YOLO('yolov8n.pt')