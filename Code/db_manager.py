import sqlalchemy as db
from sqlalchemy.orm import Session
from db_models import Base, Users, Post
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from secure_password import hash_password, check_password



class DBHandler:
    def __init__(self,path):
        self.engine = db.create_engine(path, echo=True)
        self.session = Session(self.engine)
    def create_user(self,username, password):
        if not self.session.query(Users).filter_by(username=username).first():
            new_user = Users(username=username, password=hash_password(password))
            self.session.add(new_user)
            self.session.commit()
            print("User registered")
            return True
        else: return False

    def check_user(self,username):
        return bool(self.session.query(Users).filter_by(username=username).first())


    def login(self,username, password):
        user = self.session.query(Users).filter_by(username=username).first()
        if not user:
            return False
        return bool(check_password(password, user.password))

    def create_post(self,title, content, code, user_id):
        new_post = Post(title=title, content=content, code=code, user_id=user_id,datetime_posted=datetime.now())
        self.session.add(new_post)
        self.session.commit()

    def get_users(self):
        return self.session.query(Users).all()


