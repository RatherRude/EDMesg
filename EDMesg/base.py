
from abc import ABC
from pydantic import BaseModel
from typing import Dict, Any

class EDMesgAction(BaseModel, ABC):
    pass

class EDMesgEvent(BaseModel, ABC):
    pass

class EDMesgEnvelope(BaseModel):
    type: str
    data: Dict[str, Any]