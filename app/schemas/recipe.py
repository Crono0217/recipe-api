from sqlalchemy import Column, Integer, String, Any, Text
from app.db.database import Base


class User(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author_name = Column(String, nullable=False)
    ingredients = Column(Text, nullable=False)
    cook_time = Column(Any, nullable=False)

