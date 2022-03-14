from flask_sqlalchemy import SQLAlchemy
import hashlib

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def select(self) -> list:
        return db.session.query(Users).all()
    
    def select_by_email_and_password(self):
        return db.session.query(Users).filter_by(email=self.email, password=self.hash()).first()

    def insert(self) -> bool:
        if not self.select_by_email_and_password():
            self.password = self.hash()
            db.session.add(self)
            db.session.commit()
            return True
        else:
            return False

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def hash(self):
        return hashlib.sha256(self.password.encode('utf-8')).hexdigest()
