from pydantic import BaseModel, Field
from typing import List, Optional

class EmergencyScenario(BaseModel):
    """Information about an emergency scenario."""
    scenario_name: str = Field(description="name of the emergency scenario")
    description: str = Field(description="description of the emergency scenario")

class InjuriesChart(BaseModel):
    no_injuries: int = Field(description="people who are not injured")
    minor_injuries: int = Field(description="people who have minor injuries")
    moderate_injuries: int = Field(description="people who have moderate injuries")
    major_injuries: int = Field(description="people who have major injuries")
    injured_civilians: int = Field(description="total count of civilians who are injured in the mission")
    injured_firefighters: int = Field(description="total count of firefighters who are injured in the mission")

