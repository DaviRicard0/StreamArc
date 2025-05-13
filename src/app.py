import streamlit as st
from infrastructure.engine import engine, Base

Base.metadata.create_all(bind=engine)

def main():
    auth_page = st.Page("web/controllers/auth_controller.py", url_path="/auth", title="Auth Page", icon="🎈",default=True)
    home_page = st.Page("web/controllers/home_controller.py", url_path="/home", title="Main Page", icon="🎈")
    dashboard_page = st.Page("web/controllers/dashboard_controller.py", url_path="/dashboard", title="Dashboard Page", icon="❄️")

    pg = st.navigation(
        [auth_page, dashboard_page, home_page]
    )

    pg.run()

if __name__ == "__main__":
    main()
