from utils.bot_utils import backup_bot, invoice_and_email_bot
from utils.bot_utils import send_email_bot

def activate_bot1(path:str)-> str:
    invoice_and_email_bot.check_invoice_and_email(path)
    return f'bot 1 activado'

def activate_bot2(path:str)->str:
    backup_bot.backup_warden(path,"brave")
    return f'bot 2 activado'

def activate_bot3(dest:str, sbj: str, msg: str)->str:
    send_email_bot.send_mail(msg,sbj,dest)
    return f'bot 2 activado'