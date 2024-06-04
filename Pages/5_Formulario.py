import streamlit as st
from pymongo import MongoClient
import datetime

# MongoDB setup
client = MongoClient("your_mongodb_uri")
db = client["copa_piston"]
collection = db["daily_points"]

# Set page configuration
st.set_page_config(page_title="Registrar Puntos", page_icon="📋")

# Title
st.title("Registrar Puntos Diarios 📋")

# Participant selection
participants = [
    "Alvaro", "Marco", "Xavi", "Suja", "Joel", "Monta", "Perez", "Cater", "Juan", "Jordi", "Folch"
]

participant = st.selectbox("Selecciona tu nombre", participants)

# Point system checkboxes
st.subheader("Sistema de Puntos")

points = {
    "Cubata": 3, "Chupito": 1, "Cerveza": 1, "Zumito/agua": 1, "Llegar a casa a + de las 7:00": 1,
    "Lio": 3, "Pico": 2, "Sexo novia": 5, "Sexo el resto": 10, "Trio": 15,
    "Pico entre nosotros": -1, "Menor": -5, "Potar": -3, "Poner cuernos": -15, "Drogas duras": -5,
    "Deporte": 3, "Hacerse a una ex o alguien a quien has querido mucho (preguntar) sino DESCALIFICADO DIRECTO": 0
}

accomplishments = {task: st.checkbox(task) for task in points}

# Submit button
if st.button("Enviar"):
    total_points = sum(points[task] for task in accomplishments if accomplishments[task])
    data = {
        "participant": participant,
        "date": datetime.datetime.now(),
        "points": total_points,
        "details": {task: accomplishments[task] for task in accomplishments}
    }
    collection.insert_one(data)
    st.success("¡Puntos registrados exitosamente!")
