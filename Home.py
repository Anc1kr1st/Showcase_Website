import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    page="pages/About_Me.py",
    title="About Me",
    default=True,
)

python_page = st.Page(
    page="pages/Python_Portfolio.py",
    title="Python Portfolio",
)

cpp_page = st.Page(
    page="pages/CPP_Portfolio.py",
    title="C++ Portfolio",
)

contact_page = st.Page(
    page="pages/Contact_Us.py",
    title="Contact Me",
)

# --- NAVIGATION SETUP [WITH SECTIONS]  ---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [python_page, cpp_page],
        "Contact": [contact_page]
    }
    )

# --- RUN NAVIGATION  ---
pg.run()