import os
import requests
import json

# Load the API key from an environment variable
api_key = os.getenv('CAT_API_KEY')

# Define the headers
headers = {
  "Content-Type": "application/json",
  "x-api-key": api_key
}

# Define the URL and the request options
url = "https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=1"

# Send a GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    result = json.loads(response.content)
    print(result)
else:
    print('error')