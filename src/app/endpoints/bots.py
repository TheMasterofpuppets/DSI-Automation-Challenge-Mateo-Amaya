from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from ..services.bot_service import activate_bot1_service, activate_bot2_service, activate_bot3_service
from ..auth.token_manager import get_current_user

router = APIRouter()

class FolderBotInput(BaseModel):
    path: str

class EmailBotInput(BaseModel):
    dest: str
    sbj: str
    msg: str

class BotOutput(BaseModel):
    result: str

@router.post("/activate_check_Facture", response_model=BotOutput)
async def activate_check_facture_endpoint(input: FolderBotInput, current_user: dict = Depends(get_current_user)):
    """
    Activate a bot service to check a folder for invoices.

    Parameters:
    - input (FolderBotInput): Input data containing the path to the folder.
    - current_user (dict): Current authenticated user details.

    Returns:
    - BotOutput: Result of the bot operation.
    """
    try:
        result = activate_bot1_service(input.path)
        return BotOutput(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/activate_backup_Bot", response_model=BotOutput)
async def activate_backup_endpoint(input: FolderBotInput, current_user: dict = Depends(get_current_user)):
    """
    Activates a backup bot using the specified folder path.

    Parameters:
    - input: FolderBotInput - Input data containing the folder path.
    - current_user: dict - Current authenticated user.

    Returns:
    - BotOutput: Result of the backup bot activation.
    """
    try:
        result = activate_bot2_service(input.path)
        return BotOutput(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/activate_email_bot", response_model=BotOutput)
async def activate_email_bot_endpoint(input: EmailBotInput, current_user: dict = Depends(get_current_user)):
    """
    Activates an email bot using the specified destination, subject, and message.

    Parameters:
    - input: EmailBotInput - Input data containing email details (destination, subject, message).
    - current_user: dict - Current authenticated user.

    Returns:
    - BotOutput: Result of the email bot activation.
    """
    try:
        result = activate_bot3_service(input.dest, input.sbj, input.msg)
        return BotOutput(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))