import streamlit as st
from PIL import Image
import pandas as pd

# Configuraciones Iniciales de la pagina
st.set_page_config(layout="wide", page_title="AUTO-TAG")

#### Estetica y Detalles --------------------------

# CSS code
CSS = """
/* Body styles */
body {
    font-family: 'Open Sans', sans-serif;
    background-color: #EBDFD3;
    margin: 0;
    padding: 0;
}
/* Title styles */
h1, h2, h3 {
    color: #000000;
    font-weight: 700;
    text-align: center;
}

/* paragraph stiles */
p {
  text-align:center;
  vertical-align: middle;
}

"""

# Incorporamos el codigo CSS dentro de nuestra streamlit App
st.markdown(f'<style>{CSS}</style>', unsafe_allow_html=True)


# Cuerpo Principal, Usando HTML
HTML = """
<div class="container">
    <div class="row">
        <h1 class="title">CATEGORIZAMOS TU PRODUCTOS</h1>
        <p class="subtitle">ORDENA Y CATEGORIZA TUS PRODUCTOS EN SEGUNDOS</p>
    </div>
</div>
"""

# Incorporamos el codigo HTML dentro de nuestra streamlit App
st.markdown(HTML, unsafe_allow_html=True)


#### App y Funcionalidades --------------------------

# Este codigo nos permite remover el texto en ingles deñ st.file_uploader
hide_label = """
<style>
    .css-9ycgxx {
        display: none;
    }
</style>
"""
st.markdown(hide_label, unsafe_allow_html=True)

# Cargamos nuestro modelo / modelos
# model = load_model("path/to/model.h5")

# Seccion destinada a la carga de las imagenes
images = st.file_uploader(type=["jpg"], label= "Arrastra o Selecciona tus Imagenes", label_visibility = "hidden", accept_multiple_files=True)

# Este script permite obtener las caracteristicas de las imagenes.
def get_image_characteristics():
    for image_file in images:
        if image is not None:
            image = Image.open(image_file)

            # obten las caracteristicas de la imagen
            caracteristicas = model.predict(image)

            # convert characteristics to dataframe
            df = pd.DataFrame(caracteristicas)

            # download as excel file
            st.write("Descargar características como archivo excel")
            df.to_excel("Clasificacion_imagenes.xlsx")
            st.success("Descarga Completa.")

get_image_characteristics()
