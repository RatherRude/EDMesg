from typing import List, TypedDict
from .base import EDMesgAction, EDMesgEvent
from .EDMesgProvider import EDMesgProvider
from .EDMesgClient import EDMesgClient

class SpeakAction(EDMesgAction):
    """
    Forces the AI to generate commentary on the current state of the game.
    """
    pass


class AssistantReplied(EDMesgEvent):
    muted: bool
    reason: Union[Literal["user"], str]
    text: str

class UserSpoke(EDMesgEvent):
    muted: bool
    text: str

# Factory methods
provider_name = "COVAS_NEXT"
actions = [SpeakAction]
events = [AssistantReplied, UserSpoke]
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
