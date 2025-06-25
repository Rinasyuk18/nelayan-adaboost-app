
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load Model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Prediksi Kerentanan Ekonomi Nelayan Kota Kendari")

# Form Input
Jenis_Ikan_Utama = st.selectbox('Jenis Ikan Utama', ['Cakalang', 'Tuna', 'Tongkol', 'Lainnya'])
Produksi_Tahunan = st.number_input('Produksi Tahunan (Ton)', min_value=0.0)
Pendapatan_Rata2 = st.number_input('Pendapatan Rata-rata (Juta/Tahun)', min_value=0.0)
Lama_Berpenghasilan = st.number_input('Lama Berpenghasilan (Tahun)', min_value=0)
Mangrove_Terdegradasi = st.slider('Mangrove Terdegradasi (0.0 - 1.0)', 0.0, 1.0)
Akses_Market = st.slider('Akses Market (0.0 - 1.0)', 0.0, 1.0)
Indeks_Pencemaran = st.slider('Indeks Pencemaran (0.0 - 1.0)', 0.0, 1.0)
Indeks_Reklamasi = st.slider('Indeks Reklamasi (0.0 - 1.0)', 0.0, 1.0)

# Mapping jenis ikan sesuai LabelEncoder saat training
jenis_ikan_mapping = {'Cakalang': 0, 'Tuna': 1, 'Tongkol': 2, 'Lainnya': 3}
Jenis_Ikan_Utama_encoded = jenis_ikan_mapping.get(Jenis_Ikan_Utama, 3)

# Prediksi
if st.button("Prediksi Kerentanan"):
    input_data = np.array([[Jenis_Ikan_Utama_encoded, Produksi_Tahunan, Pendapatan_Rata2,
                            Lama_Berpenghasilan, Mangrove_Terdegradasi, Akses_Market,
                            Indeks_Pencemaran, Indeks_Reklamasi]])
    
    prediksi = model.predict(input_data)
    st.success(f"Tingkat Kerentanan Ekonomi: {prediksi[0]}")
