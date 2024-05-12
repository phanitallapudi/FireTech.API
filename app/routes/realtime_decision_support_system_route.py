from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from app.classes.realtime_decision_support_system import RealtimeDecisionSupportSystem

rtdss = RealtimeDecisionSupportSystem()
router = APIRouter()

@router.get('/realtime_support_system')
async def realtime_support_system(data: str = Query(..., title="data", description="Enter the data to process")):
    response = rtdss.get_response_rtdss(data=data)
    return JSONResponse(content=response, status_code=200)
