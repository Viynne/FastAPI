from pydantic import BaseModel
from enum import Enum


class YolovModel(str, Enum):
    yolov3 = "yolov3"
    yolov3_tiny = "yolov3-tiny"