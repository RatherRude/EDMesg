from typing import List, Literal, Union, Optional
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


class ConfigurationUpdated(EDMesgEvent):
    enabled_game_events: list[str]
    is_dominant: bool


class ExternalChatNotification(EDMesgAction):
    service: str  # 'twitch', 'discord' etc
    username: Optional[str] = None
    text: str


class ExternalBackgroundChatNotification(EDMesgAction):
    service: str  # 'twitch', 'discord' etc
    username: Optional[str] = None
    text: str


# Factory methods
provider_name = "COVAS_NEXT"
actions: list[type[EDMesgAction]] = [ExternalChatNotification, ExternalBackgroundChatNotification]
events: list[type[EDMesgEvent]] = [CovasReplied, CommanderSpoke, ConfigurationUpdated]
actions_port = 15550
events_port = 15551


def create_covasnext_provider() -> EDMesgProvider:
    return EDMesgProvider(
        provider_name=provider_name,
        action_types=actions,
        event_types=events,
        action_port=actions_port,
        event_port=events_port,
    )


def create_covasnext_client() -> EDMesgClient:
    return EDMesgClient(
        provider_name=provider_name,
        action_types=actions,
        event_types=events,
        action_port=actions_port,
        event_port=events_port,
    )
