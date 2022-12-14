import numpy as np
import streamlit as st
from PIL import Image

u = "https://storage.googleapis.com/rishit-dagli.appspot.com/My_project-1_1.png"
page_title = "Weed Detech"


# Set page title and favicon.
st.set_page_config(page_title=page_title, page_icon=u)


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.discordapp.com/attachments/1041031247935316030/1041226102548467812/Untitled_presentation_1.png");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True,
    )


add_bg_from_url()

u = "https://storage.googleapis.com/rishit-dagli.appspot.com/My_project-1_1.png"
st.image(u, width=150)


st.markdown(
    f'<h1 style="color:#000000;font-size:35px;">{"Weed Detech"}</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<h1 style="color:#000000;font-size:15px;">{"Spelled as We Detect"}</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<h1 style="color:#000000;font-size:15px;">{"Note: The word weed here refers to unwanted plant growth."}</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<h1 style="color:#000000;font-size:24px;">{"Farmers waste hours scouring fields to find weeds, our model helps them drastically reduce this time. Weed Detech helps farmer detect the position of weed on a field with a single photo click. Our model is trained on over 15000 images and achieves plausible performance."}</h1>',
    unsafe_allow_html=True,
)


# st.button('Try it out!!')
