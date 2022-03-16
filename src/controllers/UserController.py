from flask import render_template
from models.User import db, User
import hash

def index() -> str:
    return render_template('index.html')

def select(email: str, password: str) -> bool:
    result = db.session.query(User).filter_by(email=email, password=hash.sha256_hash(password)).first()

    if result:
        return True
    else:
        return False


def insert(email: str, password: str) -> bool:
    if select(email, password):
        return False
    else:
        db.session.add(User(email=email, password=hash.sha256_hash(password)))
        db.session.commit()
        return True

def remove(id: int):
    result = db.session.query(User).filter_by(id=id).first()

    if result:
        db.session.delete(result)
        db.session.commit()
        return True
    else:
        return False