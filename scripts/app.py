import streamlit as st
import requests
from PIL import Image
import pandas as pd
from tensorflow.keras.models import load_model
import io


#page_config
st.set_page_config(page_title="Image Prediction App", page_icon=":guardsman:", layout="wide")

# Load the model from GCS
master_model = load_model("gs://auto_tag_old_models/model_master_vgg16")


def main():
    st.title("Upload an image for prediction")
    image_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

    if image_file is not None:
        categorias = {}
        for img in image_file:
            image_pil = Image.open(img) # esto es para trabajar con objetos pillow
            image_name = img.name # esto se encuentra en el objeto de uploded file
            image_category = master_model.predict(image_pil) #usamos la imagen en pillow para la prediccion
            categorias[image_name] = image_category #añadimos una entrada en el diccionario

    excel = pd.DataFrame(categorias)
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        excel.to_excel(writer, sheet_name='Sheet1')
        writer.save()

    st.download_button(
    label="Descagar Excel",
    data=buffer,
    file_name="clasificacion.xlsx",
    mime="application/vnd.ms-excel"
    )

if __name__ == '__main__':
    main()
