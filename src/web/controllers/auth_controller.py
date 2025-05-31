# from src.application.use_cases.login_user import LoginUserUseCase
# from src.application.use_cases.register_user import RegisterUserUseCase

from src.application.use_cases.auth_case import AuthUseCase
from src.domain.entities.user import User
from src.web.views.auth_view import auth_view
from dependency_injector.wiring import inject, Provide
from src.containers import Container, dependency_injector

@dependency_injector
class AuthController:

    @inject
    def __init__(
        self,
        auth_use_case: AuthUseCase = Provide[Container.auth_use_case]
    ):
        self.register_user = auth_use_case.register_user
        self.authenticator = auth_use_case.create_streamlit_authenticator()

    def register_user(self, name: str, email: str, password: str) -> User | None:
        return self.register_user(name, email, password)

    def execute(self):
        auth_view(self.authenticator, self.register_user)

if __name__ == "__main__":
    AuthController().execute()