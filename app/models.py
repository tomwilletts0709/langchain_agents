from sqlalchemy import integer, mapped_column, String
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime, timezone, timedelta

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: int = mapped_column(integer, primary_key=True)
    name: str = mapped_column(String(50))
    created_at: datetime = mapped_column(default=datetime.utcnow)
    updated_at: datetime = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)



class Agent_Response(Base):
    __tablename__ = "agent_responses"

    id: int = mapped_column(integer, primary_key=True)
    response: str = mapped_column(String(500))
    created_at: datetime = mapped_column(default=datetime.utcnow)
    updated_at: datetime = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)


    