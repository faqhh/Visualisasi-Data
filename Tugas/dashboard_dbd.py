import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Dashboard Analitik DBD",
    layout="wide"
)


st.markdown("""
<style>
.stApp {
    background-color: #0b0f19;
    color: white;
}
h1, h2, h3, h4 {
    color: white;
}
.metric-card {
    background: linear-gradient(145deg, #151a2d, #0b0f19);
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 0 20px rgba(0,0,0,0.4);
}
.metric-value {
    font-size: 32px;
    font-weight: bold;
}
.metric-label {
    color: #9aa4bf;
}
</style>
""", unsafe_allow_html=True)


provinsi_data = {
    "Jawa Barat": 17281,
    "Jawa Timur": 10290,
    "Bali": 6443,
    "Jawa Tengah": 6279,
    "Lampung": 4858,
    "Sulawesi Selatan": 2318,
    "Nusa Tenggara Barat": 2251,
    "Sumatra Utara": 1860,
    "Banten": 1711,
    "Riau": 1668
}

years = [2020, 2021, 2022, 2023, 2024]
months = list(range(1, 13))
genders = ["Laki-laki", "Perempuan"]

rows = []
np.random.seed(42)

for prov, total in provinsi_data.items():
    for year in years:
        for month in months:
            for gender in genders:
                value = int((total / (len(years) * 12 * 2)) * np.random.uniform(0.8, 1.2))
                rows.append([prov, year, month, gender, value])

df = pd.DataFrame(rows, columns=["Provinsi", "Tahun", "Bulan", "Jenis Kelamin", "Jumlah Kasus"])


st.sidebar.header("Filter Data")

selected_year = st.sidebar.multiselect(
    "Pilih Tahun",
    df["Tahun"].unique(),
    default=df["Tahun"].unique()
)

selected_province = st.sidebar.multiselect(
    "Pilih Provinsi",
    df["Provinsi"].unique(),
    default=df["Provinsi"].unique()
)

filtered_df = df[
    (df["Tahun"].isin(selected_year)) &
    (df["Provinsi"].isin(selected_province))
]


st.markdown(
    "<h1 style='text-align:center;'>Tren Penyakit Demam Berdarah Dengue (DBD) di Indonesia</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;color:#9aa4bf;'>Analisis interaktif kasus DBD berdasarkan wilayah, waktu, dan karakteristik demografis</p>",
    unsafe_allow_html=True
)

st.divider()


total_cases = filtered_df["Jumlah Kasus"].sum()
top_prov = filtered_df.groupby("Provinsi")["Jumlah Kasus"].sum().idxmax()
top_year = filtered_df.groupby("Tahun")["Jumlah Kasus"].sum().idxmax()
avg_month = int(filtered_df.groupby("Bulan")["Jumlah Kasus"].sum().mean())

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{total_cases:,}</div>
        <div class="metric-label">Total Kasus DBD</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{top_prov}</div>
        <div class="metric-label">Provinsi dengan Kasus Tertinggi</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{top_year}</div>
        <div class="metric-label">Tahun dengan Kasus Tertinggi</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{avg_month:,}</div>
        <div class="metric-label">Rata-rata Kasus Bulanan</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()


c1, c2, c3 = st.columns(3)

with c1:
    st.subheader(" Tren Kasus DBD Tahunan")
    yearly = filtered_df.groupby("Tahun")["Jumlah Kasus"].sum()
    fig, ax = plt.subplots()
    ax.plot(yearly.index, yearly.values, marker="o")
    st.pyplot(fig)

with c2:
    st.subheader(" Distribusi Jumlah Kasus DBD")
    fig, ax = plt.subplots()
    ax.hist(filtered_df["Jumlah Kasus"], bins=20)
    st.pyplot(fig)

with c3:
    st.subheader(" Proporsi Kasus DBD per Provinsi")
    prov_sum = filtered_df.groupby("Provinsi")["Jumlah Kasus"].sum()
    fig, ax = plt.subplots()
    ax.pie(prov_sum, labels=prov_sum.index, autopct="%1.1f%%")
    st.pyplot(fig)


c4, c5 = st.columns(2)

with c4:
    st.subheader(" Pola Kasus DBD Bulanan")
    month_sum = filtered_df.groupby("Bulan")["Jumlah Kasus"].sum()
    fig, ax = plt.subplots()
    ax.fill_between(month_sum.index, month_sum.values)
    st.pyplot(fig)

with c5:
    st.subheader(" Jumlah Kasus DBD Berdasarkan Jenis Kelamin")
    gender_sum = filtered_df.groupby("Jenis Kelamin")["Jumlah Kasus"].sum()
    fig, ax = plt.subplots()
    gender_sum.plot(kind="bar", ax=ax)
    st.pyplot(fig)


st.subheader(" Tabel Data Kasus DBD")
st.dataframe(filtered_df, use_container_width=True)

st.caption(
    "Catatan: Data merupakan hasil simulasi berbasis data agregat DBD di Indonesia dan digunakan untuk keperluan akademik."
)
