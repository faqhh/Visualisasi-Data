import streamlit as st

st.title("Columns")
st.write("Kelompok: 27")
st.markdown("""
 -  Muhammad Nur Faqih (0110122007)
 -  Nasywa Dhiya Ulhaq (0110221031)
 -  July Ismail (0110221024)
""")

# Defining Columns
col1, col2 = st.columns(2)

# Inserting Elements in column 1
col1.write("First Column")
col1.image("../images/kucing1.jpeg")

# Inserting Elements in column 2
col2.write("Second Column")
col2.image("../images/kucing2.jpeg")