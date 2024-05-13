from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from dotenv import load_dotenv
from app.routes.emergency_response_simulator_route import router as emergency_response_simulator_router
from app.routes.incident_report_analysis_route import router as incident_report_analysis_router
from app.routes.equiment_maintainance_predictor_route import router as equiment_maintainance_predictor_router
from app.routes.realtime_decision_support_system_route import router as realtime_decision_support_system_router
from app.routes.training_content_generator_route import router as training_content_generator_router

load_dotenv()

app = FastAPI()

app.include_router(emergency_response_simulator_router)
app.include_router(incident_report_analysis_router)
app.include_router(equiment_maintainance_predictor_router)
app.include_router(realtime_decision_support_system_router)
app.include_router(training_content_generator_router)

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

