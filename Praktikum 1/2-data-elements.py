import streamlit as st
import pandas as pd #utk mengelola data dalam bentuk tabel (dataFrame)
import numpy as np #utk membuat numerik acak
import altair as alt #utk membuat chart interaktif

#DataFrame : struktur data berbentuk tabel yg ditampilkan
st.subheader("DataFrame")
df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)
st.dataframe(df) #menampilkan DataFrame


#Highlight nilai minimum
st.subheader("Highlight minimum value di DataFrame")
st.dataframe(df.style.highlight_min(axis=0)) #axis=0 bekerja per kolom


#Tabel statis
st.subheader("tabel statis")
df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)
st.table(df) #menampilkan DataFrame


#Menampilkan Metrics -> komponen angka penting
st.subheader("Metrics")
st.metric(label="Temperature", value="31 C", delta="1.2 C") #Metrics tunggal

#metric ganda
st.subheader("Metrics ganda")
c1,c2,c3 = st.columns(3)
c1.metric("Rainfall", "100 cm", "10cm")
c2.metric(label="Population", value="123 Billions", delta="1 Billions", delta_color="inverse")
c3.metric(label="Customer", value=100, delta=10, delta_color="off")
st.metric(label="Speed", value=None,delta=0)
st.metric("Trees", "91456", "-1132649")


# The write() Function as a Superfuction
st.subheader("SuperFunction")
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10)))
# Definisikan multipel argumen dalam fungsi write 
st.write('Ini adalah Data kita', df, 'Data dalam format dataframe. \n', "\nWrite is Super Function")


# Membuat Diagram
st.subheader("Displaying Chart")
df = pd.DataFrame(
    np.random.randn(10,2),
    columns=['a','b'])
#Mendefinisikan diagram
chart = alt.Chart(df).mark_bar().encode(
    x='a', y='b', tooltip=['a','b'])
#Munculkan diagram dengan fungsi write
st.write(chart)


# MAGIC
st.header("Magic Feature")
st.subheader("Displaying Hitungan with Magic")
#hitungan matematika tanpa mendefinisikan fungsi
"Hitunglah 5 & 4 =", 5+4
#munculkan variabel a dengan value nya
a =5
'a', a

#Markdown dengan MAGIC
st.subheader("Displaying Markdown with Magic")
"""
#Magic Feature
Markdown bekerja tanpa mendefinisikan fungsinya scr eksplisit.
"""

#Data Frame menggunakan MAGIC
st.subheader("Displaying DataFrame with Magic")
df = pd.DataFrame({"col": [1,2]})
'dataframe', df


#MAGIC juga bisa membuat Diagram
import matplotlib.pyplot as plt

st.subheader("Displaying Diagram with Magic")
s = np.random.logistic(10,5,size=5)
chart, ax=plt.subplots()
ax.hist(s, bins=15)
#Magic Chart
"chart", chart


