from ..TwitchIntegration import create_twitch_provider, TwitchNotificationEvent
from time import time


def main():
    # Create the provider
    provider = create_twitch_provider()

    try:
        # Create a simple notification
        notification = TwitchNotificationEvent(
            message="Hello from Twitch!",
            notification_type="message",
            timestamp=str(time())
        )

        # Send it
        provider.publish(notification)
        print("Notification sent!")

    finally:
        provider.close()


if __name__ == "__main__":
    main() 