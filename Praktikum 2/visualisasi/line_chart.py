import streamlit as st
import pandas as pd
import numpy as np

st.title("Line Chart")
st.write("Kelompok: 27")
st.markdown("""
-  Muhammad Nur Faqih (0110122007)
-  Nasywa Dhiya Ulhaq (0110221031)
-  July Ismail (0110221024)
""")

df = pd.DataFrame(
    np.random.rand(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)

st.line_chart(df)
