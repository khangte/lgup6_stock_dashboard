import streamlit as st


# Navigation links
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.page_link("19_page.py", label="Home", icon="🏠", disabled=True)
    
with col2:
    st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
    
with col3:
    st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣")
    
with col4:
    st.page_link("http://www.google.com", label="Google", icon="🌎")

st.divider()
st.write("This is Page content")