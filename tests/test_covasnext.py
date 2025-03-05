import pytest
from EDMesg.CovasNext import CovasNext, CovasNextClient, CovasNextProvider

class TestCovasNext:
    def test_initialization(self):
        """Test that CovasNext can be initialized."""
        covas = CovasNext()
        assert covas is not None
        
class TestCovasNextClient:
    def test_client_initialization(self):
        """Test that CovasNextClient can be initialized."""
        client = CovasNextClient(url="http://localhost:8000")
        assert client is not None
        assert client.url == "http://localhost:8000"
    
    @pytest.mark.parametrize("message", [
        "Test message",
        {"key": "value"},
        [1, 2, 3]
    ])
    def test_format_request(self, message):
        """Test request formatting with different message types."""
        client = CovasNextClient(url="http://localhost:8000")
        request = client._format_request(message)
        assert request is not None
        assert "message" in request
        
class TestCovasNextProvider:
    def test_provider_initialization(self):
        """Test that CovasNextProvider can be initialized."""
        provider = CovasNextProvider()
        assert provider is not None
    
    def test_process_request(self):
        """Test request processing."""
        provider = CovasNextProvider()
        # Mock a request similar to what would come from a client
        request = {"message": "Test message"}
        response = provider.process_request(request)
        assert response is not None 