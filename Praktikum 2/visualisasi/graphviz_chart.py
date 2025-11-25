import streamlit as st


st.title("Graphviz Chart")
st.write("Kelompok: 27")
st.markdown("""
- Muhammad Nur Faqih (0110122007)
- Nasywa Dhiya Ulhaq (0110221031)
- July Ismail (0110221024)
""")

st.graphviz_chart("""
    digraph {
        "Training Data" -> "ML Algorithm";
        "ML Algorithm" -> "Model";
        "Model" -> "Results Forecasting";
        "New Data" -> "Model";
    }
""")

