import pytest
from pact import Consumer, Provider
import requests

PACT_DIR = "./pacts"  # Directory to store contract files
MOCK_SERVER_URL = "http://localhost:1234"  # Use the Docker mock provider

pact = Consumer("Client").has_pact_with(
    Provider("HelloService"),
    pact_dir=PACT_DIR
)

@pytest.fixture(scope="module")
def pact_setup():
    yield  

def test_hello_world_api(pact_setup):
    expected_response = {"message": "Hello, HPE!"}

    # Define expected interaction
    pact.given("The API is up")\
        .upon_receiving("a request for hello")\
        .with_request("GET", "/hello")\
        .will_respond_with(200, body=expected_response)

    with pact:
        result = requests.get(MOCK_SERVER_URL + "/hello")  # Use the Docker mock provider

    # Assertions
    assert result.status_code == 200
    assert result.json() == expected_response
