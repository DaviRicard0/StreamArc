from typing import Callable

from src.web.views.auth.components.login_component import login_form
from src.web.views.auth.components.register_component import register_form

def auth_view(login: Callable, register: Callable):
    import streamlit as st

    option = st.radio('Escolha uma opção', ('Login', 'Registrar'))
    if option == 'Login':
        login_form(login)
    else:
        register_form(register)

