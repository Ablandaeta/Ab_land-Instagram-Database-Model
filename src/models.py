from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__= 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    user_name: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    fist_name: Mapped[str] = mapped_column(String(20), nullable=False)
    last_name: Mapped[str] = mapped_column(String(20), nullable=False)
    follows: Mapped[list['Follower']] = relationship(back_populates='follower', cascade = 'all, delete-orphan')
    follow_by: Mapped[list['Follower']] = relationship(back_populates='followed', cascade = 'all, delete-orphan')
    posts: Mapped[list['Post']] = relationship(back_populates='user', cascade = 'all, delete-orphan')
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

class Follower(db.Model):
    __tablename__ = 'follower'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_from_ID: Mapped[int] = mapped_column(ForeignKey("user.id"))
    Follower: Mapped[User] = relationship(back_populates='follows')        
    user_to_ID: Mapped[int] = mapped_column(ForeignKey("user.id"))
    followed: Mapped[User] = relationship(back_populates='follow_by')

class Post(db.Model):
    __tablename__='post'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)   
    user_ID: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped[User] = relationship(back_populates='posts')
    content_media: Mapped[list['Media']]=relationship(back_populates='post', cascade = 'all, delete-orphan')

class Comment(db.Model):
    __tablename__= 'comment'
    id :Mapped[int] = mapped_column(Integer, primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(250),nullable=False)
    autor_ID: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user:Mapped[User]= relationship(back_populates='user')
    post_ID: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post:Mapped[Post]= relationship(back_populates='post')  

class Media(db.Model):
    __tablename__='media'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type:Mapped[int] = mapped_column(Integer, nullable=False)
    url: Mapped[str] = mapped_column(String(50), nullable=False) 
    post_ID: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post : Mapped[Post] = relationship(back_populates='content_media') 




    
