import pyautogui
from time import sleep

def press(key:str | list )-> None:
    pyautogui.press(key)

def hold(key1: str, key2: str | list) -> None:
    with pyautogui.hold(key1):
        pyautogui.press(key2)

def write(text:str)->None:
    pyautogui.write(text,interval=0.0001)

def enter()->None:
    pyautogui.press("enter")

def paste()->None:
    pyautogui.hotkey("ctrl", "v")

def open_application(name:str) -> None:
    hold("win","r")
    write(name)

    sleep(1)

    enter()

