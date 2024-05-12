from fastapi import APIRouter, Query, File, UploadFile
from fastapi.responses import JSONResponse
from app.classes.incident_resport_analysis import IncidentReportAnalysis
from utils.file_utils import save_file_async

import os

ira = IncidentReportAnalysis()
router = APIRouter()

@router.post('/generate_analysis')
async def generate_incident_report_analysis(incident_report: str = Query(None, title="report", description="Enter the report"),
                                            file: UploadFile = File(None)):
    
    if file != None:
        storage_directory = "data"
        os.makedirs(storage_directory, exist_ok=True)

        await save_file_async(file, storage_directory)
    
    response = ira.analyze_file_report(directory=storage_directory)
    return JSONResponse(content=response, status_code=200)

@router.get('/generate_casualties_count_charts')
async def generate_casualties_count_charts(data: str = Query(None, title="data", description="Enter the data")):
    response = ira.generate_casualties_count_charts(data=data)
    return JSONResponse(content=response, status_code=200)