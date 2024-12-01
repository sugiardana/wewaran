import streamlit as st
from datetime import datetime
import math

# Panca Wara
arr_pwara = ['Pahing', 'Pon', 'Wage', 'Kliwon', 'Umanis']
arr_upwara=[9,7,4,8,5,9]

# Sapta Wara
arr_stwara = ['Soma', 'Anggara', 'Buda', 'Wrespati', 'Sukra', 'Saniscara', 'Redite']
arr_ustwara=[4,3,7,8,6,9,5]

# Wuku
arr_wuku = ['Langkir', 'Medangsia', 'Pujut', 'Pahang', 'Krulut', 'Merakih', 'Tambir', 'Medangkungan', 'Matal', 'Uye', 'Menail', 'Prangbakat', 'Bala', 'Ugu', 'Wayang', 'Kelawu', 'Dukut', 'Watugunung', 'Sinta', 'Landep', 'Ukir', 'Kulantir', 'Taulu', 'Gumbreg', 'Wariga', 'Warigadean', 'Julungwangi', 'Sungsang', 'Dungulan', 'Kuningan',]


# Judul aplikasi
st.title("Hitung Panca Wara Berdasarkan Tanggal")

# Deskripsi aplikasi
st.write("Aplikasi ini menghitung Wewaran dari suatu tanggal.")

# Input tanggal menggunakan kalender
tanggal_input = st.date_input("Pilih tanggal:")

# Jika tanggal dipilih
if tanggal_input:
    try:
        # Konversi input ke datetime
        input_date = datetime.combine(tanggal_input, datetime.min.time())

        # Tanggal awal
        start_date = datetime(1900, 1, 1)

        # Hitung selisih hari
        delta = (input_date - start_date).days
        pwara = delta % 5
        stwara = delta % 7
        wuku = math.floor(((delta + 1) % 210) / 7)
        u_hari = arr_ustwara[stwara] + arr_upwara[pwara]

        # Tampilkan hasil
        st.info(f"Wewaran: **{arr_stwara[stwara]} {arr_pwara[pwara]} Wuku {arr_wuku[wuku]} **")
        st.info(f"Urip Hari: **{arr_ustwara[stwara]} + {arr_upwara[pwara]} = {u_hari} **")
    except Exception as e:
        # Jika terjadi kesalahan
        st.error(f"Terjadi kesalahan: {e}")
