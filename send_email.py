import smtplib, ssl
import streamlit as st
# import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = st.secrets.USERNAME
    password = st.secrets.PASSWORD

    receiver = username
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)