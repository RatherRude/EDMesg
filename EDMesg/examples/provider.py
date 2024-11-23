from EDMesg.base import EDMesgWelcomeAction
from ..EDCoPilot import (
    create_edcopilot_provider,
    SpeakingPhraseEvent,
    OpenPanelAction,
    PrintThisAction,
)
from time import sleep, time


def open_panel(name: str):
    print(f"Opening panel: {name}")
    # Implement the actual panel opening logic here


def main():
    provider = create_edcopilot_provider()  # Factory method for EDCoPilot
    try:
        # Publish an initial event

        last_event_time = time()

        while True:
            current_time = time()
            if current_time - last_event_time >= 5:
                provider.publish(
                    SpeakingPhraseEvent(
                        text="I am talking every 5 second for 3.1 seconds duration",
                        duration=3.1,
                        timestamp="2021-09-01T12:00:00Z",
                        reason="test",
                    )
                )
                last_event_time = current_time

            if not provider.pending_actions.empty():
                action = provider.pending_actions.get()
                if isinstance(action, EDMesgWelcomeAction):
                    print("new client connected")
                if isinstance(action, OpenPanelAction):
                    open_panel(action.name)
                if isinstance(action, PrintThisAction):
                    print("SpeakThis: ", action.text)
            sleep(0.1)
    except KeyboardInterrupt:
        print("Shutting down provider.")
    finally:
        provider.close()


if __name__ == "__main__":
    main()
