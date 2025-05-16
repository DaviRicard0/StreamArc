import bcrypt
from src.domain.entities.user import User
from src.domain.repositories.user_repo import IUserRepository

class RegisterUserUseCase:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def execute(self, name: str, email: str, password: str) -> User:
        if self.user_repo.get_by_email(email):
            raise ValueError("Email already registered.")

        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User(id=None, name=name, email=email, password=hashed)
        return self.user_repo.create(user)
