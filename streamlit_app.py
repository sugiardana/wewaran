import streamlit as st
from datetime import datetime
import math

# Panca Wara
arr_pwara = ['Pahing', 'Pon', 'Wage', 'Kliwon', 'Umanis']

# Sapta Wara
arr_stwara = ['Soma', 'Anggara', 'Buda', 'Wrespati', 'Sukra', 'Saniscara', 'Redite']

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

        # Tampilkan hasil
        st.success(f"Jumlah hari dari 01/01/1900 sampai {tanggal_input.strftime('%d/%m/%Y')}: {delta} hari")
        st.info(f"Wewaran: **{arr_stwara[stwara]} {arr_pwara[pwara]} {arr_wuku[wuku]} **")
    except Exception as e:
        # Jika terjadi kesalahan
        st.error(f"Terjadi kesalahan: {e}")
