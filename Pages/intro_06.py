import streamlit as st
from PIL import Image

def main():
    car_image_path = "Images/rayo_mcqueen.jpg"

    st.title("Bienvenidos a la copa Piston! 🍻")
    st.subheader("El juego definitivo del los verdaderos heroes del verano")

    car_image = Image.open(car_image_path)
    st.image(car_image, use_column_width=True)

    # Main Content
    st.markdown("""
    La competición donde solo unos pocos podrán salir victoriosos, pero no les saldrá barato. ¿Quien será nuestro héroe número 1 de la edición 2024?
    """)

    # Game Overview
    st.header("¿Como Funciona?")
    st.markdown("""
    Esta atrevida competición se basa en un sistema de puntos en el cual se decidirán los ganadores en base a quien obtenga más. Pero no será de la noche a la mañana, la competición dura del 03/06/2024 hasta las 8:00h del 15/09/2024.

    Estad atentos para más detalles y preparaos para uno de los veranos más locos de vuestras vidas!
    """)

if __name__ == "__main__":
    main()
