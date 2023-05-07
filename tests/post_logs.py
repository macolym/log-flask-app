
# This Python code is responsible for sending a log message to a web server using an authenticated API. We will explain each line step by step:

import requests
from datetime import datetime
from tests import post_token

# Gets the authentication token
API_AUTH_TOKEN = post_token.post_token()

# Defines the server URL and authorization header
url = 'http://localhost:5000/add_log'
headers = {'Authorization': f"Bearer {API_AUTH_TOKEN}"}

# Creates the log message
log_message = {
    'system': 'system15',
    'message': 'A new test log.',
    'type': 'info',
    'date': datetime.now().strftime("%d/%m/%Y"),
    'time': datetime.now().strftime("%H:%M:%S")
}

# Sends the log message to the web server
response = requests.post(url, json=log_message, headers=headers)

# Prints the web server's JSON response
print(response.json())
