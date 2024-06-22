from .scanners import *
from ...utils.scripts_utils import keyboard

from .send_email_bot import send_mail

from time import sleep

def check_invoice_and_email(path:str) -> None:

    keyboard.open_application(path)

    sleep(1)

    factures = scan_factures()

    for i in factures:
        if i["price"] > 20000:
            send_mail(f"{i["name"]} Ten cuidado con tus gastos","Notificacion de gastos",i["email"])