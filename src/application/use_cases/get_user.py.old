from src.domain.entities.user import User
from src.domain.repositories.user_repo import IUserRepository

class GetUserUseCase:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def execute(self) -> list[User]:
        return self.user_repo.get()