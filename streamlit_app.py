import streamlit as st
from datetime import datetime

# Panca Wara
arr_pwara = ['Umanis', 'Pahing', 'Pon', 'Wage', 'Kliwon']

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

        # Tampilkan hasil
        st.success(f"Jumlah hari dari 01/01/1900 sampai {tanggal_input.strftime('%d/%m/%Y')}: {delta} hari")
        st.info(f"Panca Wara: **{arr_pwara[pwara]}**")
    except Exception as e:
        # Jika terjadi kesalahan
        st.error(f"Terjadi kesalahan: {e}")
