import re
import streamlit_authenticator as stauth
from src.domain.repositories.user_repo import IUserRepository

class AuthUseCase:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def get_credentials(self):
        users = self.user_repo.get()

        emails = [user.email for user in users]
        usernames = [user.name for user in users]
        passwords = [user.password for user in users]

        credentials = {'usernames': {}}

        for index in range(len(emails)):
            credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

        return credentials

    def create_authenticator(self):
        credentials = self.get_credentials()

        return stauth.Authenticate(
            credentials,
            cookie_name="Streamlit",
            cookie_key="abcdef",
            cookie_expiry_days=4
        )