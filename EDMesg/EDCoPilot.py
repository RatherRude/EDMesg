from pydantic import BaseModel
from .base import EDMesgAction, EDMesgEvent
from .EDMesgProvider import EDMesgProvider
from .EDMesgClient import EDMesgClient
from typing import Any, Dict, Optional, Union
from typing_extensions import Literal


class OpenPanelAction(EDMesgAction):
    panelName: Literal[
        "bookmarks", "bookmarkgroups", "voicelog", "eventlog", "sessionprogress",
        "systemhistory", "traderoute", "discoveryestimator", "miningstats", "miningprices",
        "placesofinterest", "locationsearch", "locationresults", "guidancecomputer", "timetrials",
        "systeminfo", "stations", "bodies",	"factionsystems", "miningprices",
        "stationfacts", "bodydata", "blueprints", "shiplist", "storedmodules",
        "materials", "shiplocker", "suitlist", "weaponlist", "aboutedcopilot", "permits",
        "messages", "prospectorannouncements", "music",	"historyrefresh",
        "commandreference", "settings"
    ]
    details: str

class PanelNavigationAction(EDMesgAction):
    navigate: Literal[
        "scrolldown", "scrollup", "scrolltop", "scrollbottom", "back"
    ]
    item: int


class SpeakingPhraseEvent(EDMesgEvent):
    text: str
    reason: Union[str, Literal[
        "ArrivedAtDesination", # when reached system that was plotted to
        "ArrivedHome", # when reached system that is designated a home system
        "ChitChat", # ship chit-chat
        "FacilitySystemReminder", # when reached system that was recommended to visit a particular facility (eg after a search)
        "FirstVisitToStation", # when docked at station for first time
        "HGE", # candidate system for HGEs
        "LastHere", # when reaching a destination system
    ]]
    duration: float
    timestamp: str


class LastVisitedEvent(EDMesgEvent):
    days_since_last_here: float
    visit_number: int
    passed_through_count: int
    timestamp: str


class BookmarkAttributes(BaseModel):  # placeholder for future?
    has_landable_planets: bool
    has_atmosphere: bool


class Bookmark(BaseModel):  # placeholder for future?
    number: int
    system_name: str
    last_visit: str
    number_of_visits: int
    attributes: BookmarkAttributes


class DisplayBookmarksPanelEvent(EDMesgEvent):  # placeholder for future?
    bookmarks: list[Bookmark]


class PanelOpenedEvent(EDMesgEvent):  # placeholder for future?
    name: str
    contents: Optional[Dict[str, Any]]

# Factory methods
provider_name = "EDCoPilot"
actions: list[type[EDMesgAction]] = [OpenPanelAction]
events: list[type[EDMesgEvent]] = [
    SpeakingPhraseEvent,
    LastVisitedEvent,
    PanelOpenedEvent,
    DisplayBookmarksPanelEvent,
]
actions_port = 15560
events_port = 15561


def create_edcopilot_provider() -> EDMesgProvider:
    return EDMesgProvider(
        provider_name=provider_name,
        action_types=actions,
        event_types=events,
        action_port=actions_port,
        event_port=events_port,
    )


def create_edcopilot_client() -> EDMesgClient:
    return EDMesgClient(
        provider_name=provider_name,
        action_types=actions,
        event_types=events,
        action_port=actions_port,
        event_port=events_port,
    )
