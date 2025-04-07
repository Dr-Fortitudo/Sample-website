import streamlit as st

st.set_page_config(
    page_title="My Streamlit Website",
    layout="wide",
    page_icon="🌐",
)

st.title("🌐 Welcome to My Website")
st.write("Use the buttons to navigate to different pages: Home, About, and Contact.")

# Use session state to track active page
if "page" not in st.session_state:
    st.session_state.page = "Home"

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

# Page content rendering
if st.session_state.page == "Home":
    st.title("🏠 Home Page")
    st.write("Welcome to the homepage of your Streamlit website.")
    st.image("https://plus.unsplash.com/premium_photo-1668017178993-4c8fc9f59872?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", use_container_width=True)

elif st.session_state.page == "About":
    st.title("ℹ️ About Us")
    st.write("We are building a multi-page website in Streamlit using a custom navbar.")
    st.success("This approach allows a more web-like experience in Streamlit!")

elif st.session_state.page == "Contact":
    st.title("📞 Contact Us")
    st.write("Feel free to reach out!")
    name = st.text_input("Your Name")
    msg = st.text_area("Your Message")
    if st.button("Send"):
        st.success(f"Thanks {name}, your message has been sent!")
