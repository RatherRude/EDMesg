import pytest
from EDMesg.CovasNext import CovasNextClient, CovasNextProvider
from EDMesg.EDCoPilot import EDCoPilotClient, EDCoPilotProvider

class MockServer:
    """A simple mock server that processes requests."""
    def __init__(self, provider):
        self.provider = provider
        
    def handle_request(self, request):
        return self.provider.process_request(request)

def test_covasnext_integration():
    """Test CovasNext client-provider communication."""
    provider = CovasNextProvider()
    server = MockServer(provider)
    client = CovasNextClient(url="mock://server")
    
    # Patch the client's send method to use our mock server
    original_send = client._send_request
    client._send_request = lambda request: server.handle_request(request)
    
    # Test sending a message
    response = client.send_message("Test integration message")
    assert response is not None
    
    # Restore original method
    client._send_request = original_send

def test_edcopilot_integration():
    """Test EDCoPilot client-provider communication."""
    provider = EDCoPilotProvider()
    server = MockServer(provider)
    client = EDCoPilotClient(url="mock://server")
    
    # Patch the client's send method to use our mock server
    original_send = client._send_request
    client._send_request = lambda request: server.handle_request(request)
    
    # Test sending a command
    response = client.send_command("navigate", {"destination": "Beagle Point"})
    assert response is not None
    
    # Restore original method
    client._send_request = original_send 