import streamlit as st

st.header("Contact me")

with st.form(key='email'):
    email_id=st.text_input("Your E-mail")
    mes=st.text_area("Enter your message ")
    button=st.form_submit_button("Submit")

