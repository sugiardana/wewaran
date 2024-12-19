import streamlit as st
from datetime import datetime
import math

# Dwi Wara
arr_dwara = ['Menga', 'Pepet']
# Tri Wara
arr_twara = ['Pasah', 'Beteng', 'Kajeng']
# Catur Wara
arr_cwara = ['Sri', 'Laba', 'Jaya', 'Menala']
# Panca Wara
arr_pwara = ['Pahing', 'Pon', 'Wage', 'Kliwon', 'Umanis']
arr_upwara=[9,7,4,8,5,9]
# Sad Wara
arr_sdwara = ['Tungleh', 'Aryang', 'Urukung', 'Paniron', 'Was','Maulu']
# Sapta Wara
arr_stwara = ['Soma', 'Anggara', 'Buda', 'Wrespati', 'Sukra', 'Saniscara', 'Redite']
arr_ustwara=[4,3,7,8,6,9,5]
# Asta Wara
arr_awara = ['Sri', 'Indra', 'Guru', 'Yama', 'Ludra', 'Brahma', 'Kala', 'Uma']
# Sanga Wara
arr_sgwara = ['Dangu', 'Jangur', 'Gigis', 'Nohan', 'Ogan', 'Erangan', 'Urungan', 'Tulus', 'Dadi']
# Dasa Wara
arr_dswara = ['Pandita', 'Pati', 'Suka', 'Duka', 'Sri', 'Manuh', 'Manusa', 'Eraja', 'Dewa','Raksasa']
# Wuku
arr_wuku = ['Langkir', 'Medangsia', 'Pujut', 'Pahang', 'Krulut', 'Merakih', 'Tambir', 'Medangkungan', 'Matal', 'Uye', 'Menail', 'Prangbakat', 'Bala', 'Ugu', 'Wayang', 'Kelawu', 'Dukut', 'Watugunung', 'Sinta', 'Landep', 'Ukir', 'Kulantir', 'Taulu', 'Gumbreg', 'Wariga', 'Warigadean', 'Julungwangi', 'Sungsang', 'Dungulan', 'Kuningan',]


# Judul aplikasi
st.title("Hitung Wewaran Berdasarkan Tanggal")

# Deskripsi aplikasi
st.write("Aplikasi ini menghitung Wewaran dari suatu tanggal.")

# Input tanggal menggunakan kalender
tanggal_input = st.date_input("Pilih tanggal:", min_value=datetime(1900, 1, 1))

# Jika tanggal dipilih
if tanggal_input:
    try:
        # Konversi input ke datetime
        input_date = datetime.combine(tanggal_input, datetime.min.time())

        # Tanggal awal
        start_date = datetime(1900, 1, 1)

        # Hitung selisih hari
        delta = (input_date - start_date).days
        twara = delta % 3
        cwara = delta % 4
        pwara = delta % 5
        sdwara = delta % 5
        stwara = delta % 7
        awara = delta % 8
        sgwara = delta % 9
        dswara = delta % 10
        wuku = math.floor(((delta + 1) % 210) / 7)
        u_hari = arr_ustwara[stwara] + arr_upwara[pwara]
        e_wara = u_hari % 2
        if e_wara==1:
            nm_e_wara="Luwang"
        else:
            nm_e_wara="-"

        # Tampilkan hasil
        st.info(f"Eka Wara: **{nm_e_wara}**")
        st.info(f"Dwi Wara: **{arr_dwara[e_wara]}**")
        st.info(f"Tri Wara: **{arr_twara[twara]}**")
        st.info(f"Catur Wara: **{arr_cwara[cwara]}**")
        st.info(f"Panca Wara: **{arr_pwara[pwara]}**")
        st.info(f"Sad Wara: **{arr_sdwara[sdwara]}**")
        st.info(f"Sapta Wara: **{arr_stwara[stwara]}**")
        st.info(f"Asta Wara: **{arr_awara[awara]}**")
        st.info(f"Sanga Wara: **{arr_sgwara[sgwara]}**")
        st.info(f"Dasa Wara: **{arr_dswara[dswara]}**")
        st.info(f"Wuku: **{arr_wuku[wuku]}**")
        st.info(f"Urip Hari: **{arr_ustwara[stwara]} + {arr_upwara[pwara]} = {u_hari}**")
    except Exception as e:
        # Jika terjadi kesalahan
        st.error(f"Terjadi kesalahan: {e}")
