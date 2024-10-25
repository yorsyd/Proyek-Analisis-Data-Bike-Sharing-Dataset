import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
import streamlit as st

def crt_weather_counts(df):
    weather_counts = df.groupby(by='weathersit').count()
    return weather_counts

def crt_partOfDay_counts(df):
    partOfDay_counts = df.groupby(by='part_of_day').count()
    return partOfDay_counts

def crt_monthly_counts_avg(df):
    monthly_counts_avg = df.groupby("month")[["casual", "registered"]].mean()
    return monthly_counts_avg

day_df = pd.read_csv("/workspaces/Proyek-Analisis-Data-Bike-Sharing-Dataset/dashboard_dicoding/day_df.csv")
hour_df = pd.read_csv("/workspaces/Proyek-Analisis-Data-Bike-Sharing-Dataset/dashboard_dicoding/hour_df.csv")

min_month = day_df["month"].min()
max_month = day_df["month"].max()

monthly_counts_avg = crt_monthly_counts_avg(day_df)
partOfDay_counts = crt_partOfDay_counts(hour_df)
weather_counts = crt_weather_counts(hour_df)

st.title("Dashboard Analisis Data Bike Sharing")
st.page_link("https://www.linkedin.com/in/yogarusydia/", label="by: Yoga Rusydi Arifin")
st.image(
        "https://back.3blmedia.com/sites/default/files/styles/ratio_3_2/public/triplepundit/wide/BlueBikes%20in%20Boston%20is%20among%20many%20successful%20bike%20share%20programs.png?h=85ee54f6",
        use_column_width="always"
    )

st.subheader("Dicuaca Seperti Apa Sepeda Paling Banyak Disewa?")
#weather_counts
st.bar_chart(
    weather_counts['count'], 
    x_label='Kondisi Cuaca', 
    y_label='Jumlah Pengguna', 
    )
st.caption("""Keterangan:
           
1: Clear, Few clouds, Partly cloudy, Partly cloudy | 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
 | 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
 | 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
""")
st.write("""Sepeda lebih banyak disewa pada cuaca kategori 1 yaitu sebanyak 11413 pengguna. Sedangkan pada cuaca
kategori 4 menjadi cuaca dengan pengguna paling sedikit, dengan total hanya 3 pengguna.""")


st.subheader("Kapan Sepeda Paling Sering Disewa? Apakah Siang atau Malam?")
#partOfDay_counts
st.bar_chart(
    partOfDay_counts['count'],
    y_label="Jumlah Pengguna",
    x_label="Bagian Hari"
)
st.write("""Pada siang hari, sepeda paling banyak disewa dengan jumlah 8738 pengguna. 
Sedangkan pada malam hari, terdapat 8641 pengguna sepeda. Kemudian dari visualisasi
tersebut, dapat dilihat bahwa perbedaan antara banyak pengguna pada malam hari
dan siang hari tidak terlalu signifikan.""")

st.subheader("Bagaimana Perbandingan Pengguna Kasual dengan Registered pada Setiap Bulan?")
#monthly_counts_avg
st.bar_chart(
    monthly_counts_avg,
    x_label='Bulan',
    y_label='Jumlah Pengguna',
    stack=False
)
st.write("""Pengguna terdaftar terlihat signifikan lebih banyak menyewa sepeda dibanding
pengguna kasual disetiap bulannya. Berarti, pengguna sepeda kebanyakan adalah pengguna
yang benar-benar membutuhkan jasa ini karena mereka berlangganan dengan jasa tersebut.""")

st.page_link("pages/Analisis Lanjutan.py", label="Go to Analisis Lanjutan")
