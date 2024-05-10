from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from dotenv import load_dotenv
from app.routes.emergency_response_simulator_route import router as emergency_response_simulator_router

load_dotenv()

app = FastAPI()

app.include_router(emergency_response_simulator_router)

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

