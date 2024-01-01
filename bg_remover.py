import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
from datetime import datetime

st.set_page_config(layout="wide", page_title="Image Background Remover")

st.markdown("# Background Remover App 🎆")

st.markdown("Effortlessly remove backgrounds with precision. Transform photos instantly. Elevate your visuals with our intuitive Background Remover App!")
st.write("##")


st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_img = buf.getvalue()
    return byte_img


def remove_background(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    current_datetime = datetime.now().date()
    st.sidebar.download_button("Download fixed image", convert_image(fixed), f"{current_datetime}_fixed.png", "image/png")


col1,col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])


if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        remove_background(upload=my_upload)
else:
    remove_background("images/img1.jpg")




# input_path = 'images/img1.jpg'
# output_path = 'output.png'
# input = Image.open(input_path)
# output = remove(input)
# output.save(output_path)