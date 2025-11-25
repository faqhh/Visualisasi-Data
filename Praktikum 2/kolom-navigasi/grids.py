import streamlit as st

st.title("Grids")
st.write("Kelompok: 27")
st.markdown("""
-  Muhammad Nur Faqih (0110122007)
-  Nasywa Dhiya Ulhaq (0110221031)
-  July Ismail (0110221024)
""")

import streamlit as st
from PIL import Image

img = Image.open("../images/kucing2.jpeg")
st.title("Grids")

# Defining no of Rows
for a in range(4):
    # Defining no. of columns with size
    cols = st.columns((1, 1, 1, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)