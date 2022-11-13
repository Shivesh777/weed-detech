import numpy as np
import streamlit as st
from PIL import Image

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




st.markdown(f'<h1 style="color:#000000;font-size:35px;">{"Weed Detech"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#000000;font-size:15px;">{"Note: The word weed here refers to unwanted plant growth."}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#000000;font-size:24px;">{"Farmers waste hours scouring fields to find weeds, our model helps them drastically reduce this time. Weed Detech helps farmer detect the position of weed on a field with a single photo click. Our model is trained on over 15000 images and achieves plausible performance."}</h1>', unsafe_allow_html=True)


# st.button('Try it out!!')

