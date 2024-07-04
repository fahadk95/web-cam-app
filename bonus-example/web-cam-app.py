import streamlit as st
from PIL import Image

# Start the Camera
with st.expander("Start Camera"):
    camera_image = st.camera_input("camera")

# Create a Pillow image
if camera_image:
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.image(gray_img)
