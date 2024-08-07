import streamlit as st
from pymongo import MongoClient
import datetime

def main():
    # MongoDB setup
    username = "ocramayora"
    password = "Arsic969!"
    cluster_address = "cluster0.ckteqa9.mongodb.net"
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
        "Escoge Tu participante",
        "Alvarito", "Marco", "Xavi", "Suja", "Joel", "Monta", "Perez", "Cater", "Juan", "Jordi", "Folch"
    ]

    participant = st.selectbox("Selecciona tu nombre", participants)

    st.subheader("Sistema de Puntos")

    points = {
        "Cubata": 3, "Chupito": 1, "Cerveza": 1, "Zumito/agua": 2, "Llegar a casa a + de las 7:00": 1,
        "Lio": 3, "Pico": 2, "Sexo novia(Primera vez)": 5,"Sexo novia(resto de veces)":2, "Sexo el resto": 10, "Trio": 15,
        "Pico entre nosotros": -1, "Menor": -5, "Potar": -3, "Poner cuernos": -15, "Drogas duras": -5,
        "Deporte": 3, "Libro(10pag)": 1, "Hacerse a una ex o alguien a quien has querido mucho (preguntar) sino DESCALIFICADO DIRECTO": 0
    }

    
    accomplishments = {task: st.number_input(task, min_value=0, step=1, value=0) for task in points}

    if st.button("Enviar"):
        # Check if a participant has been selected
        if participant == "Escoge Tu participante":
            st.error("Por favor, selecciona un participante.")
        else:
            # Calculate the total points, including negative points
            total_points = sum(points[task] * accomplishments[task] for task in accomplishments)

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

if __name__ == "__main__":
    main()
