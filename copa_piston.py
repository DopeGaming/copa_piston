import streamlit as st
from PIL import Image
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        base64_str = base64.b64encode(img_file.read()).decode()
    return base64_str

st.set_page_config(
    page_title="Intro Copa Piston",
    page_icon="🍻🚗",
    layout="centered",
    initial_sidebar_state="expanded"
)

car_image_path = "C:/Users/Marco/Desktop/Data For Change/copa_piston/Images/rayo_mcqueen.jpg"

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

#Title
st.title("Bienvenidos a la copa Piston! 🍻🚗")
st.subheader("El juego definitivo del los verdaderos heroes del verano")

# Introduction text
st.markdown("""
<style>
.justified-text {
    text-align: justify;
    text-justify: inter-word;
}
</style>
<div class="justified-text">
    La competición donde solo unos pocos podrán salir victoriosos, pero no les saldrá barato. ¿Quien será nuestro héroe número 1 de la edición 2024?
</div>
""", unsafe_allow_html=True)

# Game overview
st.header("¿Como Funciona?")
st.markdown("""
<div class="justified-text">
            
Esta atrevida competición se basa en un sistema de puntos en el cual se decidiran los ganadores en base a a quien obtenga más. 
Pero no sera de la noche a la mañana, la competición dura del 03/06/2024 hasta las 8:00h del 15/09/2024. 

Estad atentos para más detalles y preparaos para uno de los veranos más locos de vuestras vidas!

</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("Creado por Sitges man y editado por Marco. Bebed responsablemente y disfrutad de la experiencia!")

# Custom CSS for additional styling
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
