import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
import streamlit as st

day_df = pd.read_csv("dashboard_dicoding/day_df.csv")
hour_df = pd.read_csv("dashboard_dicoding/hour_df.csv")

min_month = day_df["month"].min()
max_month = day_df["month"].max()

monthly_rentals = day_df.groupby(by='month').sum()
#monthly_rentals    

st.title("Dashboard Analisis Data Bike Sharing")
st.page_link("https://www.linkedin.com/in/yogarusydia/", label="by: Yoga Rusydi Arifin")
st.image(
        "https://back.3blmedia.com/sites/default/files/styles/ratio_3_2/public/triplepundit/wide/BlueBikes%20in%20Boston%20is%20among%20many%20successful%20bike%20share%20programs.png?h=85ee54f6",
        use_column_width="always"
    )

st.subheader("Peforma Jumlah Pelanggan Sepeda Berdasarkan Bulan")
#partOfDay_counts
st.markdown("**Peforma Keseluruhan Pelanggan**")
st.line_chart(
    monthly_rentals['count'],
    x_label='Bulan',
    y_label='Jumlah Pelanggan'
)
st.write("""
Jumlah pelanggan mengalami kenaikan dari bulan ke-1 sampai dengan bulan ke-8. 
Kemudian mengalami penurunan jumlah pelanggan mulai bulan ke-9 sampai dengan 12
""")

st.markdown("**Peforma Pelanggan Kasual vs Terdaftar**")
st.line_chart(
    monthly_rentals,
    y = ["registered", "casual"],
    x_label='Bulan',
    y_label='Jumlah Pelanggan'
)
st.write("""
Jumlah pelanggan terdaftar (registered) mengalami kenaikan mulai dari bulan ke-1 sampai dengan bulan ke-6. Lalu mengalami penurunan
pada bulan ke-7 dan menaik lagi di bulan ke-8. Tetapi setelah itu, mengalami penurunan terus menurus sampai bulan ke-12. Selanjutnya, pada
pelanggan kasual (casual), mengalami kenaikan pelanggan dari bulan ke-1 hingga bulan ke-5. Lalu mengalami sedikit penurunan pada bulan ke-6 dan naik lagi di bulan ke-7.
Tetapi mengalami penurunan kembali pada bulan ke-8 hingga bulan ke-12
""")

day_df['year'] = day_df['year'].map({0: 2011, 1: 2012})
year_rentals = day_df.groupby(by='year').sum()

st.subheader("Perbandingan Jumlah pelanggan Sepeda pada Tahun 2011 dan 2012")
#partOfDay_counts
st.bar_chart(
    year_rentals['count'],
    x_label='Bulan',
    y_label='Jumlah pelanggan'
)
st.write("""
Jumlah pelanggan pada tahun 2012 memiliki perbedaan sangat signifikan
dari jumlah pelanggan pada tahun 2011. Hal ini berarti bisnis mengalami
peningkatan jumlah pelanggan di tahun kedua
""")

st.page_link("Home.py",label="Back to Home")
