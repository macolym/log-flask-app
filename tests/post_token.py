
# This Python code is responsible for obtaining an authentication token from a web server. We will explain each line step by step:

# The requests, base64 and cryptography libraries are imported.
import requests
import base64
from cryptography.fernet import Fernet
from config import client_secret, username as user, password as pwd

# The post_token() function is defined. The URL of the web server that provides the authentication token is defined.
def post_token():
    url = "http://localhost:5000/token"

    # Generate a secret key and save it for later use, remembering that it must be the same as the server's client_secret
    secret_key = client_secret
    
    # Create a Fernet object with the secret key
    cipher = Fernet(secret_key)
    
    # Replace with your own username and password values
    username = user
    password = pwd
    
    # The user's authentication credentials are defined, encrypted with the secret key, and converted to a base64-encoded string.
    credentials = f"{username}:{password}"
    encrypted_credentials = cipher.encrypt(credentials.encode())
    credentials_base64 = base64.b64encode(encrypted_credentials).decode()
    
    # The base64-encoded credentials are sent to the web server as JSON data in a POST request.
    auth_data = {'credentials': credentials_base64}
    response = requests.post(url, json=auth_data, headers={'Content-Type': 'application/json'})
    
    # If the web server's response is successful (status 200), the authentication token is returned. Otherwise, an error message is printed and None is returned.
    if response.ok:
        token = response.json()['token']
        print("Authentication successful!")
        print(f"Token: {token}")
        return token
    else:
        print("Authentication failed.")
        print(response.text)
        return None
