import streamlit as st
import pandas as pd
import numpy as np

st.title("Map")
st.write("Kelompok: 27")
st.markdown("""
-  Muhammad Nur Faqih (0110122007)
-  Nasywa Dhiya Ulhaq (0110221031)
-  July Ismail (0110221024)
""")

df = pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"] 
)

st.map(df)