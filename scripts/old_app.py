import streamlit as st
from PIL import Image
import requests


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

if images:
    for file in images:
        st.image(file, caption="Imagen cargada", use_column_width=True)
    st.success("Que lindo!")
else:
    st.info("Po favor al menos sube una imagen.")


# Este script permite obtener las caracteristicas de las imagenes.
def get_image_characteristics():
    """Definimos un diccionario que toma Y retorna los nombres de cada archivo y el objeto PIL de la fotografia"""
    images_names_and_pil = {}

    for image_file in images:
        if image_file is not None:
            #image = Image.open(image_file) esto es para trabajar con objetos pillow
            image = image_file #esto se encuentra en el objeto de uploded file
            images_names_and_pil[image_file.name] = image

            # download as excel file
            #st.write("Descargar características como archivo excel")
            #df.to_excel("Clasificacion_imagenes.xlsx")
            #st.success("Descarga Completa.")
    print(images_names_and_pil)
    return images_names_and_pil


def get_prediction(input_data):
    response = requests.post("https://your-model-endpoint.com/predict", json=input_data)
    return response.json()

def main():
    print("a")
    #input_data = {"input": "some input"}
    #rediction = get_prediction(input_data)
    #st.write("Prediction:", prediction)

if __name__ == '__main__':
    main()
    get_image_characteristics()
