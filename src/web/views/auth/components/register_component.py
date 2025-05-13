from typing import Callable

def register_form(register: Callable):
    import streamlit as st

    with st.form(key='register_form'):
        st.subheader('Register New User')
        first_name = st.text_input('First Name')
        email = st.text_input('Email')
        password = st.text_input('Password', type='password')
        password_repeat = st.text_input('Repeat Password', type='password')
        submit_button = st.form_submit_button('Register')

        if submit_button:
            if password != password_repeat:
                st.error('Passwords do not match')
            else:
                result = register(first_name, email, password)
                if result is not None:
                    st.success('User registered successfully')
                else:
                    st.error('Error registering user. Email may already be in use.')