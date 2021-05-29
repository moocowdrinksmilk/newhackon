from sqlalchemy import Table, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///hackon.db')


class UserActivity(Base):
    __tablename__ = 'user_activity'
    user_id = Column(Integer, ForeignKey('user.chat_id'), primary_key = True)
    activity_id = Column(Integer, ForeignKey('activity.id'), primary_key = True)
    reflection = Column(Text)
    activity = relationship("Activity", back_populates= 'users')
    user = relationship("User", back_populates="activities")

class GroupActivity(Base):
    __tablename__ = 'group_activity'
    group_id = Column(Integer, ForeignKey('group.chat_id'), primary_key = True)
    activity_id = Column(Integer, ForeignKey('activity.id'), primary_key = True)
    reflection = Column(Text)
    activity = relationship("Activity", back_populates= 'groups')
    group = relationship("Group", back_populates="activities")

class User(Base):
    __tablename__ = 'user'
    chat_id = Column(Integer, primary_key = True)
    username = Column(String(50))
    set_time = Column(DateTime)
    created_at = Column(DateTime, default = datetime.utcnow)
    activities = relationship("UserActivity", back_populates="user")

    def __repr__(self):
        return f"User(id={self.chat_id!r}, name={self.username!r})"

class Group(Base):
    __tablename__ = 'group'
    chat_id = Column(Integer, primary_key = True)
    set_time = Column(DateTime)
    created_at = Column(DateTime, default = datetime.utcnow)
    activities = relationship("GroupActivity", back_populates="group")
    
    def __repr__(self):
        return f"Group(id={self.chat_id!r}"

class Activity(Base):
    __tablename__ = 'activity'
    id = Column(Integer, primary_key = True)
    title = Column(String(80), nullable = False)
    content = Column(String(120))
    category = Column(String(50))
    prompt = Column(String(120))
    users = relationship("UserActivity", back_populates="activity")
    groups = relationship("GroupActivity", back_populates="activity")
    
    def __repr__(self):
        return f"Activity(title={self.title!r})"


