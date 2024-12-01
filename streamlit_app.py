import streamlit as st
from datetime import datetime

# Panca Wara
arr_pwara = ['Umanis', 'Pahing', 'Pon', 'Wage', 'Kliwon']

# Judul aplikasi
st.title("Hitung Panca Wara Berdasarkan Tanggal")

# Deskripsi aplikasi
st.write("Aplikasi ini menghitung Wewaran dari suatu tanggal.")

# Input tanggal dari pengguna
tanggal_input = st.text_input("Masukkan tanggal (format: DD/MM/YYYY):")

# Jika input tidak kosong, proses data
if tanggal_input:
    try:
        # Konversi input ke objek datetime
        input_date = datetime.strptime(tanggal_input, "%d/%m/%Y")

        # Tanggal awal
        start_date = datetime(1900, 1, 1)

        # Hitung selisih hari
        delta = (input_date - start_date).days
        pwara = delta % 5

        # Tampilkan hasil
        st.success(f"Jumlah hari dari 01/01/1900 sampai {tanggal_input}: {delta} hari")
        st.info(f"Panca Wara: **{arr_pwara[pwara]}**")
    except ValueError:
        # Jika format tanggal salah
        st.error("Format tanggal salah! Gunakan format DD/MM/YYYY.")
