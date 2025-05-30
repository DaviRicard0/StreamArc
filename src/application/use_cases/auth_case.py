import bcrypt
import streamlit_authenticator as stauth

from src.domain.entities.user import User
from src.domain.repositories.user_repo import IUserRepository

class AuthUseCase:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def register_user(self, name: str, email: str, password: str) -> User:
        """
        Registers a new user in the system with an encrypted password.
        """
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User(id=None, name=name, email=email, password=hashed_password)
        return self.user_repo.create(new_user)

    def create_streamlit_authenticator(self) -> stauth.Authenticate:
        """
        Creates a configured instance of streamlit_authenticator.
        """
        credentials = self._build_authenticator_credentials()

        return stauth.Authenticate(
            credentials=credentials,
            cookie_name="Streamlit",
            cookie_key="abcdef",
            cookie_expiry_days=4
        )

    def _build_authenticator_credentials(self) -> dict:
        """
        (Private) Builds the credentials in the format expected by streamlit_authenticator.
        """
        users = self.user_repo.get_all()
        credentials = {'usernames': {}}

        for user in users:
            credentials['usernames'][user.name] = {
                'name': user.email,
                'password': user.password
            }

        return credentials