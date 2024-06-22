import pyautogui

def move_to(x:int, y:int) -> None:
    pyautogui.moveTo(x,y,1)

def move_and_click(positionX: int, positionY: int, buttonPress:str) -> None:
    pyautogui.click(positionX,positionY,button=buttonPress,duration=1,)

def click(buttonPress:str, clicksPress:int = 1) -> None:
    pyautogui.click(button=buttonPress, clicks=clicksPress)
