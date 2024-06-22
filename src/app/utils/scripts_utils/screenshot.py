import pyautogui
import os

from utils.config_utils import *

Number_Of_ScreenShot = 0

def region_screenshot(regionScreen: tuple[int, int, int, int],name:str) -> str:
    try:
        savePath = os.path.join(ROOT,'temp',name)
        image = pyautogui.screenshot(region=regionScreen)
        image.save(savePath)
        return savePath
    except Exception as e:
        print("Error al tomar la captura")
        raise e


def calculate_region(x: int, y: int, x1: int, y1: int)-> tuple:
    width = x1 - x
    height = y1 - y
    return (x,y,width,height)