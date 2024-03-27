import requests

# Set url = your local host address where your containerized application is deployed from docker
url = "http://localhost:8000/summarize/"
# Input the data you'd like to be condensed
data = {
    "text": "This is a long text input that needs to be summarized. The FastAPI service should be able to handle lengthy inputs and generate a coherent summary based on the user-defined summary length...",
    "summary_length": 50
}
# Set up requests to get a response in json format
response = requests.post(url, json=data)
# Print your condensed data in json format to the console
print(response.json())
