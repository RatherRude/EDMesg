import pytest
from EDMesg.EDCoPilot import EDCoPilot, EDCoPilotClient, EDCoPilotProvider

class TestEDCoPilot:
    def test_initialization(self):
        """Test that EDCoPilot can be initialized."""
        copilot = EDCoPilot()
        assert copilot is not None
        
class TestEDCoPilotClient:
    def test_client_initialization(self):
        """Test that EDCoPilotClient can be initialized."""
        client = EDCoPilotClient(url="http://localhost:8001")
        assert client is not None
        assert client.url == "http://localhost:8001"
    
    @pytest.mark.parametrize("message", [
        "Navigate to Alpha Centauri",
        {"destination": "Sagittarius A*", "route": "fastest"},
        ["scan", "system", "bodies"]
    ])
    def test_format_request(self, message):
        """Test request formatting with different message types."""
        client = EDCoPilotClient(url="http://localhost:8001")
        request = client._format_request(message)
        assert request is not None
        assert "command" in request
        
class TestEDCoPilotProvider:
    def test_provider_initialization(self):
        """Test that EDCoPilotProvider can be initialized."""
        provider = EDCoPilotProvider()
        assert provider is not None
    
    def test_process_command(self):
        """Test command processing."""
        provider = EDCoPilotProvider()
        # Mock a request similar to what would come from a client
        request = {"command": "plot route", "params": {"destination": "Sol"}}
        response = provider.process_request(request)
        assert response is not None
        assert "status" in response 