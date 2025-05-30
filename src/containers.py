from dependency_injector import containers, providers
from infrastructure.engine import SessionLocal
from infrastructure.db.user_repo_impl import SQLAlchemyUserRepository
from src.application.use_cases.auth_case import AuthUseCase

class Container(containers.DeclarativeContainer):
    _session = providers.Factory(SessionLocal)
    _user_repository = providers.Singleton(SQLAlchemyUserRepository, session=_session)

    auth_use_case = providers.Factory(AuthUseCase, user_repo=_user_repository)

def dependency_injector(cls):
    container = Container()
    container.wire(modules=[cls.__module__])
    return cls