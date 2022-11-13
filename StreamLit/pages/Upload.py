import streamlit as st
from PIL import Image
import urllib.request 
import tensorflow as tf
import cv2
import numpy as np
import matplotlib.pyplot as plt
shape = 224

SEEDLING_EMOJI_URL = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/facebook/65/seedling_1f331" \
                     ".png "
page_title = "Weed Detector"


# Set page title and favicon.
st.set_page_config(
    page_title=page_title,
    page_icon=SEEDLING_EMOJI_URL
)


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.pexels.com/photos/440731/pexels-photo-440731.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

# Display markdown content
st.markdown(f'<h1 style="color:#000000;font-size:35px;">{"Weed Detech"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#000000;font-size:24px;">{"Witness the magic by simply uploading an image below and let our model do the talking."}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#000000;font-size:18px;">{"Please upload your file below:"}</h1>', unsafe_allow_html=True)

file = st.file_uploader('', type=["jpg", "png"])

def load_model():
    if 'model' not in st.session_state:
        urllib.request.urlretrieve("https://github.com/Shivesh777/weed-detech/releases/download/model-weights/model.h5", "model.h5")
        st.session_state['model'] = tf.keras.models.load_model('model.h5')
    return st.session_state['model']

if file is None:
    pass
else:
    image = cv2.imread(file)
    image = cv2.resize(image, (shape, shape))
    image_1 = np.reshape(image, (1 ,shape, shape, 3))
    pred = load_model().predict(image_1)
    startX = int(pred[1][0][0] * 224)
    startY = int(pred[1][0][1] * 224)
    endX =   int(pred[1][0][2] * 224)
    endY =   int(pred[1][0][3] * 224)
    cv2.rectangle(image, (startX, startY), (endX, endY),(0, 255, 0), 2)
    plt.imshow(image)
