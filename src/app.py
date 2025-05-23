import streamlit as st

# Base.metadata.create_all(bind=engine)

def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    def logout():
        if st.button("Log out"):
            st.session_state.logged_in = False
            st.rerun()

    auth_page = st.Page("web/controllers/auth_controller.py", url_path="/auth", title="Auth Page", icon="🎈",default=True)
    logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

    home_page = st.Page("web/controllers/home_controller.py", url_path="/home", title="Main Page", icon="🎈")
    dashboard_page = st.Page("web/controllers/dashboard_controller.py", url_path="/dashboard", title="Dashboard Page", icon="❄️")

    if st.session_state.logged_in:
        pg = st.navigation(
            {"Account":[logout_page],"Home": [dashboard_page, home_page]}
        )
    else:
        pg = st.navigation([auth_page])

    pg.run()

if __name__ == "__main__":
    main()
