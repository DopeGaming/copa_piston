import streamlit as st
from PIL import Image
import base64
import datetime
import streamlit.components.v1 as components
def main():
    car_image_path = "Images/saly.jpg"
    
    def get_base64_image(image_path):
        with open(image_path, "rb") as img_file:
            base64_str = base64.b64encode(img_file.read()).decode()
        return base64_str
    
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

    st.title("Normas de la copa pistón 2024 ⚡🏆")

    st.subheader("Detalles del evento")

    st.write("""
    Esta competición veraniega arranca el lunes día 3 de junio 🗓 a las 8:00h ⏰ y finaliza el 15 🗓 de septiembre a las 8:00 ⏰.
    """)

    st.header("Normas de la Competición")

    st.write("""
    1. **Participación y Premios:**
        - Cada jugador deberá poner 10€ x cabeza.
        - Reparto de premios:
            - 50€ al ganador 🥇
            - 30€ al segundo 🥈
            - 20€ al tercero 🥉
        - El campeón también recibirá un trofeo y una cena gratis patrocinada por los concursantes 🏆🍱💰

    2. **Registro de Puntos:**
        - Cada participante, al finalizar su jornada, deberá poner por el grupo la cantidad de puntos que haya conseguido ese día y el total que lleve para llevar un control de la clasificación 📈📉.
        - Se debe llevar un bloc de notas con el progreso del puntaje para evitar trampas.
        - La honestidad es crucial. En caso de sospecha, se reclamarán evidencias y/o explicaciones de donde han sacado los puntos 🧐📸.

    3. **Normas del Grupo:**
        - Quien no quiera participar, debe abandonar el grupo 🚷.
        - El grupo se usa solo para pasar los puntos. Cualquier otro mensaje (excepto dudas o preguntas sobre puntos) puede resultar en penalización ❌ o descalificación.
        - El jugador descalificado debe abonar su parte del premio económico, trofeo y cena común.

    4. **Sistema de Puntos:**
    """)

    st.subheader("Sistema de Puntos 💯")

    st.markdown("""
    | **Actividad** | **Puntos** |
    |---------------|------------|
    | Cubata        | 3 p        |
    | Chupito       | 1 p        |
    | Cerveza       | 1 p        |
    | Zumito/agua   | 1 p (exclusiva para Joel en ambiente de fiesta) |
    | Llegar a casa a + de las 7:00 | 1 p  |
    | Lio           | 3 p        |
    | Pico          | 2 p        |
    | Sexo novia    | 5 p        |
    | Sexo el resto | 10 p       |
    | Trio          | 15 p       |
    | Pico entre nosotros | -1 p |
    | Menor         | -5 p       |
    | Potar         | -3 p       |
    | Poner cuernos | -15 p      |
    | Drogas duras  | -5 p       |
    | Deporte       | 3 p        |
    | Hacerse a una ex o alguien a quien has querido mucho (preguntar) | DESCALIFICADO DIRECTO |
    """)

    st.markdown("---")
    st.write("**Nota:** La honestidad y el respeto son fundamentales para mantener la integridad de la competición. ¡Disfruten y jueguen limpio!")

if __name__ == "__main__":
    main()
