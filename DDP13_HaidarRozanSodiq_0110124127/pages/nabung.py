import streamlit as st 

st.title("ini halaman Nabung!")

with st.form("nabung"):
    nama= st.text_input("Masukkan nama: ")
    nominal= st.number_input("Masukkan nominal nabung: ")
    submitButton= st.form_submit_button("simpan")

    if submitButton:
        st.write(nama)
        st.session_state["Nabung"].append({
            "Nama": nama,
            "Nominal":nominal,
        })
        st.success("Dana anda sudah masuk")