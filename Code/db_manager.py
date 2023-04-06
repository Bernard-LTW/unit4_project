import sqlalchemy as db
from sqlalchemy.orm import Session
from db_models import Base, Users, Post
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from secure_password import hash_password, check_password



class DBHandler:
    def __init__(self,path):
        self.engine = db.create_engine(path, echo=False)
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

    def create_post(self,title, content, code, language, username):
        user = self.session.query(Users).filter_by(username=username).first()
        new_post = Post(title=title, content=content, code=code, user_id=user.id,datetime_posted=datetime.now(),code_language=language)
        self.session.add(new_post)
        self.session.commit()

    def get_users(self):
        return self.session.query(Users).all()

    def get_posts(self):
        return self.session.query(Post).all().reverse()

    def get_own_posts(self, username):
        user = self.session.query(Users).filter_by(username=username).first()
        print(f"selecting posts from user {user.username} with id {user.id}")
        posts = self.session.query(Post).filter_by(user_id=user.id).all()
        print(f"posts: {posts[0].code}")
        for post in posts:
            post.username = user.username
            post.datetime_posted = post.datetime_posted.strftime("%d/%m/%Y %H:%M")
        posts.reverse()
        return posts

    def delete_post(self, post_id):
        post = self.session.query(Post).filter_by(id=post_id).first()
        self.session.delete(post)
        self.session.commit()
        return


