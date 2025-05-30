from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from src.infrastructure.engine import Base

class UserModel(Base):
    __tablename__ = "users"

    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)