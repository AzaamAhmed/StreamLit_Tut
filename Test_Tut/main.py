import streamlit as st
import time
import math

st.write("Hello, Azaam Ahmed!")

@st.cache_data
def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.text_area("File Content", content, height=300)
    # Optionally, save uploaded file and use cache
    with open("temp_uploaded.txt", "w", encoding="utf-8") as f:
        f.write(content)
    cached_content = read_file("temp_uploaded.txt")
    st.write("Cached Content Preview:")
    st.text_area("Cached Content", cached_content, height=100)