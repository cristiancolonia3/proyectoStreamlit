import pandas as pd
import utilidades as util
import streamlit as st
from PIL import Image

#Página de presentación o Index
st.set_page_config(
    page_title="Info Liga Colombiana",
    initial_sidebar_state="expanded",
    layout="centered",
    page_icon="✅"
)

#llamando la función
util.generarMenu()

#Estructura de presentación
left_col, center_Col, right_col = st.columns(
    [
        1,4,1
    ],
    vertical_alignment="center"
)

#Edito la columna Central
with center_Col:
    st.title("Informe de la Liga Colombiana 2024 - Nacional Campeón")
    st.write("""
En este espacio se puede mostrar cuál el desempeño de los equipos de fútbol durante la liga Betplat, en el año 2024, segundo semestre.
             
En la página Informes, se puede observar los datos y su análisis.
             """)
    imagen2=Image.open("Media\AtlNal.png")
    st.image(imagen2, use_container_width=True,width=500,caption="Atlético Nacional")