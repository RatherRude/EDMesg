
from abc import ABC
from pydantic import BaseModel
from typing import Dict, Any

class EDMesgAction(BaseModel, ABC):
    class Config:
        orm_mode = True

class EDMesgEvent(BaseModel, ABC):
    class Config:
        orm_mode = True

class EDMesgEnvelope(BaseModel):
    type: str
    data: Dict[str, Any]