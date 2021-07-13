from todoapp import db
from datetime import datetime

class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(300), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    finished = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"Todo: <{self.data}>\nTask ID: {self.id}"