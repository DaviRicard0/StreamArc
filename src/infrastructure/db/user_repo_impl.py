from typing import Type

from src.domain.entities.user import User
from src.domain.repositories.user_repo import IUserRepository
from src.infrastructure.db.models import UserModel
from sqlalchemy.orm import Session

class SQLAlchemyUserRepository(IUserRepository):
    def __init__(self, db: Session):
        self.db = db

    def get(self) -> list[Type[UserModel]]:
        return self.db.query(UserModel).all()

    def get_by_email(self, email: str) -> User | None:
        user_row = self.db.query(UserModel).filter(UserModel.email == email).first()
        if not user_row:
            return None

        return User(id=user_row.id, name=user_row.name, email=user_row.email, password=user_row.password)

    def create(self, user: User) -> User:
        user_row = UserModel(name=user.name, email=user.email, password=user.password)
        self.db.add(user_row)
        self.db.commit()
        self.db.refresh(user_row)
        return User(id=user_row.id, name=user_row.name, email=user_row.email, password=user_row.password)