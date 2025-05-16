# from src.application.use_cases.login_user import LoginUserUseCase
# from src.application.use_cases.register_user import RegisterUserUseCase

from src.application.use_cases.auth_case import AuthUseCase
from src.web.views.auth.auth_view import auth_view
from dependency_injector.wiring import inject, Provide
from src.containers import Container, dependency_injector

@dependency_injector
class AuthController:

    @inject
    def __init__(
        self,
        auth_use_case: AuthUseCase = Provide[Container.auth_use_case]
        #login_use_case: LoginUserUseCase = Provide[Container.login_user_use_case],
        #register_use_case: RegisterUserUseCase = Provide[Container.register_user_use_case]
    ):
        self.authenticator = auth_use_case.create_authenticator()

    def execute(self):
        auth_view(self.authenticator)

if __name__ == "__main__":
    AuthController().execute()