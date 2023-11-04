import streamlit as st

st.title("Kuliah Praktikum Big Data")
st.write("Arin - Sabtu 4 November 2023")
st.write("# heading 1")
st.write("## heading 2")
st.write("### heading 3")

pilih1 = st.checkbox('YA')
pilih2 = st.checkbox("tidak")

st.write(pilih1)
st.write(pilih2)

makanan = st.radio('Makanan kesukaan', ['Bakso', 'Nasi goreng kimchi', 'Mie ayam'])

minuman = st.selectbox ('Pilih minuman yang akan dipesan', ['Iced americano', 'Mineral water', 'Tea'])

st.write(minuman)
st.write(makanan)

bayar = st.multiselect('Bayar pakai:', ['Cash', 'QRIS', 'Debit'])

st.write(bayar)
