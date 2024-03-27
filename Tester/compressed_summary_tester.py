import requests

# Set url = your local host address where your containerized application is deployed from docker
url = "http://localhost:8000/compress_summary/"
# Input the data you'd like to be compressed
data = {
    "text": "This committee meets annually to assess the effectiveness of policies on environmental protection.",
    "summary_length": 50
}
# Set up requests to get a response in json format
response = requests.post(url, json=data)
# Print your compressed data in json format to the console
print(response.json())
