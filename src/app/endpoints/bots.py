from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.bot_service import activate_bot1_service, activate_bot2_service, activate_bot3_service

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
async def activate_check_facture_endpoint(input: FolderBotInput):
    try:
        result = activate_bot1_service(input.path)
        return BotOutput(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/activate_backup_Bot", response_model=BotOutput)
async def activate_backup_endpoint(input: FolderBotInput):
    try:
        result = activate_bot2_service(input.path)
        return BotOutput(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/activate_email_bot", response_model=BotOutput)
async def activate_email_bot_endpoint(input: EmailBotInput):
    try:
        result = activate_bot3_service(input.dest, input.sbj, input.msg)
        return BotOutput(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))