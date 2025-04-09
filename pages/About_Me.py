import streamlit as st
import pandas
from PIL import Image
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", initial_sidebar_state="auto")

col1, col2 = st.columns(2, gap="medium")


image = Image.open("images/photo.JPG")
rotated_img = image.rotate(0)
fig = plt.figure()
plt.imshow(rotated_img)
plt.axis("off")

with col1:

    st.pyplot(fig, use_container_width=False)

with col2:
    st.title("Richard Bajan")
    content = """
    Hi, I am Richard! Although I don't have professional experience yet, I have actively worked on personal projects 
    and self-education. During my self-learning, I have gained strong technical skills and practical experience working 
    on personal projects.

    I am looking for an opportunity for a programmer/tester position, where I can utilize my technical knowledge and 
    passion for technology, while continuing to grow in the IT field.
    """
    st.info(content)
