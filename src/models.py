import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250),  nullable=False)
    password = Column(String(250), nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    follower_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    followed_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship('User')

class Post(Base):
    __tablename__ = 'post'     
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    body = Column(String(250), nullable=False)
    date = Column(Date, nullable=False)
    published = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'),primary_key=True) 
    user = relationship('User')

class Coment(Base):
    __tablename__ = 'coment'     
    id = Column(Integer, primary_key=True)
    text = Column(Text(250),nullable=False)
    date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'),primary_key=True) 
    post_id = Column(Integer, ForeignKey('post.id'),primary_key=True) 
    user = relationship('User')    
    post = relationship('post')    
       
    def to_dict(self):
        return {}

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
