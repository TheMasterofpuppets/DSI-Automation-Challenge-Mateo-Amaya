from utils.scripts_utils import keyboard, mouse
from time import sleep

def backup_warden(path:str,browser)->None:

    keyboard.open_application(browser)

    mouse.move_and_click(745, 65,"left")
    keyboard.write("drive.google.com")
    keyboard.enter()

    sleep(1)

    mouse.move_and_click(60,184,"left")

    mouse.move_and_click(77,260,"left")

    mouse.move_and_click(446,55,"left")

    keyboard.write(path)
    keyboard.enter()

    mouse.move_and_click(771,492,"left")

    mouse.move_and_click(1052, 188, "left")