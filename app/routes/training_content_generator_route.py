from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.classes.training_content_generator import TrainingContentGenerator

tcg = TrainingContentGenerator()
router = APIRouter()

@router.get('/generate_training_content')
async def generate_training_content():
    response = tcg.generate_training_content()
    return JSONResponse(content=response, status_code=200)