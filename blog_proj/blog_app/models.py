from blog_app import db
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from base import Base,engine
from blog_app import login
from flask_login import UserMixin

@login.user_loader
def user_loader(id):
    return User.query.get(int(id))


class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id=Column(Integer,primary_key=True)
    username=Column(String(64),index=True , unique=True)
    email=Column(String(120),index=True , unique=True)
    post=relationship('Post',backref='author',lazy='dynamic')
    password_hash=Column(String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def __init__(self,username,email,password):
         self.username=username
         self.email=email
         self.password_hash=hash(password)
    def check_password(self,passw):
        if hash(passw) == self.password_hash :
            return True
        
        return False




class Post(db.Model):
    __tablename__='post'
    id=Column(Integer,primary_key=True)
    title=Column(String(130))
    body=Column(String(255))
    timestamp=Column(DateTime,index=True,default=datetime.utcnow)
    user_id=Column(Integer,ForeignKey('user.id'))
    def __repr__(self):
        return '<Post> {}'.format(self.body)

    def __init__(self,title,body,user_id):
        self.titile=title
        self.body=body
        self.timestamp=datetime.utcnow()
        self.user_id=user_id
        





Base.metadata.create_all(engine)
