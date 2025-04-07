import streamlit as st

st.set_page_config(
    page_title="My Streamlit Website",
    layout="wide",
    page_icon="🌐",
)

st.title("🌐 Welcome to My Website")
st.write("Use the sidebar to navigate to different pages: Home, About, and Contact.")

# CSS styling for top navigation bar
st.markdown("""
    <style>
    .navbar {
        display: flex;
        justify-content: center;
        gap: 2rem;
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        font-size: 18px;
    }
    .navbar button {
        border: none;
        background: none;
        cursor: pointer;
        font-weight: bold;
        padding: 0.5rem 1rem;
        color: #31333f;
    }
    .navbar button:hover {
        background-color: #d0d3d8;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for consistent layout
st.sidebar.title("Navigation")

# Use session state to track active page
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Navbar buttons
st.markdown('<div class="navbar">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
with col2:
    if st.button("ℹ️ About"):
        st.session_state.page = "About"
with col3:
    if st.button("📞 Contact"):
        st.session_state.page = "Contact"
st.markdown('</div>', unsafe_allow_html=True)

# Page content rendering
if st.session_state.page == "Home":
    st.title("🏠 Home Page")
    st.write("Welcome to the homepage of your Streamlit website.")
    st.image("https://source.unsplash.com/800x300/?home,nature", use_column_width=True)

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
