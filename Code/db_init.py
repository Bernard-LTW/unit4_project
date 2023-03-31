import sqlalchemy as db
from db_models import Base, User, Post
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from db_manager import create_user, create_post
from secure_password import hash_password, check_password

engine = db.create_engine("sqlite:///social_media.sqlite")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session = Session(engine)

def dummy_insert_user():
    users = ["alice123", "bob123"]
    passwords = ["alice123", "bob123"]
    emails = ["alice.doe@company.com","bob.doe@company.com"]
    for user, password, email in zip(users, passwords, emails):
        new_user = User(username=user, password=hash_password(password), email=email)
        session.add(new_user)
    session.commit()

def dummy_insert_post():
    titles = ["First Post", "Second Post"]
    contents = ["This is my first post", "This is my second post"]
    codes = ["print('Hello World')", "print('Hello World')"]
    user_ids = [1, 2]
    for title, content, code, user_id in zip(titles, contents, codes, user_ids):
        new_post = Post(title=title, content=content, code=code, user_id=user_id)
        session.add(new_post)
    session.commit()

dummy_insert_user()
dummy_insert_post()


