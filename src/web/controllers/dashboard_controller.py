from dependency_injector.wiring import inject, Provide
from src.application.use_cases.login_user import LoginUserUseCase
from src.containers import Container, dependency_injector
from src.web.views.dashboard_view import dashboard_view

@dependency_injector
class DashboardController:

    @inject
    def __init__(self):
        pass

    def execute(self):
        dashboard_view()

if __name__ == "__main__":
    DashboardController().execute()