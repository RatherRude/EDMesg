from pydantic import BaseModel
from .base import EDMesgAction, EDMesgEvent
from .EDMesgProvider import EDMesgProvider
from .EDMesgClient import EDMesgClient

class OpenPanelAction(EDMesgAction):
    name: str

class SpeakThisAction(EDMesgAction):
    text: str

class PrintThisAction(EDMesgAction):
    text: str

class SpeakingPhraseEvent(EDMesgEvent):
    text: str
    duration: float

class BookmarkAttributes(BaseModel):
    has_landable_planets: bool
    has_atmosphere: bool

class Bookmark(BaseModel):
    number: int
    system_name: str
    last_visit: str
    number_of_visits: int
    attributes: BookmarkAttributes

class DisplayBookmarksPanelEvent(EDMesgEvent):
    bookmarks: list[Bookmark]



# Factory methods
provider_name = "EDCoPilot"
actions = [OpenPanelAction, PrintThisAction, SpeakThisAction]
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
