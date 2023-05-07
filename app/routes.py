from flask import render_template, request, jsonify, url_for, redirect, session
from app.utils import token_required, JWT_SECRET
from getmac import get_mac_address
from datetime import datetime, timedelta
import jwt
from functools import wraps
from cryptography.fernet import Fernet
import base64
from app.models import Log
from app import app, db
from config import client_secret, secret_key, username as user, password as pwd

CLIENT_SECRET = client_secret
app.secret_key = secret_key

@app.route('/')
def get_mac_address_from_ip2ww  ():
    return redirect(url_for('show_logs'))

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.pop('jwt_token', None)
    return redirect(url_for('login'))

@app.route('/systems')
def get_systems():
    systems = db.session.query(Log.system).distinct().order_by(Log.system).all()
    systems_list = [system[0] for system in systems]
    return jsonify(systems_list)

@app.route('/token', methods=['POST'])
def authenticate():
    if request.is_json:
        # Caso a solicitação seja um JSON
        auth_data = request.json
        credentials_base64 = auth_data.get('credentials')
    else:
        # Caso a solicitação seja um formulário HTML
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        if not username or not password:
            return render_template('login.html', error_message='Preencha todos os campos.')
        else:
            credentials = f"{username}:{password}"
            cipher = Fernet(CLIENT_SECRET)
            encrypted_credentials = cipher.encrypt(credentials.encode())
            credentials_base64 = base64.b64encode(encrypted_credentials).decode()

    try:
        encrypted_credentials = base64.b64decode(credentials_base64.encode())
        cipher = Fernet(CLIENT_SECRET)
        credentials = cipher.decrypt(encrypted_credentials).decode()
        username, password = credentials.split(':')
    except Exception:
        return jsonify({'status': 'error', 'message': 'Credenciais inválidas.'}), 401

    if username == user and password == pwd:
        payload = {
            'user': username,
            'exp': datetime.utcnow() + timedelta(hours=1)
        }
        jwt_token = jwt.encode(payload, JWT_SECRET, algorithm='HS512')
        
        if request.is_json:
            return jsonify({'status': 'success', 'token': jwt_token})
        else:
            # Se a solicitação vier do formulário HTML, redirecione para uma página diferente
            session['jwt_token'] = jwt_token # Armazene o token na sessão
            return redirect(url_for('show_logs'))
    else:
        if request.is_json:
            return jsonify({'status': 'error', 'message': 'Credenciais inválidas.'}), 401
        else:
            # Caso a solicitação venha do formulário HTML, exiba uma mensagem de erro na mesma página
            return render_template('login.html', error_message='Credenciais inválidas.')

@app.route('/add_log', methods=['POST'])
@token_required
def add_log():
    log_data = request.json
    new_log = Log(system=log_data['system'], message=log_data['message'], type=log_data['type'], date=log_data['date'], time=log_data['time'])
    db.session.add(new_log)
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Log adicionado com sucesso.'}), 201

@app.route('/logs')
@token_required
def show_logs():
    selected_systems = request.args.getlist('systems')
    session_selected_systems = session.get('selected_systems', [])  # usa a lista armazenada na sessão ou uma lista vazia

    if len(selected_systems) == 0:
        selected_systems = session_selected_systems
    else:
        session['selected_systems'] = selected_systems

    if len(selected_systems) == 0:
        logs_to_show = Log.query.all()
    else:
        logs_to_show = Log.query.filter(Log.system.in_(selected_systems)).all()

    return render_template('logs.html', logs=logs_to_show, datetime=datetime)
