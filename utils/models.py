from pydantic import BaseModel, Field
from typing import List, Optional

class EmergencyScenario(BaseModel):
    """Information about an emergency scenario."""
    scenario_name: str = Field(description="name of the emergency scenario")
    description: str = Field(description="description of the emergency scenario")