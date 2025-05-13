import bcrypt
from src.domain.repositories.user_repo import IUserRepository

class LoginUserUseCase:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def execute(self, email: str, password: str):
        user = self.user_repo.get_by_email(email)
        if not user:
            return None
        if bcrypt.checkpw(password.encode(), user.password.encode()):
            return user
        return None