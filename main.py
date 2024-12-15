import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Bogdan Chisu")
    content = """
    Hi, I am Bogdan! I am a Python programmer and FEA engineer. I graduated 
    in 2008. I've worked with companies from various countries, such as 
    Manufactura Moderna de Metales, Ulma Packaging, Emerson and Marelli 
    performing FEA simulation as a member of their NPD teams.
    """
    st.info(content)