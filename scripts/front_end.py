import streamlit as st
import requests
from PIL import Image
import pandas as pd
import io

st.set_page_config(page_title="Retail Auto Tagging", page_icon=":guardsman:", layout="wide")


logo_path = "/home/sandorabad/code/Sandorabad/front_auto_tag/scripts/Logotipo de Internet Blanco con Triángulos de Colores.png"
st.image(logo_path, width=200)


def predict_image(image):
    # Add code to send the image to the API and receive a prediction
    api_url = 'http://127.0.0.1:8002/pred/'
    response = requests.post(api_url, files={'file': image})
    return response

def main():
    st.title("Upload a set of images for prediction")
    image_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    if image_file is not None:
        lista_vacia = []
        for img in image_file:


            result = predict_image(img).json()
            result["name_img"] = img.name
            st.success(f"Procesando imagen {img.name}")
            lista_vacia.append(result)

        excel = pd.DataFrame(lista_vacia)

        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            excel.to_excel(writer, sheet_name='Sheet1', index = False)
            writer.save()

        if excel is not None:
            st.download_button(
            label="Download Excel",
            data=buffer,
            file_name="clasificacion.xlsx",
            mime="application/vnd.ms-excel"
            )



if __name__ == '__main__':
    main()
