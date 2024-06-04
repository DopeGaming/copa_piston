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
