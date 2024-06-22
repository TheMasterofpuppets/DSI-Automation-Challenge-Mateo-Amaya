from PIL import Image

import os
from ...utils.config_utils import *

import pytesseract

pathImages = os.path.join(ROOT,'temp')

def image_to_string(image:str)->str:
    try:
        return pytesseract.image_to_string(Image.open(image))
    except FileNotFoundError as e:
        return f"File not Found"