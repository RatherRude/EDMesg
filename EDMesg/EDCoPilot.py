from .base import EDMesgAction, EDMesgEvent
from .EDMesgProvider import EDMesgProvider
from .EDMesgClient import EDMesgClient

class OpenPanelAction(EDMesgAction):
    name: str

class SpeakingPhraseEvent(EDMesgEvent):
    text: str
    duration: float


# Factory methods
actions = [OpenPanelAction]
events = [SpeakingPhraseEvent]

def create_edcopilot_provider() -> EDMesgProvider:
    return EDMesgProvider(
        provider_name="EDCoPilot",
        action_types=actions,
        event_types=events
    )

def create_edcopilot_client() -> EDMesgClient:
    return EDMesgClient(
        provider_name="EDCoPilot",
        action_types=actions,
        event_types=events
    )