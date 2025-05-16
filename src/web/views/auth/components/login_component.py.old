from typing import Callable

def login_form(login: Callable):
    import streamlit as st
    st.session_state["logged_in"] = 'true'
    with st.form(key='login_form'):
        st.subheader('Log In')
        email = st.text_input('Email')
        password = st.text_input('Password', type='password')
        submit_button = st.form_submit_button('Log In')

        if submit_button:
            user = login(email, password)
            if user is not None:
                st.session_state["logged_in"] = 'true'
                st.success(f'Welcome, {email}!')
            else:
                st.error('Incorrect email or password')