import streamlit_authenticator as stauth
import streamlit as st
from streamlit_authenticator import Authenticate

def auth_view(authenticator: stauth.Authenticate):
    def login_callback(data):
        st.session_state.logged_in = True
        st.rerun()

    def register_callback(data):
        st.success("Registro realizado com sucesso! Agora você pode fazer login.")
        st.session_state.registered = True
        st.rerun()

    st.title("🔐 Sistema de Autenticação")

    tab_login, tab_register = st.tabs(["🔑 Login", "📝 Registrar"])

    with tab_login:
        st.subheader("Entrar na sua conta")
        with st.spinner("Verificando..."):
            authenticator.login('main', key='login', callback=login_callback)

        if st.session_state.get('authentication_status') is True:
            st.success(f"✅ Bem-vindo(a), {st.session_state.get('name', 'usuário')}!")
        elif st.session_state.get('authentication_status') is False:
            st.error("❌ Usuário ou senha incorretos!")
        elif st.session_state.get('authentication_status') is None:
            st.info("ℹ️ Por favor, insira suas credenciais.")

    with tab_register:
        st.subheader("Criar nova conta")
        try:
            authenticator.register_user(
                'main',
                key='register',
                callback=register_callback,
                merge_username_email=True,
                password_hint=True,
                captcha=True
            )
        except stauth.utilities.exceptions.RegisterError as e:
            st.error(f"Erro ao registrar: {e}")