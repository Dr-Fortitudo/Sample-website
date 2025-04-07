import streamlit as st

# Page config
st.set_page_config(page_title="My Streamlit Website", layout="wide")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- Top Navigation Bar ---
st.markdown("## 🌐 My Streamlit Website")

nav1, nav2, nav3 = st.columns([1, 1, 1])
with nav1:
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
with nav2:
    if st.button("ℹ️ About"):
        st.session_state.page = "About"
with nav3:
    if st.button("📞 Contact"):
        st.session_state.page = "Contact"

st.markdown("---")

# --- Page Content Based on Navigation ---
if st.session_state.page == "Home":
    st.header("🏠 Home")
    st.write("Welcome to the homepage of your Streamlit website.")
    st.image("https://source.unsplash.com/800x300/?technology", use_column_width=True)

elif st.session_state.page == "About":
    st.header("ℹ️ About")
    st.write("We are building a modular multi-page Streamlit website with a clean navigation system.")

elif st.session_state.page == "Contact":
    st.header("📞 Contact")
    name = st.text_input("Your Name")
    message = st.text_area("Your Message")
    if st.button("Send"):
        st.success(f"Thank you {name}, your message has been sent!")
