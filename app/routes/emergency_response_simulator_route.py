from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from app.classes.emergency_response_simulator import EmergencyResponseSimulator

emrs = EmergencyResponseSimulator()
router = APIRouter()

@router.get('/generate_scenario')
async def generate_scenario_api():
    response = emrs.generate_scenario()
    return JSONResponse(content=response, status_code=200)

@router.get('/generate_response')
async def generate_response_for_scenario_with_trainee_inputs(trainee_response: str = Query(..., title="response", description="Enter the trainee response"),
                                                             scenario: str = Query(..., title="scenario", description="Enter the scenario")):
    response = emrs.generate_response_scenario(trainee_response=trainee_response, scenario=scenario)
    return JSONResponse(content=response, status_code=200)
