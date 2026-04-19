import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("fruit_model.h5")

# Class names
class_names = ['Apple','Banana','Grapes','Mango','Strawberry']

# Page settings
st.set_page_config(
page_title="Fruit Classifier",
layout="centered"
)

st.markdown(
"<h1 style='text-align:center;color:#2E8B57;'>🍎 Fruit Classification System</h1>",
unsafe_allow_html=True
)

st.markdown(
"<p style='text-align:center;'>Upload a fruit image to classify</p>",
unsafe_allow_html=True
)

# Upload box
file = st.file_uploader(
"Upload Fruit Image",
type=["jpg","jpeg","png"]
)

if file is not None:

    col1,col2 = st.columns(2)

    with col1:

        image = Image.open(file).convert("RGB")

        st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
        )

    # Preprocess
    img = image.resize((128,128))

    img_array = np.array(img)

    img_array = img_array/255

    img_array = np.expand_dims(img_array,0)

    prediction = model.predict(img_array)

    predicted_class = class_names[np.argmax(prediction)]

    confidence = np.max(prediction)

    with col2:

        st.markdown("### Prediction Result")

        st.success(predicted_class)

        st.metric(
        label="Confidence",
        value=str(round(confidence*100,2))+"%"
        )

    st.markdown("### Probability Distribution")

    for i in range(len(class_names)):

        st.progress(float(prediction[0][i]))

        st.write(
        class_names[i],
        str(round(prediction[0][i]*100,2))+"%"
        )