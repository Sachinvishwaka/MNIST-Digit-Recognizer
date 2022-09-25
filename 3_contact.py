import streamlit as st

st.header("About Myself")
st.markdown("I am sachin vishwakarma,I am a student of RJ college from the department of DATA SCIENCE and ARTIFICIAL INTELLIGENCE. ")
st.markdown("This project is created by me ,with the help of my inspiring mentor prof. MRS ANITA GAIKWAD ,GITHUB is   'https://github.com/Sachinvishwaka/MNIST-digit-recognizer'")

# Display Images
 
# import Image from pillow to open images
from PIL import Image
img = Image.open("digit.png")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img, caption="Image of Mnist Digits")

