from fastapi import HTTPException
import io
import numpy as np


def filter_file_type(file_input):
    file_name = file_input.filename
    valid_image_format = ['jpg', 'jpeg', 'png']
    file_extension = file_name.split(".")[-1] in valid_image_format
    if not file_extension:
        raise HTTPException(status_code=425, detail="Unsupported file format")


def process_image_file(file_input):
    image_stream = io.BytesIO(file_input.file.read())
    image_stream.seek(0)
    image_stream_to_array = np.asarray(bytearray(image_stream.read()))
    return image_stream_to_array
