from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.user import User


class IUserRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[User]:
        """
        Returns all registered users.
        """
        raise NotImplementedError("Method 'get_all' not implemented.")

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        """
        Returns a user by their email, if they exist.

        :param email: The user's email.
        :return: A User instance or None.
        """
        raise NotImplementedError("Method 'get_by_email' not implemented.")

    @abstractmethod
    def create(self, user: User) -> User:
        """
        Creates a new user in the repository.

        :param user: A User instance containing the data to be saved.
        :return: The created user instance (with ID populated, if applicable).
        """
        raise NotImplementedError("Method 'create' not implemented.")
