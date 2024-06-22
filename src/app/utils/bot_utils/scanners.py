from utils.scripts_utils import screenshot, mouse
from utils.ocr_utils.capture import *

from time import sleep

from . import invoice_analysis_bot as iab
from . import document_analysis_bot as dab
import re

def word_counter(text:str, word:str) -> int:
    text = text.lower()
    ocurrencias = re.findall(word,text,re.IGNORECASE)
    return len(ocurrencias)

def scan_factures()-> list:

    img = screenshot.region_screenshot(screenshot.calculate_region(192,130,392,419), "files.png")

    files = image_to_string(img)

    num_of_files = word_counter(files,"Factura")

    factures = list()

    if num_of_files:
        positionY = 180
        while num_of_files:

            mouse.move_to(240,positionY)
            sleep(0.1)
            mouse.click("left",2)
            sleep(1)

            info = iab.check_Facture()
            mouse.move_and_click(1889,16,"left")

            factures.append(info)

            num_of_files -=1
            positionY += 30

    return factures


def scan_files() -> list:

    img = screenshot.region_screenshot(screenshot.calculate_Region(195,167,305,598), "files.png")

    files = image_to_string(img)

    num_of_files = word_counter(files,"Documento")

    documents = list()

    if num_of_files:

        mouse.move_to(268,184)
        sleep(0.1)
        mouse.click("left",2)
        sleep(2)
        x = 825

        info = dab.check_document()
        documents.append(info)

        mouse.move_and_click(x, 1002,"left")

        while num_of_files:

            info = dab.check_document()
            documents.append(info)
            mouse.move_and_click(x, 1002,"left")
            x += 60
            num_of_files -= 1

    return documents