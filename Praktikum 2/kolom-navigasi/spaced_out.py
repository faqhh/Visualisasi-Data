import streamlit as st

st.title("Spaced-Out Columns")
st.write("Kelompok: 27")
st.markdown("""
-  Muhammad Nur Faqih (0110122007)
-  Nasywa Dhiya Ulhaq (0110221031)
-  July Ismail (0110221024)
""")

from PIL import Image
img = Image.open("../images/kucing1.jpeg")
st.title("Spaced-Out Columns")
# Defining two Rows
for _ in range(2):
    # Defining no. of columns with size
    cols = st.columns((3, 1, 2, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)