from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime

event_user = Table('event_user', Base.metadata,
                   Column('user_id', ForeignKey('user.id'), primary_key=True),
                   Column('event_id', ForeignKey('event.id'), primary_key=True)
                   )


class Status(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True)

    name = Column(String)

    active = Column(Boolean, default=True)

    def __repr__(self):
        return self.name


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)

    name = Column(String)

    active = Column(Boolean, default=True)


class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)

    author_id = Column(Integer, ForeignKey('user.id'))

    participants = relationship('User', secondary=event_user)

    author = relationship('User')

    title = Column(String)

    description = Column(String)

    status_id = Column(Integer, ForeignKey('status.id'))

    status = relationship('Status')

    date_created = Column(DateTime(timezone=True), onupdate=datetime.now())

    date_event = Column(DateTime(timezone=True))

    active = Column(Boolean, default=True)

    def __repr__(self):
        return self.title.title()

# Base.metadata.create_all(engine)
