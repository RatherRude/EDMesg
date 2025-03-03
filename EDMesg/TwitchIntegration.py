from typing import List, Optional, Literal
from .base import EDMesgAction, EDMesgEvent
from .EDMesgProvider import EDMesgProvider


class TwitchNotificationEvent(EDMesgEvent):
    """Event sent when a notification is received from Twitch"""
    message: str
    notification_type: Literal[
        "follow",   # New follower
        "tip",      # Donation/tip
        "host",     # Channel host
        "sub",      # New subscription
        "resub",    # Resubscription
        "giftsub",  # Gifted subscription
        "bits",     # Bits cheer
        "redeem",   # Channel point redemption
        "raid",     # Channel raid
        "order",    # Store order
        "message"   # Chat message
    ]
    timestamp: Optional[str] = None


# Factory methods
provider_name = "TWITCH_INTEGRATION"
actions: list[type[EDMesgAction]] = []  # No actions needed since we only send events
events: list[type[EDMesgEvent]] = [TwitchNotificationEvent]
actions_port = 15570  # Using a new port range
events_port = 15571


def create_twitch_provider() -> EDMesgProvider:
    return EDMesgProvider(
        provider_name=provider_name,
        action_types=actions,
        event_types=events,
        action_port=actions_port,
        event_port=events_port,
    ) 