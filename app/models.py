from app import db

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    system = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(10), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(8), nullable=False)

    def __init__(self, system, message, type, date, time):
        self.system = system
        self.message = message
        self.type = type
        self.date = date
        self.time = time

