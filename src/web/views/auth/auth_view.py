import streamlit_authenticator as stauth
from streamlit_authenticator import Authenticate

def auth_view(authenticator: Authenticate):
    import streamlit as st

    def login(data):
        st.session_state.logged_in = True
        st.rerun()
    def register(data):
        st.write(data)

    option = st.radio('Escolha uma opção', ('Login', 'Registrar'))
    if option == 'Login':
        authenticator.login('main', key='login', callback=login)

        if st.session_state.authentication_status:
            st.success(f'Bem-vindo(a), 1!')
        elif st.session_state.authentication_status is False:
            st.error('Usuário ou senha incorretos!')
        elif st.session_state.authentication_status is None:
            st.warning('Por favor, insira suas credenciais de login.')
    else:
        try:
            authenticator.register_user('main', key='register', callback=register, merge_username_email=True,
                                        password_hint=False, captcha=False)
        except stauth.utilities.exceptions.RegisterError as e:
            st.error(e)