from db import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func


class New(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
