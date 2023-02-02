import streamlit as st
from streamlit import response
import requests
from PIL import Image
import pandas as pd
import io
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(page_title="Retail Auto Tagging", page_icon=":guardsman:", layout="wide")

logo_path = "scripts/Logotipo de Internet Blanco con Triángulos de Colores.png"
st.image(logo_path, width=200)

def predict_image(image):
    # Add code to send the image to the API and receive a prediction
    api_url = 'https://autotagging2-osgbhqumjq-as.a.run.app/pred//'
    response = requests.post(api_url, files={'file': image})
    return response


def download_excel(df):
    # Create a binary stream for the Excel file
    bio = io.BytesIO()
    # Write the DataFrame to the stream
    df.to_excel(bio, index=False)
    # Set the stream position to the beginning
    bio.seek(0)
    # Add headers to trigger a download
    response.set_header("Content-Disposition", "attachment; filename=data.xlsx")
    response.set_header("Content-Type", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    # Return the stream
    return bio.read()


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

            if st.download_button("Download Excel File"):
                st.markdown("""
                ```
                <a href="%s" download>Download Excel File</a>
                ```
                """ % "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64," +
                    str(download_excel(excel).encode("base64"))[2:-1], unsafe_allow_html=True)



if __name__ == '__main__':
    main()
