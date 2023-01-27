import streamlit as st
import requests
from PIL import Image
import pandas as pd
from tensorflow.keras.models import load_model


def page_config():
    st.set_page_config(page_title="Image Prediction App", page_icon=":guardsman:", layout="wide")

# Load the model from GCS
def load_master_model():
    master_model = load_model("gs://auto_tag_old_models/model_master_vgg16")

# Seccion destinada a la carga de las imagenes
def load_images():
    images = st.file_uploader(type=["jpg"], label= "Arrastra o Selecciona tus Imagenes", label_visibility = "hidden", accept_multiple_files=True)

#if images:
#    for file in images:
#        st.image(file, caption="Imagen cargada", use_column_width=True)
#    st.success("Que lindo!")
#else:
#    st.info("Po favor al menos sube una imagen.")


# Este script permite obtener las caracteristicas de las imagenes.
def get_image_categories():
    """Definimos un diccionario que toma Y retorna los nombres de cada archivo y el objeto PIL de la fotografia"""
    image_categories = {}

    for image_file in images:
        if image_file is not None:

            image_pil = Image.open(image_file) # esto es para trabajar con objetos pillow

            image_name = image_file.name # esto se encuentra en el objeto de uploded file

            image_prediction_master = master_model.predict(image_pil)

            image_categories[image_name] = image_prediction_master


    print(image_categories)
    return image_categories


def main():
    page_config()
    load_master_model
    load_images
    get_image_categories()


if __name__ == '__main__':
    main()
