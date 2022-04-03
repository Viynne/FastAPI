from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from models.functions import filter_file_type, process_image_file
from models.model import YolovModel
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

app = FastAPI(title="Testing how files are uploaded on fast")


@app.get("/")
async def home_page():
    return{"Message": "Wo you don start am, no look me"}


@app.post("/collect")
async def receive_image(model: YolovModel, file: UploadFile = File(...)):
    """
    Server request. Image file for detection.
    :param model: Available model Yolov3-tiny, Yolov3
    :param file: Image file
    :return: image with label object in bounding box
    """
    # File file format to check for unsupported format
    filter_file_type(file)

    # process image file to array to be fed into the machine learning algorithm
    processed_image = process_image_file(file)

    # cv read processed image
    img = cv2.imdecode(processed_image, cv2.IMREAD_COLOR)

    # Object detection
    bbox, label, conf = cv.detect_common_objects(img, model=model, )
    img_output = draw_bbox(img, bbox, label, conf)

    # Write image to folder after detection
    cv2.imwrite(f"uploaded_image/{file.filename}", img_output)

    open_image = open(f"uploaded_image/{file.filename}", mode='rb')
    return StreamingResponse(open_image, media_type='image/jpeg')


