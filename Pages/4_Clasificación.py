import streamlit as st
from pymongo import MongoClient
import pandas as pd

# MongoDB setup
client = MongoClient("your_mongodb_uri")
db = client["copa_piston"]
collection = db["daily_points"]

# Set page configuration
st.set_page_config(page_title="Tabla de Clasificación", page_icon="🏆")

# Title
st.title("Tabla de Clasificación 🏆")

# Fetch data from MongoDB
data = list(collection.find())

# Calculate total points for each participant
leaderboard = {}
for entry in data:
    participant = entry["participant"]
    points = entry["points"]
    if participant in leaderboard:
        leaderboard[participant] += points
    else:
        leaderboard[participant] = points

# Convert leaderboard to a DataFrame
df = pd.DataFrame(list(leaderboard.items()), columns=["Participant", "Total Points"])
df = df.sort_values(by="Total Points", ascending=False)

# Display the leaderboard
st.dataframe(df)
