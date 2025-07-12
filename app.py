import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="Hapus Background", layout="centered")

st.title("🧼 Hapus Background Gambar")

uploaded_file = st.file_uploader("Upload gambar...", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar Asli", use_column_width=True)

    if st.button("Hapus Background"):
        input_bytes = uploaded_file.read()
        output_bytes = remove(input_bytes)
        output_image = Image.open(io.BytesIO(output_bytes))

        st.image(output_image, caption="Tanpa Background", use_column_width=True)
        st.download_button("⬇️ Download Hasil", output_bytes, file_name="hasil.png", mime="image/png")
