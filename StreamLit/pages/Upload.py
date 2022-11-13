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



# Cache model and class indices loading
# @st.cache
# def load_model():
#     with open(class_indices_path) as json_file:
#         class_indices = json.load(json_file)

#     model = tf.keras.models.load_model(model_path)
#     return model, class_indices


# Display markdown content
st.markdown(f'<h1 style="color:#000000;font-size:35px;">{"Weed Detech"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#000000;font-size:24px;">{"Witness the magic by simply uploading an image below and let our model do the talking."}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#000000;font-size:18px;">{"Please upload your file below:"}</h1>', unsafe_allow_html=True)



file = st.file_uploader('', type=["jpg", "png"])

if file is None:
    pass
else:
    pass
    # image = Image.open(file)
    # st.image(image, use_column_width=True)

    # image = image.resize((224, 224))
    # image = np.expand_dims(np.asarray(image), axis=0) / 255

    # model, class_indices = load_model()
    # predictions = model(image)

    # class_indices = {v: k for (k, v) in class_indices.items()}
    # predicted_label = str(class_indices[np.argmax(predictions)])
    # species, disease = predicted_label.split("__")

    # st.subheader(f"This leaf is of a {species} plant")
    # if disease == "healthy":
    #     st.subheader("This plant is healthy ✔")
    # else:
    #     disease_name = disease.replace("_", " ")
    #     st.subheader(f"This plant is suffering from {disease_name}")
