import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página para que ocupe todo el ancho
st.set_page_config(
    page_title="Gestion ARSOF",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ocultar el menú de hamburguesa y el footer de Streamlit para que parezca una app nativa
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
}
iframe {
    width: 100%;
    /* Ajusta esto si necesitas más altura en móviles */
    height: 100vh; 
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Leer el archivo HTML
with open("index.html", "r", encoding='utf-8') as f:
    html_code = f.read()

# Renderizar el HTML
# height=850 asegura que quepa en la mayoría de pantallas sin doble scroll
components.html(html_code, height=850, scrolling=True)
