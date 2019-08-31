from blog_app import db
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from base import Base,engine

class User(db.Model):
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
