from typing import List, Optional, Type
from sqlalchemy.orm import Session

from src.domain.entities.user import User
from src.domain.repositories.user_repo import IUserRepository
from src.infrastructure.db.models import UserModel


class SQLAlchemyUserRepository(IUserRepository):
    def __init__(self, session: Session):
        """
        Initializes the repository with a SQLAlchemy session.
        """
        self._session = session

    def get_all(self) -> List[User]:
        """
        Retrieves all users from the database.
        """
        user_rows = self._session.query(UserModel).all()
        return [self._to_domain(user) for user in user_rows]

    def get_by_email(self, email: str) -> Optional[User]:
        """
        Retrieves a user by email if found.
        """
        user_row = self._session.query(UserModel).filter(UserModel.email == email).first()
        return self._to_domain(user_row) if user_row else None

    def create(self, user: User) -> User:
        """
        Persists a new user to the database.
        """
        user_row = UserModel(name=user.name, email=user.email, password=user.password)
        self._session.add(user_row)
        self._session.commit()
        self._session.refresh(user_row)
        return self._to_domain(user_row)

    def _to_domain(self, user_model: UserModel) -> User:
        """
        Converts a UserModel instance to a User domain entity.
        """
        return User(
            id=user_model.id,
            name=user_model.name,
            email=user_model.email,
            password=user_model.password
        )