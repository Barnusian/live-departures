import requests
from requests.auth import HTTPBasicAuth

# Replace with your actual API endpoint
API_URL = "https://api.realtimetrains.co.uk/v1/some_endpoint"

# Your credentials
USERNAME = "your_username"
PASSWORD = "your_password"

# Make the API request
response = requests.get(API_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD))

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Convert response to a Python dictionary
    print(data)  # Print the raw data (useful for debugging)
else:
    print(f"Error {response.status_code}: {response.text}")  # Print error message if request fails