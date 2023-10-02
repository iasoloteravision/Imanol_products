import streamlit as st

st.set_page_config(
    page_title="Code Codix products",
    page_icon="👋",
)

st.success("# Welcome to Code Codix products page! ")

col1, col2, col3 = st.columns(3)

text1 = "ChatBot design, development and maintenance"
text2 = "Web pages design, development and maintenance"
text3 = "Dedicated software (ERPs, SRCs, Web scraping, ETLs)"

col1.success (text1)
col2.warning (text2)
col3.info (text3)

st.warning ("# Used technologies")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.image("python-powered-w-200x80.png",width=120)

with col2:
    st.image("JavaScript-logo.png",width=120)

with col3:
    st.image("botpress-vector-logo.png", width=120)

with col4:
    st.image("streamlit-logo-secondary-colormark-darktext.png", width=120)

with col5:
    st.image("scrapy_logo.png", width=120)

st.error ("more technologies depending project...")




