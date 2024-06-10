# import streamlit as st
# from pymongo import MongoClient
# import pandas as pd

# def clear_collection():
#     # MongoDB setup
#     username = "ocramayora"
#     password = "Arsic969!"
#     cluster_address = "cluster0.ckteqa9.mongodb.net"
#     connection_string = f"mongodb+srv://{username}:{password}@{cluster_address}/?retryWrites=true&w=majority"
    
#     try:
#         client = MongoClient(connection_string)
#         db = client["copa_piston"]
#         collection = db["daily_points"]
#         result = collection.delete_many({})
#         return result.deleted_count
#     except Exception as e:
#         return f"Failed to connect to MongoDB: {e}"

# def main():
#     st.title("Leaderboard 🏆")
    
#     if st.button("Clear All Data"):
#         deleted_count = clear_collection()
#         if isinstance(deleted_count, int):
#             st.success(f"Deleted {deleted_count} documents.")
#         else:
#             st.error(deleted_count)

#     # MongoDB setup
#     username = "ocramayora"
#     password = "Arsic969!"
#     cluster_address = "cluster0.ckteqa9.mongodb.net"
#     connection_string = f"mongodb+srv://{username}:{password}@{cluster_address}/?retryWrites=true&w=majority"
    
#     try:
#         client = MongoClient(connection_string)
#         db = client["copa_piston"]
#         collection = db["daily_points"]
#         st.success("Connected to MongoDB successfully!")
#     except Exception as e:
#         st.error(f"Failed to connect to MongoDB: {e}")

#     # Aggregating points and details for each participant
#     try:
#         pipeline = [
#             {
#                 "$group": {
#                     "_id": "$participant",
#                     "total_points": {"$sum": "$points"},
#                     "details": {"$push": "$details"}
#                 }
#             },
#             {"$sort": {"total_points": -1}}
#         ]
#         leaderboard = list(collection.aggregate(pipeline))

#         st.subheader("Puntuación Total por Participante")
#         if leaderboard:
#             # Create a detailed leaderboard
#             detailed_data = []
#             for entry in leaderboard:
#                 participant = entry['_id']
#                 total_points = entry['total_points']
#                 details = pd.DataFrame(entry['details']).sum().to_dict()  # Summing up the details
                
#                 detailed_data.append({
#                     "Participante": participant,
#                     "Total Puntos": total_points,
#                     **details
#                 })
            
#             detailed_df = pd.DataFrame(detailed_data)
#             st.dataframe(detailed_df)
#         else:
#             st.write("No hay datos disponibles.")
#     except Exception as e:
#         st.error(f"Error al obtener la tabla de clasificación: {e}")

# if __name__ == "__main__":
#     main()

# SOLO ACTIVAR SI QUIERES ACTIVAR FUNCION DE ELIMINAR TODA LA BASE DE DATOS

import streamlit as st
from pymongo import MongoClient
import pandas as pd

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

    st.title("Leaderboard 🏆")

    # Aggregating points and details for each participant
    try:
        pipeline = [
            {
                "$group": {
                    "_id": "$participant",
                    "total_points": {"$sum": "$points"},
                    "details": {"$push": "$details"}
                }
            },
            {"$sort": {"total_points": -1}}
        ]
        leaderboard = list(collection.aggregate(pipeline))

        st.subheader("Puntuación Total por Participante")
        if leaderboard:
            # Create a detailed leaderboard
            detailed_data = []
            for entry in leaderboard:
                participant = entry['_id']
                total_points = entry['total_points']
                details = pd.DataFrame(entry['details']).sum().to_dict()  # Summing up the details
                
                detailed_data.append({
                    "Participante": participant,
                    "Total Puntos": total_points,
                    **details
                })
            
            detailed_df = pd.DataFrame(detailed_data)
            st.dataframe(detailed_df)
        else:
            st.write("No hay datos disponibles.")
    except Exception as e:
        st.error(f"Error al obtener la tabla de clasificación: {e}")

    # Displaying the last 11 records
    st.subheader("Historial")

    try:
        last_entries = collection.find().sort("date", -1).limit(11)
        last_entries_list = list(last_entries)
        
        if last_entries_list:
            last_entries_data = []
            for entry in last_entries_list:
                entry_data = {
                    "Participante": entry["participant"],
                    "Fecha": entry["date"].strftime("%Y-%m-%d %H:%M:%S"),
                    "Total Puntos": entry["points"],
                    **entry["details"]
                }
                last_entries_data.append(entry_data)
            
            last_entries_df = pd.DataFrame(last_entries_data)
            st.dataframe(last_entries_df)
        else:
            st.write("No hay entradas recientes.")
    except Exception as e:
        st.error(f"Error al obtener las últimas entradas: {e}")

if __name__ == "__main__":
    main()
