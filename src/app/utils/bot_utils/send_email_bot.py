from utils.ocr_utils.capture import *
from utils.scripts_utils import mouse, keyboard
from time import sleep

import pyperclip

def send_mail(msg:str,sbj:str,dest:str) -> None:

    keyboard.open_application("brave")

    mouse.move_and_click(793,67,"left")

    keyboard.write("www.gmail.com")

    keyboard.enter()

    sleep(3)

    mouse.move_and_click(76,167,"left")

    sleep(0.5)

    pyperclip.copy(dest)
    keyboard.paste()


    mouse.move_and_click(1567,511,"left")

    keyboard.write(sbj)

    sleep(0.5)

    mouse.move_and_click(1647,550,"left")

    keyboard.write(msg)

    mouse.move_and_click(1299,1003,"left")