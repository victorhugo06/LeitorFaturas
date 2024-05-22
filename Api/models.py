from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fatura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.text, nullable=False)

    def __repr__(self):
        return f'<Id {self.id}>'
