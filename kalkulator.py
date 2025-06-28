
import streamlit as st

st.title("🧮 Kalkulator Sederhana")

a = st.number_input("Masukkan angka pertama", format="%.2f")
b = st.number_input("Masukkan angka kedua", format="%.2f")
operasi = st.selectbox("Pilih operasi", ["Tambah", "Kurang", "Kali", "Bagi"])

if st.button("Hitung"):
    if operasi == "Tambah":
        hasil = a + b
    elif operasi == "Kurang":
        hasil = a - b
    elif operasi == "Kali":
        hasil = a * b
    elif operasi == "Bagi":
        if b == 0:
            hasil = "❌ Tidak bisa dibagi 0"
        else:
            hasil = a / b
    st.write("Hasil:", hasil)
