import streamlit as st

# Set page configuration
st.set_page_config(page_title="Participantes de la Copa Piston", page_icon="👥")

# Title
st.title("Participantes de la Copa Piston 2024 👥")

# Participants data
participants = [
    {"name": "Alvaro", "photo": "Images/alvarito.jpg", "text": "“Gasté un montón de dinero en coches, mujeres y alcohol. El resto simplemente lo malgasté” -George Best"},
    # {"name": "Marco", "photo": "Images/participant2.jpg", "text": "Texto del participante 2."},
    # {"name": "Xavi", "photo": "Images/participant3.jpg", "text": "Texto del participante 3."},
    {"name": "Jaime", "photo": "Images/foto_suja_graciosa.jpg", "text": "El papá de de tu papá de tu papá 🦈//Me creo Piolin mi gata me reclama"},
    # {"name": "Joel", "photo": "Images/participant5.jpg", "text": "Texto del participante 5."},
    {"name": "Monta", "photo": "Images/monta.jpg", "text": "ESTO NO ES UN JUEGO! Hemos venido a competir. Solo para perracos🐕"},
    # {"name": "Perez", "photo": "Images/participant7.jpg", "text": "Texto del participante 7."},
    # {"name": "Cater", "photo": "Images/participant8.jpg", "text": "Texto del participante 8."},
    # {"name": "Juan", "photo": "Images/participant9.jpg", "text": "Texto del participante 9."},
    # {"name": "Jordi", "photo": "Images/participant10.jpg", "text": "Texto del participante 10."},
    # {"name": "Folch", "photo": "Images/participant11.jpg", "text": "Texto del participante 11."}
]

# Number of columns to display
num_columns = 3

# Display participants
for i in range(0, len(participants), num_columns):
    cols = st.columns(num_columns)
    for j, col in enumerate(cols):
        if i + j < len(participants):
            participant = participants[i + j]
            with col:
                st.image(participant["photo"], width=150)  # Adjust width to make the photos smaller
                st.subheader(participant["name"])
                st.write(participant["text"])

# Custom CSS for additional styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #222222;
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
    .stMarkdownContainer p {
        text-align: justify;
        text-justify: inter-word;
    }
    .stMarkdownContainer img {
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)