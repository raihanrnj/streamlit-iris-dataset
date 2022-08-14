# CALCULATOR SEDERHANA
import streamlit as st

st.title("Contoh Program Kalkulator penjumlahan")

st.write("""

  # Contoh Program Kalkulator penjumlahan

  Yuk tengok

  """)

bil1 = st.number_input("Masukkan angka pertama", 0)
bil2 = st.number_input("Masukkan angka kedua", 0)
hitung = st.button("Hitung Penjumlahan")

if hitung:
  total = bil1 + bil2
  st.success(f"Hasil Penjumlahan adalah : {total}")
  st.balloons()
