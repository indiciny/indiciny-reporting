import streamlit as st

with st.form("my_form"):
  st.write("Please provide admin credentials:")
  user_name = st.text_input('Name')
  password = st.text_input('Password',type="password")
  
  submitted = st.form_submit_button("Submit")

if submitted:
  st.write("checking...")
