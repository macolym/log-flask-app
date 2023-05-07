from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import computer_names
import os

computer_name = os.getenv('COMPUTERNAME', 'defaultValue')

if computer_name in computer_names:
    dir_principal = os.path.join(r'C:\hipercred_services\app-logs-flask')
    os.makedirs(dir_principal, exist_ok=True)
else:
    dir_principal = os.path.join(os.getcwd())

app = Flask(__name__)
db_path = os.path.join(dir_principal, 'app', 'static', 'db', 'hipercred-logs.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import routes
