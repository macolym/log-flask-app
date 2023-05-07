import os
from app import app, db

def init_db():
    db_path = os.path.join(app.config["SQLALCHEMY_DATABASE_URI"][10:])
    if not os.path.exists(db_path):
        with app.app_context():
            db.create_all()

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)

