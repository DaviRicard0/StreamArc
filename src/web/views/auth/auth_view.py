from typing import Callable

import streamlit_authenticator as stauth
import streamlit as st
from streamlit_authenticator import Authenticate

def auth_view(authenticator: stauth.Authenticate, register_user: Callable):
    def login_callback(data):
        st.session_state.logged_in = True
        st.rerun()

    def register_callback(data):
        if register_user(data['new_username'], data['new_email'], data['new_password']) is None:
            st.error("Registration failed. Please try again.")
            st.rerun()
        else:
            st.success("Registration successful! You can now log in.")
            st.session_state.registered = True
            st.rerun()

    st.title("🔐 Authentication System")

    tab_login, tab_register = st.tabs(["🔑 Login", "📝 Register"])

    with tab_login:
        st.subheader("Log in to your account")
        with st.spinner("Verifying..."):
            authenticator.login('main', key='login', callback=login_callback)

        if st.session_state.get('authentication_status') is True:
            st.success(f"✅ Welcome, {st.session_state.get('name', 'user')}!")
        elif st.session_state.get('authentication_status') is False:
            st.error("❌ Incorrect username or password!")
        elif st.session_state.get('authentication_status') is None:
            st.info("ℹ️ Please enter your credentials.")

    with tab_register:
        st.title("Register New User")

        # Coleta as informações do usuário
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        password_repeat = st.text_input("Repeat Password", type="password")

        # Valida se as senhas coincidem
        if password and password_repeat and password != password_repeat:
            st.error("Passwords do not match.")
            return

        if st.button("Register"):
            if name and email and password:
                st.success("User registered successfully.")
            else:
                st.warning("Please fill in all fields.")

        st.subheader("Create a new account")
        try:
            authenticator.register_user(
                'main',
                key='register',
                callback=register_callback,
                merge_username_email=True,
                password_hint=False,
                captcha=False
            )
        except stauth.utilities.exceptions.RegisterError as e:
            st.error(f"Registration error: {e}")