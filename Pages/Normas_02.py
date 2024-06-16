import streamlit as st
from PIL import Image

def main():
    car_image_path = "Images/saly.jpg"
    
    st.title("Normas de la copa pistón 2024 ⚡")
    st.subheader("Detalles del evento")

    car_image = Image.open(car_image_path)
    st.image(car_image, use_column_width=True)

    st.write("""
    Esta competición veraniega arranca el lunes día 3 de junio a las 8:00h ⏰ y finaliza el 15 de septiembre a las 8:00 ⏰.
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
        - Cada participante, al finalizar su jornada, deberá poner por el grupo o web la cantidad de puntos que haya conseguido ese día y el total que lleve para llevar un control de la clasificación 📈📉.
        - La honestidad es crucial. En caso de sospecha, se reclamarán evidencias y/o explicaciones de donde han sacado los puntos 🧐📸.
        - En caso de trampas o sabotaje no permitido se votara el castigo o una descalificación directa
        - Los puntos provenientes de las sesiones de deporte funcionan de la siguiente manera:
            1. No habrá límite diario.
            2. Las sesiones durarán mínimo 1h a menos que sean casos especiales por lo tanto 30 minutos.
            3. Si se va a repetir la misma actividad deportiva se necesitará un intervalo de 1h para volver a repetirla y que cuente como puntos extra.
            4. En caso de que se hagan sesiones de deporte seguidas pero sean diferentes deportes se ignorará el intervalo de tiempo y se podrán sumar los puntos extra.
            5. Las sesiones de deporte que se hagan de manera consecutiva y quieran contar como dos sesiones diferentes, al ser dos actividades diferentes, ambas actividades juntas deberán sumar un mínimo de tiempo de 1h45.
            6. Ejemplo de caso especial para deportes de 30 min: si Jordi sale a nadar 40 minutos y luego corre 1 hora, se le sumarán 2 sesiones de deporte. Por otro lado, si solo quiere correr 30 minutos y nadar 30, solo le contará como 1 sesión.
        - Cualquier particpante con novia obtendra 5 puntos por sexo la primera vez en un dia pero 2 puntos las siguientes veces que se realice en ese dia.
    """)

    st.header("Normas del Grupo")

    st.write("""
    3. **Normas del Grupo:**
        - El grupo de puntuaciones se usa solo para pasar los puntos. Cualquier otro mensaje (excepto dudas o preguntas sobre puntos) puede resultar en penalización si así sale en las votaciones.
        - El jugador que haya sido descalificado debe abonar su parte del premio económico, trofeo y cena común.
        - Las votaciones son absolutas a menos que se vote lo contrario en un caso específico.
    """)

    st.header("Sistema de Puntos 💯")

    st.markdown("""
    | **Actividad** | **Puntos** |
    |---------------|------------|
    | Cubata        | 3 p        |
    | Chupito       | 1 p        |
    | Cerveza       | 1 p (en compañia)       |
    | Zumito/agua   | 2 p (exclusiva para Joel en ambiente de fiesta) |
    | Llegar a casa a + de las 7:00 | 1 p  |
    | Lio           | 3 p        |
    | Pico          | 2 p        |
    | Sexo novia    | 5/2 p        |
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
