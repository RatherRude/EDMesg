from .base import EDMesgAction, EDMesgEvent
from .EDMesgProvider import EDMesgProvider
from .EDMesgClient import EDMesgClient

class OpenPanelAction(EDMesgAction):
    name: str

class SpeakingPhraseEvent(EDMesgEvent):
    text: str
    duration: float


# Factory methods
provider_name = "EDCoPilot"
actions = [OpenPanelAction]
events = [SpeakingPhraseEvent]
actions_port = 15560
events_port = 15561

def create_edcopilot_provider() -> EDMesgProvider:
    return EDMesgProvider(
        provider_name=provider_name,
        action_types=actions,
        event_types=events,
        action_port=actions_port,
        event_port=events_port
    )

def create_edcopilot_client() -> EDMesgClient:
    return EDMesgClient(
        provider_name=provider_name,
        action_types=actions,
        event_types=events,
        action_port=actions_port,
        event_port=events_port
    )