import streamlit as st
import pandas as pd
import numpy as np

st.title('ini adalah aplikasi menghitung molaritas')

bobot=st.number_input('Masukkan nilai bobot')
volume=st.number_input('Masukkan nilai volume')
mr=st.number_input('Masukkan nilai Mr')

tombol=st.button('Hitung nilai molaritas')

if tombol:
    nilai_molaritas=bobot/(mr*volume)
    st.success(f'Nilai molaritas adalah {nilai_molaritas}')