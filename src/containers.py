from dependency_injector import containers, providers
from infrastructure.engine import SessionLocal
from infrastructure.db.user_repo_impl import SQLAlchemyUserRepository
from src.application.use_cases.auth_case import AuthUseCase


# from application.use_cases.register_user import RegisterUserUseCase
# from application.use_cases.login_user import LoginUserUseCase

class Container(containers.DeclarativeContainer):
    # wiring_config = containers.WiringConfiguration(
    #     modules=["web.controllers.auth_controller", "web.controllers.dashboard_controller"]
    # )

    _db = providers.Factory(SessionLocal)
    _user_repository = providers.Singleton(SQLAlchemyUserRepository, db=_db)

    # register_user_use_case = providers.Factory(RegisterUserUseCase, user_repo=_user_repository)
    # login_user_use_case = providers.Factory(LoginUserUseCase, user_repo=_user_repository)

    auth_use_case = providers.Factory(AuthUseCase, user_repo=_user_repository)

def dependency_injector(cls):
    container = Container()
    container.wire(modules=[cls.__module__])
    return cls