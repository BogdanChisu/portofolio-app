import streamlit as st

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email adress: ")
    message = st.text_area("Your message")
    button = st.form_submit_button()
    # print(button) # this will return False if the button is not pressed
    if button:
        # print(button) # shows that the button is a boolean type
        print("Submit email button was pressed")
