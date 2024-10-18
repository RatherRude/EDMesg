from ..EDCoPilot import (
    create_edcopilot_client, 
    OpenPanelAction,
    SpeakingPhraseEvent,
    SpeakThisAction
)
from time import sleep, time

def handle_speaking_phrase(event: SpeakingPhraseEvent):
    print(f"Handling SpeakingPhraseEvent: '{event.text}' for {event.duration} seconds")
    # Implement the event handling logic here

def main():
    client = create_edcopilot_client()  # Factory method for EDCoPilot
    try:
        # Publish an initial action
        client.publish(OpenPanelAction(name="Voice Activity"))
        
        last_action_time = time()
        
        while True:
            current_time = time()
            if current_time - last_action_time >= 10:
                client.publish(SpeakThisAction(text="Hey how are you?"))
                last_action_time = current_time

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