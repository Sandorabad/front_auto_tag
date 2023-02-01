

import streamlit as st
import requests
from PIL import Image
import pandas as pd
import io
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Retail Auto Tagging", page_icon=":guardsman:", layout="wide")

logo_path = "scripts/Logotipo de Internet Blanco con Triángulos de Colores.png"
st.image(logo_path, width=200)

def predict_with_cloud_function(image):
    # Encode the image file as a binary string
    image_binary = image.tobytes()

    # Send a POST request to the Google Cloud Function
    response = requests.post('https://<REGION>-<PROJECT_ID>.cloudfunctions.net/predict', data=image_binary)

    # Return the prediction from the response
    return response


def main():
    st.title("Upload a set of images for prediction")
    image_file = st.file_uploader("Choose images", type=["jpg", "png", "jpeg"], accept_multiple_files=True)


    if image_file is not None:
        lista_vacia = []
        flag = False
        button_status = False
        if st.button("Get Tags"):
            button_status = True

        if button_status is True:
            with st.spinner("Processing Images"):
                for img in image_file:

                    result = {}
                    result["Image Id"] = img.name
                    result.update(predict_with_cloud_function(img).json())
                    st.success(f"Processing Image : {img.name}" , icon = "⌛")
                    lista_vacia.append(result)
                    flag = True

            if flag == True:
                st.success("All Images Processed, Ready for Download", icon = "🔥" )

            excel = pd.DataFrame(lista_vacia)

            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                excel.to_excel(writer, sheet_name='Sheet1', index = False)
                writer.save()

            if excel.empty is False:

                st.download_button(
                label="Download Excel",
                data=buffer,
                file_name="clasificacion.xlsx",
                mime="application/vnd.ms-excel"
                )


if __name__ == '__main__':
    main()
