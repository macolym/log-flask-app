from flask import request, jsonify, url_for, redirect, session
from functools import wraps
from config import jwt_secret
import jwt

JWT_SECRET = jwt_secret

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.is_json:
            # Caso a solicitação seja um JSON (API)
            auth_header = request.headers.get('Authorization')
            if auth_header and auth_header.lower().startswith("bearer "):
                token = auth_header[7:]
            else:
                token = None
        else:
            # Caso a solicitação seja um formulário HTML (Web)
            token = session.get('jwt_token', None)
        if not token:
            if request.is_json:
                return jsonify({'status': 'error', 'message': 'Token ausente.'}), 403
            else:
                return redirect(url_for('login'))
        try:
            decoded = jwt.decode(token, JWT_SECRET, algorithms=["HS512"])
        except jwt.InvalidTokenError:
            if request.is_json:
                return jsonify({'status': 'error', 'message': 'Token inválido.'}), 403
            else:
                return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated
