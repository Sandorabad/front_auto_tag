import streamlit as st
import requests
from PIL import Image
import pandas as pd
import io
import warnings
warnings.filterwarnings('ignore')
from xlsxwriter

st.set_page_config(page_title="Retail Auto Tagging", page_icon=":guardsman:", layout="wide")

logo_path = "scripts/Logotipo de Internet Blanco con Triángulos de Colores.png"
st.image(logo_path, width=200)

def predict_image(image):
    # Add code to send the image to the API and receive a prediction
    api_url = 'https://autotagging2-osgbhqumjq-as.a.run.app/pred//'
    response = requests.post(api_url, files={'file': image})
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
                    result.update(predict_image(img).json())

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
