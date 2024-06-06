import streamlit as st
from PIL import Image
import base64
from Pages import Normas_01, Participantes_02, Clasificacion_03, Formulario_04

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        base64_str = base64.b64encode(img_file.read()).decode()
    return base64_str

st.set_page_config(
    page_title="Intro Copa Piston",
    page_icon="🍻🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
pages = {
    "Normas de la Copa Pistón 2024": Normas_01,
    "Participantes": Participantes_02,
    "Clasificación": Clasificacion_03,
    "Formulario": Formulario_04
}

selection = st.sidebar.radio("Navegación", list(pages.keys()))
page = pages[selection]

# Render selected page
if selection == "Normas de la Copa Pistón 2024":
    car_image_path = "Images/rayo_mcqueen.jpg"
    car_image_base64 = get_base64_image(car_image_path)
    st.markdown(
        f"""
        <div style="background-image: url('data:image/jpeg;base64,{car_image_base64}'); 
                    background-size: cover; 
                    height: 300px; 
                    display: flex; 
                    justify-content: center; 
                    align-items: center;">
        </div>
        """, 
        unsafe_allow_html=True
    )

page.main()

# Footer
st.markdown("---")
st.write("Creado por Sitges man y editado por Marco. Bebed responsablemente y disfrutad de la experiencia!")

# Custom CSS
st.markdown(
    """
    <style>
    .stApp {
        color: #ffffff;
    }
    .stApp header {
        background: rgba(0, 0, 0, 0.7);
        padding: 10px;
        border-radius: 10px;
    }
    .stApp footer {
        background: rgba(0, 0, 0, 0.7);
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
