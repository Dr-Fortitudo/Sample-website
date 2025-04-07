import streamlit as st

st.set_page_config(
    page_title="My Streamlit Website",
    page_icon="🌐",
)

st.title("🌐 Welcome to My Website")
st.write("Use the sidebar to navigate to different pages: Home, About, and Contact.")

st.markdown("---")
st.subheader("✨ Quick Overview")
st.markdown(
    """
    - 🏠 **Home**: Main landing page  
    - ℹ️ **About**: Learn about this project  
    - 📞 **Contact**: Get in touch with us  
    """
)

st.markdown("---")
st.write("Built with ❤️ using [Streamlit](https://streamlit.io)")
