import streamlit as st
import pandas

st.header("C++ portfolio")

content3 = """
Below you can find some of the apps I have built in C++. Feel free to contact me!
"""
st.write(content3)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data2.csv", sep=";")

with col3:
    for index, row in df[:3].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images2/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[3:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images2/" + row["image"])
        st.write(f"[Source Code]({row['url']})")