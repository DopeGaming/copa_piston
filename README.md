# Copa Piston

1

#Your current IP address (77.243.23.105) has been added to enable local connectivity. Add another later in
#mongodb+srv://ocramayora:Arsic969!@cluster0.ckteqa9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
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

st.title("Bienvenidos a la copa Piston! 🍻🚗")
st.subheader("El juego definitivo del los verdaderos heroes del verano")
st.sidebar.title("Navigation")

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
2

import streamlit as st

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
                st.image(participant["photo"], width=150)  # Adjust width to make the photos smaller
                st.subheader(participant["name"])
                st.write(participant["text"])

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
3

import streamlit as st
from pymongo import MongoClient
from collections import defaultdict

# MongoDB setup
username = "ocramayora"
password = "Arsic969!"
cluster_address = "cluster0.ckteqa9.mongodb.net"

# Connection string with credentials
connection_string = f"mongodb+srv://{username}:{password}@{cluster_address}/?retryWrites=true&w=majority"

try:
    client = MongoClient(connection_string)
    db = client["copa_piston"]
    collection = db["daily_points"]
    st.success("Connected to MongoDB successfully!")
except Exception as e:
    st.error(f"Failed to connect to MongoDB: {e}")

st.title("Leaderboard 🏆")

# Aggregating points for each participant
try:
    pipeline = [
        {
            "$group": {
                "_id": "$participant",
                "total_points": {"$sum": "$points"}
            }
        },
        {"$sort": {"total_points": -1}}
    ]
    leaderboard = list(collection.aggregate(pipeline))
    
    st.subheader("Puntuación Total por Participante")
    if leaderboard:
        for idx, entry in enumerate(leaderboard, start=1):
            st.write(f"{idx}. **{entry['_id']}**: {entry['total_points']} puntos")
    else:
        st.write("No hay datos disponibles.")
except Exception as e:
    st.error(f"Error al obtener la tabla de clasificación: {e}")

 4

import streamlit as st
from pymongo import MongoClient
import datetime

# MongoDB setup
username = "ocramayora"
password = "Arsic969!"
cluster_address = "cluster0.ckteqa9.mongodb.net"

# Connection string with credentials
connection_string = f"mongodb+srv://{username}:{password}@{cluster_address}/?retryWrites=true&w=majority"

try:
    client = MongoClient(connection_string)
    db = client["copa_piston"]
    collection = db["daily_points"]
    st.success("Connected to MongoDB successfully!")
except Exception as e:
    st.error(f"Failed to connect to MongoDB: {e}")

st.title("Registrar Puntos Diarios 📋")

participants = [
    "Alvarito", "Marco", "Xavi", "Suja", "Joel", "Monta", "Perez", "Cater", "Juan", "Jordi", "Folch"
]

participant = st.selectbox("Selecciona tu nombre", participants)

st.subheader("Sistema de Puntos")

points = {
    "Cubata": 3, "Chupito": 1, "Cerveza": 1, "Zumito/agua": 1, "Llegar a casa a + de las 7:00": 1,
    "Lio": 3, "Pico": 2, "Sexo novia": 5, "Sexo el resto": 10, "Trio": 15,
    "Pico entre nosotros": -1, "Menor": -5, "Potar": -3, "Poner cuernos": -15, "Drogas duras": -5,
    "Deporte": 3, "Hacerse a una ex o alguien a quien has querido mucho (preguntar) sino DESCALIFICADO DIRECTO": 0
}

# Add a number input for each activity
accomplishments = {task: st.number_input(task, min_value=0, step=1, value=0) for task in points}

if st.button("Enviar"):
    # Calculate the total points
    total_points = sum(points[task] * accomplishments[task] for task in accomplishments if accomplishments[task] > 0)
    
    # Get the current date and time
    current_date = datetime.datetime.now()
    
    data = {
        "participant": participant,
        "date": current_date,  # Store the current date and time
        "points": total_points,
        "details": accomplishments  # Store the number of times each task was performed
    }
    collection.insert_one(data)
    st.success("¡Puntos registrados exitosamente!")

