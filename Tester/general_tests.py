import pytest
from fastapi.testclient import TestClient
from Summarizer import app

client = TestClient(app)

@pytest.mark.parametrize("endpoint", ["/summarize/", "/compress_summary/"])
def test_invalid_json(endpoint):
    response = client.post(endpoint)
    assert response.status_code == 422  # Expecting Unprocessable Entity status code

def test_summarize():
    # Test valid summarization request
    text = "This is a sample text for summarization."
    response = client.post("/summarize/", json={"text": text})
    assert response.status_code == 200
    assert "Summary" in response.json()
    assert len(response.json()["Summary"]) > 0

    # Test summarization with custom summary length
    response = client.post("/summarize/", json={"text": text, "summary_length": 10})
    assert response.status_code == 200
    assert len(response.json()["Summary"]) == 10

def test_compress_summary():
    # Test valid compression request
    text = "AAAAABBBCCCC"
    response = client.post("/compress_summary/", json={"text": text})
    assert response.status_code == 200
    assert "Compressed_summary" in response.json()
    assert response.json()["Compressed_summary"] == "A5B3C4"

    # Test compression with custom summary length
    response = client.post("/compress_summary/", json={"text": text, "summary_length": 5})
    assert response.status_code == 200
    assert response.json()["Compressed_summary"] == "A5B3C4"

    # Test compression with a text having only one character
    response = client.post("/compress_summary/", json={"text": "A"})
    assert response.status_code == 200
    assert response.json()["Compressed_summary"] == "A1"

    # Test compression with an empty text
    response = client.post("/compress_summary/", json={"text": ""})
    assert response.status_code == 200
    assert response.json()["Compressed_summary"] == ""

    # Test compression with long repeated text
    text = "A" * 1000
    expected_result = "A1000"
    response = client.post("/compress_summary/", json={"text": text})
    assert response.status_code == 200
    assert response.json()["Compressed_summary"] == expected_result

def test_error_handling():
    # Test invalid JSON in request body
    response = client.post("/summarize/", data="invalid_data")
    assert response.status_code == 422  # Expecting Unprocessable Entity status code

    # Test internal server error when the summarizer fails
    with pytest.raises(Exception):
        client.post("/summarize/", json={"text": "invalid_text"})

    # Test internal server error when the compression algorithm fails
    with pytest.raises(Exception):
        client.post("/compress_summary/", json={"text": "invalid_text"})

    # Test handling of invalid endpoint
    response = client.post("/invalid_endpoint/")
    assert response.status_code == 404  # Expecting Not Found status code
