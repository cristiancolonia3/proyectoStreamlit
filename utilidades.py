import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

def generarMenu():
    with st.sidebar:
        col1, col2 =st.columns(2)
        with col1:
            imagen= Image.open("Media/Nacional.png")
            st.image(imagen, use_container_width=False, width=80)
        with col2:
            st.header('Liga BetPlay 2024 - Campeón Atlético Nacional')

        st.page_link('app.py',label='Home',icon='⭐')
        st.page_link('Pages//informe.py',label='Informes',icon='🗳️')#error

