from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from app.classes.equipment_maintainance_predictor import EquipmentMaintainancePredictor

emp = EquipmentMaintainancePredictor()
router = APIRouter()

@router.post('/predict_maintenance')
async def predict_maintenance_for_equipment(operating_hours: int = Query(..., title="operating hours", description="Enter the operating hours"),
                                            temperature: int = Query(..., title="temperature", description="Enter the temperature"),
                                            pressure: int = Query(..., title="pressure", description="Enter the pressure")):
    
    response = emp.predict_maintenance(operating_hours=operating_hours, temperature=temperature, pressure=pressure)
    return JSONResponse(content=response, status_code=200)
