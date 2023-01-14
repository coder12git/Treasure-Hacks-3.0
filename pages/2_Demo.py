import streamlit as st
import tensorflow as tf
import PIL

@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('./model/model.h5')
    return model

st.set_page_config(
    page_title="Alzheimer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Alzheimer's Disease Detection")
st.write("This is a demo of the Alzheimer's Disease Detection app.")

pic = st.file_uploader(
    label="Upload an image",
    type=["jpg", "png", "jpeg"],
    accept_multiple_files=False,
    help="Upload an image of a brain scan to predict the stage of Alzheimer's Disease",
)

if st.button("Predict"):
    if pic is None:
        st.error("Please upload an image file")
    else:
        st.header("Result")
        cols = st.columns([1, 2])
        with cols[0]:
            st.image(pic, caption=pic.name, use_column_width=True)
        with cols[1]:
            model = load_model()
            labels = [
                "Mild Dementia",
                "Moderate Dementia",
                "No Dementia",
                "Very Mild Dementia"
            ]
            with st.spinner("Predicting..."):
                img = PIL.Image.open(pic)
                img = img.convert("RGB")
                img = img.resize((128, 128))
                img = tf.expand_dims(img, axis=0)

                prediction = model.predict(img)
                prediction = tf.nn.softmax(prediction)

                score = tf.reduce_max(prediction)
                score = tf.round(score * 100, 2)

                prediction = tf.argmax(prediction, axis=1)
                prediction = prediction.numpy()[0]

                result = labels[prediction]

                st.write(f"**Prediction**: `{result}`")
                st.write(f"**Confidence**: `{score}%`")
