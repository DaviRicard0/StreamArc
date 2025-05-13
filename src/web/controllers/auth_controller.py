from src.application.use_cases.login_user import LoginUserUseCase
from src.application.use_cases.register_user import RegisterUserUseCase
from src.web.views.auth.auth_view import auth_view
from dependency_injector.wiring import inject, Provide
from src.containers import Container, dependency_injector

@dependency_injector
class AuthController:

    @inject
    def __init__(
        self,
        login_use_case: LoginUserUseCase = Provide[Container.login_user_use_case],
        register_use_case: RegisterUserUseCase = Provide[Container.register_user_use_case]
    ):
        self.login_use_case = login_use_case
        self.registerUseCase = register_use_case

    def login(self,email:str,password:str):
        return self.login_use_case.execute(email, password)

    def register(self,name: str,email:str,password:str):
        return self.registerUseCase.execute(name, email, password)

    def execute(self):
        auth_view(self.login, self.register)

if __name__ == "__main__":
    AuthController().execute()