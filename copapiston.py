import streamlit as st
from PIL import Image
import base64
from Pages import Clasificacion_01, Formulario_02, Normas_03, Participantes_05, intro_06, fut_04

pages = {
    "Clasificación": Clasificacion_01,
    "Formulario": Formulario_02,
    "Normas de la Copa Pistón 2024": Normas_03,
    "Piston Champions": fut_04,
    "Participantes": Participantes_05,
    "Sobre la competición": intro_06
}

selection = st.sidebar.radio("Navegación", list(pages.keys()))
page = pages[selection]

# # Render selected page
# if selection == "Normas de la Copa Pistón 2024":
#     car_image_path = "Images/rayo_mcqueen.jpg"
#     car_image_base64 = get_base64_image(car_image_path)
#     st.markdown(
#         f"""
#         <div style="background-image: url('data:image/jpeg;base64,{car_image_base64}'); 
#                     background-size: cover; 
#                     height: 300px; 
#                     display: flex; 
#                     justify-content: center; 
#                     align-items: center;">
#         </div>
#         """, 
#         unsafe_allow_html=True
#     )

page.main()

# Footer
st.markdown("---")
st.write("Creado por Sitges man y editado por Marco. Bebed responsablemente y disfrutad de la experiencia!")