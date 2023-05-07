import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USER").lower()
password = os.getenv("PASSWORD")
computer_names = list(os.getenv("COMPUTER_NAME").split(","))
jwt_secret = os.getenv("JWT_SECRET")
client_secret = os.getenv("CLIENT_SECRET")
secret_key = os.getenv("SECRET_KEY")
