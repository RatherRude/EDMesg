from ..EDCoPilot import (
    create_edcopilot_client,
    OpenPanelAction,
    SpeakingPhraseEvent
)
from time import sleep, time


def handle_speaking_phrase(event: SpeakingPhraseEvent):
    print(f"Handling SpeakingPhraseEvent: '{event.text}' for {event.duration} seconds")
    # Implement the event handling logic here


def main():
    client = create_edcopilot_client()  # Factory method for EDCoPilot
    try:
        # Publish an initial action
        client.publish(OpenPanelAction(panelName="activity"))

        while True:
            if not client.pending_events.empty():
                event = client.pending_events.get()
                if isinstance(event, SpeakingPhraseEvent):
                    handle_speaking_phrase(event)
            sleep(0.1)
    except KeyboardInterrupt:
        print("Shutting down client.")
    finally:
        client.close()


if __name__ == "__main__":
    main()
