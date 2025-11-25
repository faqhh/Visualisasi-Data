import streamlit as st

st.title("Empty Containers")
st.write("Kelompok: 27")
st.markdown("""
-  Muhammad Nur Faqih (0110122007)
-  Nasywa Dhiya Ulhaq (0110221031)
-  July Ismail (0110221024)
""")

import streamlit as st
import time

# Empty Container
with st.empty():
    for seconds in range(5):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    
    st.write("✔️ Times up!")