import pytest
from multiprocessing import Process
from time import sleep
from queue import Empty

from EDMesg.examples.provider import create_edcopilot_provider
from EDMesg.examples.client import create_edcopilot_client
from EDMesg.EDCoPilot import SpeakingPhraseEvent

def test_basic_communication():
    # Start provider in a separate process
    provider = create_edcopilot_provider()
    
    # Create a client
    client = create_edcopilot_client()
    
    try:
        # Wait for connection to establish
        sleep(0.5)
        
        # Provider publishes an event
        test_text = "Test message"
        provider.publish(
            SpeakingPhraseEvent(
                text=test_text,
                duration=1.0,
                timestamp="2024-03-14T12:00:00Z",
                reason="test"
            )
        )
        
        # Wait for message propagation
        sleep(0.5)
        
        # Client should receive the event
        try:
            event = client.pending_events.get(timeout=1)
            assert isinstance(event, SpeakingPhraseEvent)
            assert event.text == test_text
            assert event.duration == 1.0
        except Empty:
            pytest.fail("No event received from provider")
            
    finally:
        client.close()
        provider.close() 