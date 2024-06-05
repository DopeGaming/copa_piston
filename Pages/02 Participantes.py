import streamlit as st

def main():
    st.title("Participantes de la Copa Piston 2024 👥")

    participants = [
        {"name": "flicki flacka", "photo": "./Images/alvarito.jpg", "text": "“Gasté un montón de dinero en coches, mujeres y alcohol. El resto simplemente lo malgasté” -George Best"},
        {"name": "Pelee", "photo": "./Images/marquimetro.jpg", "text": "Por mis venas corre el agua con un poco de rrrrron cola"},
        {"name": "BigJavs", "photo": "./Images/xavi1.jpg", "text": "El dia que el amor se convierta en alcohol, me lo tomare en serio"},
        {"name": "Suja", "photo": "./Images/foto_suja_graciosa.jpg", "text": "El papá de de tu papá de tu papá 🦈//Me creo Piolin mi gata me reclama"},
        {"name": "Joel", "photo": "./Images/joel1.jpg", "text": "Yo lo soñé"},
        {"name": "Monta", "photo": "./Images/monta.jpg", "text": "ESTO NO ES UN JUEGO! Hemos venido a competir. Solo para perracos🐕"},
        {"name": "Perez", "photo": "./Images/perez.jpg", "text": "Que vamos a hacer?? Follar, follar y follar"},
        {"name": "Cater", "photo": "./Images/cater1.jpg", "text": "En busca del One Piece"},
        {"name": "Juan3c3k3", "photo": "./Images/juanpa.jpg", "text": "Texto del participante 9."},
        {"name": "Jorge", "photo": "./Images/jordi1.jpg", "text": "Deportista iniciándome en el mundo del alcoholismo y el mundo femenino"},
        {"name": "Folch", "photo": "./Images/folch1.jpg", "text": "Texto del participante 11."}
    ]

    num_columns = 3

    for i in range(0, len(participants), num_columns):
        cols = st.columns(num_columns)
        for j, col in enumerate(cols):
            if i + j < len(participants):
                participant = participants[i + j]
                with col:
                    st.image(participant["photo"], width=150)
                    st.subheader(participant["name"])
                    st.write(participant["text"])

    # st.markdown(
    #     """
    #     <style>
    #     .stApp {
    #         background-color: #222222;
    #         color: #ffffff;
    #     }
    #     .stApp header {
    #         background: rgba(0, 0, 0, 0.7);
    #         padding: 10px;
    #         border-radius: 10px;
    #     }
    #     .stApp footer {
    #         background: rgba(0, 0, 0, 0.7);
    #         padding: 10px;
    #         border-radius: 10px;
    #         text-align: center;
    #     }
    #     .stMarkdownContainer p {
    #         text-align: justify;
    #         text-justify: inter-word;
    #     }
    #     .stMarkdownContainer img {
    #         border-radius: 10px;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )

if __name__ == "__main__":
    main()
