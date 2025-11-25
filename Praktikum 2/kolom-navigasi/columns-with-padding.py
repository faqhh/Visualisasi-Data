import streamlit as st

st.title("Columns With Padding")
st.write("Kelompok: 27")
st.markdown("""
 -  Muhammad Nur Faqih (0110122007)
 -  Nasywa Dhiya Ulhaq (0110221031)
 -  July Ismail (0110221024)
""")

from PIL import Image
img = Image.open("../images/kucing2.jpeg")
st.title("Padding")

# Defining Padding with columns
col1, padding, col2 = st.columns((10, 2, 10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)