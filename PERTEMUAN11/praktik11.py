import streamlit as st

st.title("Selamat Datang di Aplikasi data diri saya ")
st.header("Praktik 11 Streamlit")
st.subheader("biodata diri saya")

nama = st.text_input("nama lengkap", max_chars=10)
st.write(f'Nama lengkap saya adalah {nama}')

with st.form("biodata "):
        st.write("Masukkan biodata diri anda")
        nama = st.text_input("Nama Lengkap")
        umur = st.number_input("Umur", min_value=1, max_value=100, step=1)
        alamat = st.text_area("Alamat")
        email = st.text_input("Email")
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Biodata yang anda masukkan:")
            st.write(f"Nama Lengkap: {nama}")
            st.write(f"Umur: {umur}")
            st.write(f"Alamat: {alamat}")
            st.write(f"Email: {email}")