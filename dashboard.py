import streamlit as st
import mysql.connector

if 'authorized' not in st.session_state or not st.session_state.authorized:
    st.session_state.authorized = False
    with st.form("my_form"):
        st.write("Please provide admin credentials:")
        user_name = st.text_input('Name')
        password = st.text_input('Password', type="password")

        submitted = st.form_submit_button("Submit")

    if submitted:
        if user_name == st.secrets.admin and password == st.secrets.password:
            st.session_state.authorized = True
        else:
            st.warning('Wrong credentials!')


if st.session_state.authorized:
    btnFetch = st.button('Fetch data')
    if btnFetch:
        conn = mysql.connector.connect(**st.secrets["tradb"])
        query = "SELECT * FROM `indiciny_transactions`;"
        with conn.cursor() as cursor:
            cursor.execute(query)
            query_result = cursor.fetchall()

    if query_result is not None:
        query_result

