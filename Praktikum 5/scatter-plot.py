import streamlit as st
import matplotlib.pyplot as plt

# Judul halaman
st.title("Bar Chart")
st.write("Kelompok: 27")
st.markdown("""
            1. Muhammad Nur Faqih (0110122007)
            2. Nasywa Dhiya Ulhaq (0110221031)
            3. July Ismail (0110221024)
            """)

# Data dummy utama
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

# Data tambahan untuk multiple scatter
penjualan_weekdays = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_weekend = [60, 70, 80, 100, 110, 120, 140, 160, 200]

st.title("Visualisasi Hubungan Penjualan Es Krim dengan Suhu")


# 1. Basic Scatter Plot
def basic_scatter():
    st.subheader("1. Basic Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan)
    ax.set_title("Hubungan Penjualan Es Krim dengan Suhu")
    ax.set_xlabel("Suhu (°C)")
    ax.set_ylabel("Penjualan Es Krim")
    st.pyplot(fig)


# 2. Kustomisasi Scatter Plot
def custom_scatter():
    st.subheader("2. Kustomisasi Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='orange', s=100,
               edgecolor='black', alpha=0.7)
    ax.set_title("Hubungan Penjualan Es Krim dengan Suhu")
    ax.set_xlabel("Suhu (°C)")
    ax.set_ylabel("Penjualan Es Krim")
    ax.grid(True)
    st.pyplot(fig)


# 3. Multiple Scatter Plot
def multiple_scatter():
    st.subheader("3. Multiple Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan_weekdays, color="green",
               label="Hari Kerja", s=80)
    ax.scatter(suhu, penjualan_weekend, color="purple",
               label="Akhir Pekan", s=80)
    ax.set_title("Perbandingan Penjualan Weekdays & Weekend")
    ax.set_xlabel("Suhu (°C)")
    ax.set_ylabel("Penjualan")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)


# 4. Scatter Plot 3 Variabel 2D
def scatter_3_variabel():
    st.subheader("4. Analisis Scatter Plot 3 Variabel")

    import pandas as pd
    df = pd.DataFrame({
        "Suhu": suhu,
        "Kelembapan": [60, 65, 70, 75, 80, 85, 90, 95, 100],
        "Penjualan_Cokelat": [50, 60, 70, 90, 100, 110, 130, 150, 180],
        "Penjualan_Vanila": [45, 55, 65, 80, 95, 105, 120, 140, 160],
        "Penjualan_Stroberi": [40, 50, 60, 75, 90, 100, 115, 135, 155]
    })

    jenis_eskrim = st.selectbox(
        "Pilih Jenis Es Krim",
        ["Cokelat", "Vanila", "Stroberi"]
    )

    if jenis_eskrim == "Cokelat":
        penjualan_data = df["Penjualan_Cokelat"]
    elif jenis_eskrim == "Vanila":
        penjualan_data = df["Penjualan_Vanila"]
    else:
        penjualan_data = df["Penjualan_Stroberi"]

    st.subheader("Data Penjualan dan Suhu")
    st.dataframe(df)

    fig, ax = plt.subplots()
    scatter = ax.scatter(df["Suhu"], penjualan_data,
                         c=df["Kelembapan"], s=100,
                         cmap="coolwarm", alpha=0.7)

    ax.set_title(f"Hubungan Penjualan {jenis_eskrim} vs Suhu & Kelembapan")
    ax.set_xlabel("Suhu (°C)")
    ax.set_ylabel(f"Penjualan Es Krim ({jenis_eskrim})")
    fig.colorbar(scatter, label="Kelembapan (%)")

    st.pyplot(fig)

    st.subheader("Analisis Hubungan")
    st.write(
        f"Grafik menunjukkan hubungan antara suhu, kelembapan, "
        f"dan penjualan es krim **{jenis_eskrim}**."
    )


# 5. Scatter Plot 3D
def scatter_3d():
    from mpl_toolkits.mplot3d import Axes3D
    
    st.subheader("5. Scatter Plot 3D")
    
# Data 3 dimensi
    x = suhu
    y = [60, 65, 70, 75, 80, 85, 90, 95, 100]   # Kelembapan
    z = penjualan                               # Penjualan

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z, s=80, c=z, cmap='viridis')

    ax.set_title("3D Scatter Plot: Suhu, Kelembapan, dan Penjualan")
    ax.set_xlabel("Suhu (°C)")
    ax.set_ylabel("Kelembapan (%)")
    ax.set_zlabel("Penjualan")

    st.pyplot(fig)

# Sidebar Routing
option = st.sidebar.selectbox(
    "Pilih jenis visualisasi",
    ["Basic Scatter Plot",
     "Kustomisasi Scatter Plot",
     "Multiple Scatter Plot",
     "Analisis Scatter Plot",
     "3D Scatter Plot"]
)

if option == "Basic Scatter Plot":
    basic_scatter()
elif option == "Kustomisasi Scatter Plot":
    custom_scatter()
elif option == "Multiple Scatter Plot":
    multiple_scatter()
elif option == "Analisis Scatter Plot":
    scatter_3_variabel()
elif option == "3D Scatter Plot":
    scatter_3d()
