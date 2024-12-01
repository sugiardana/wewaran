import streamlit as st
from datetime import datetime

# Judul aplikasi
st.title("Mencari Wewaran")

# Deskripsi aplikasi
st.write("Masukkan tanggal ")

# Input tanggal dari pengguna
tanggal_input = st.text_input("Masukkan tanggal (format: DD/MM/YYYY):")

arr_pwara = ['Umanis','Pahing','Pon','Wage','Kliwon']

if tanggal_input:
    try:
        # Konversi input ke objek datetime
        input_date = datetime.strptime(tanggal_input, "%d/%m/%Y")

        # Tanggal awal
        start_date = datetime(1900, 1, 1)

        # Hitung selisih hari
        delta = (input_date - start_date).days
	pwara = delta % 5
	stwara = delta % 7

        # Tampilkan hasil
        
	st.write(f"{delta} hari")
	st.write(f"index: {pwara}")
        st.write(f"Panca Wara: {arr_pwara[pwara]}")
		
    except ValueError:
        # Jika format input salah
        st.error("Format tanggal salah! Gunakan format DD/MM/YYYY.")
