import pickle
import streamlit as st

model = pickle.load(open('estimasi_motor3.sav', 'rb'))

st.title('Estimasi Keuntungan Penjualan Motor Di Eropa')

year = st.number_input('Input Tahun Motor')
mileage = st.number_input('Input Biaya Unit')
lot = st.number_input('Input Jumlah Pesanan')

prediksi = ''
if st.button('Estimasi Jumlah Keuntungan'):
    prediksi = model.predict(
        [[year, mileage, lot]]
    )
    st.write('Estimasi Keuntungan penjualan motor di Eropa : ', prediksi)
