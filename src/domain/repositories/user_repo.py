from src.domain.entities.user import User
from abc import ABC, abstractmethod

class IUserRepository(ABC):
    @abstractmethod
    def get(self) -> list[User]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    def create(self, user: User) -> User:
        pass