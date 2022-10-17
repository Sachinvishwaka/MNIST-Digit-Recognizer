
import streamlit as st

st.set_page_config(
    page_title="Multipage_app",
    page_icon="None",
    layout="wide"
)
st.title("About MNIST")
# Display Images
 
# import Image from pillow to open images
# import Image from pillow to open images
from PIL import Image
img = Image.open("digit.png")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img, caption="Image of Mnist Digits")



## adding description about mnist digit recognizer


st.markdown("The MNIST database (Modified National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems.The database is also widely used for training and testing in the field of machine learning.")

st.markdown("MNIST is a large database of small, square 28횞28 pixel grayscale images of handwritten single digits between 0 and 9. It consists of a total of 70,000 handwritten images of digits, with the training set having 60,000 images and the test set having 10,000. All images are labeled with the respective digit that they represent. There are a total of 10 classes of digits (from 0 to 9).")

st.markdown(" It is an extremely good database for people who want to try machine learning techniques and pattern recognition methods on real-world data while spending minimal time and effort on data preprocessing and formatting. Its simplicity and ease of use are what make this dataset so widely used and deeply understood. Therefore, the goal of this project is to show you how this dataset can be used in a digits recognition example using Convolutional Neural Network (CNN), which achieves a high classification accuracy on the test dataset.")
