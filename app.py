import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image


model = load_model('my_model.h5')



def predict(image):
    img = Image.open(image)
    img = img.resize((220, 220))
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  
    prediction = model.predict(img)
    return prediction

def main():
    st.title('Soil Type Classifier')
    st.text('Upload an image for prediction')

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if st.button('Predict'):
            with st.spinner('Predicting...'):
                prediction = predict(uploaded_file)
                predicted_class = np.argmax(prediction)
                classes = ['Black Soil', 'Cinder Soil', 'Laterite Soil', 'Peat Soil', 'Yellow Soil']
                st.success(f'Predicted Class: {classes[predicted_class]}')
                st.write('Confidence:', round(prediction[0][predicted_class] * 100, 2), '%')

if __name__ == "__main__":
    main()
