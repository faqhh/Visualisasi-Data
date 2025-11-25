import streamlit as st
st.write("Displaying an Images")
# Displaying Image by specifying path
st.image("Images/image1.jpeg")
#Image Courtesy by National Wildlife Federation
st.write("Image Courtesy: National Wildlife Federation")


import streamlit as st

# Image Courtesy
st.write("Diplaying Multiple Images")

# Listing out animal images
animal_images = [
    'Images/kucing1.jpeg',
    'Images/kucing2.jpeg',
    'Images/kucing3.jpeg',
    'Images/kucing4.jpeg',
    'Images/kucing5.jpeg',
]

# Displaying Multiple images with width 150
st.image(animal_images, width=150)

# Image Courtesy
st.write("Image Courtesy: National Wildlife Federation")


import streamlit as st
import base64

# Function to set Image as Background
def add_local_background_image(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())

    st.write("Image Courtesy: National Wildlife Federation")
    st.markdown(
    f""" 
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
   unsafe_allow_html=True
    )

st.write("Background Image")
# Calling Image in function
add_local_background_image('Images/kucing1.jpeg')



import streamlit as st
from PIL import Image

original_image = Image.open("Images/kucing1.jpeg")

# Display Original Image
st.title("Original Image")
st.image(original_image)

# Resizing Image to 600*400
resized_image = original_image.resize((600, 400))

# Displaying Resized Image
st.title("Resized Image")
st.image(resized_image)

