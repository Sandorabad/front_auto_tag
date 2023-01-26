import streamlit as st
import requests
from PIL import Image
import pandas as pd

st.set_page_config(page_title="Image Prediction App", page_icon=":guardsman:", layout="wide")

def predict_image(image):
    # Add code to send the image to the API and receive a prediction
    api_url = 'http://127.0.0.1:8002/pred/'
    response = requests.post(api_url, files={'file': image})
    return response

def main():
    st.title("Upload an image for prediction")
    image_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    if image_file is not None:
        lista_vacia = []
        for img in image_file:

        #image__ = Image.open(image_file)
        #st.image(image, caption='Uploaded Image.', use_column_width=True)
            result = predict_image(img)
            st.success(result.text)
            lista_vacia.append(result.text)
        print(lista_vacia)
        excel = pd.DataFrame(lista_vacia).to_excel
        if excel is not None:
            st.download_button("Download csv ", excel)

if __name__ == '__main__':
    main()
