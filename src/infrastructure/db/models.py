from sqlalchemy import Column, Integer, String

from src.infrastructure.engine import Base

class UserModel(Base):
    __tablename__ = "users"

    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False)