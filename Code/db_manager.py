import sqlalchemy as db
from sqlalchemy.orm import Session
from db_models import Base, User, Post
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from secure_password import hash_password, check_password

engine = db.create_engine("sqlite:///social_media.sqlite")
session = Session(engine)

def create_user(username, password, email):
    if not session.query(User).filter_by(email=email).first():
        new_user = User(username=username, password=hash_password(password), email=email)
        session.add(new_user)
        session.commit()
        print("User registered")


def login(username, password):
    user = session.query(User).filter_by(username=username).first()
    if not user:
        return False
    return bool(check_password(password, user.password))

def create_post(title, content, code, user_id):
    new_post = Post(title=title, content=content, code=code, user_id=user_id,datetime_posted=datetime.now())
    session.add(new_post)
    session.commit()


