from typing import List, TypedDict, Union, Literal
from .base import EDMesgAction, EDMesgEvent
from .EDMesgProvider import EDMesgProvider
from .EDMesgClient import EDMesgClient

class CovasReplied(EDMesgEvent):
    muted: bool
    reasons: List[Union[Literal["user"], str]]
    text: str

class CommanderSpoke(EDMesgEvent):
    muted: bool
    text: str

# Factory methods
provider_name = "COVAS_NEXT"
actions = []
events = [CovasReplied, CommanderSpoke]
actions_port = 15550
events_port = 15551

def create_covasnext_provider() -> EDMesgProvider:
    return EDMesgProvider(
        provider_name=provider_name,
        action_types=actions,
        event_types=events
    )

def create_covasnext_client() -> EDMesgClient:
    return EDMesgClient(
        provider_name=provider_name,
        action_types=actions,
        event_types=events
    )
