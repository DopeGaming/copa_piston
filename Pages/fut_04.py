import streamlit as st 

def main():
    st.title("Próximamente")


if __name__ == "__main__":
    main()

# import streamlit as st
# from PIL import Image
# from streamlit_image_select import image_select

# # Load player images
# player_images = {
#     "Player 1": "Images/card1.png",
#     "Player 2": "Images/card2.png",
#     "Player 3": "Images/card3.png",
#     "Player 4": "Images/card4.png",
#     "Player 5": "Images/card5.png",
#     "Player 6": "Images/card6.png",
#     "Player 7": "Images/card7.png",
#     "Player 8": "Images/card8.png",
#     "Player 9": "Images/card9.png",
#     "Player 10": "Images/card10.png",
#     "Player 11": "Images/card11.png"
# }

# # Function to display player image
# def display_player(image_path, caption):
#     image = Image.open(image_path)
#     st.image(image, caption=caption, use_column_width=True)

# st.title("Interactive Football Team Formation")

# # Define formation slots
# formation_slots = ["GK", "LB", "CB", "CB", "RB", "LM", "CM", "CM", "RM", "LW", "ST", "RW"]

# # Display player cards for selection
# st.sidebar.header("Select Players")
# selected_players = {}
# for player_name, image_path in player_images.items():
#     if st.sidebar.checkbox(player_name):
#         selected_players[player_name] = image_path

# # Display formation slots with selectable players
# st.subheader("Formation")
# formation = {}
# for slot in formation_slots:
#     st.write(f"{slot}:")
#     if selected_players:
#         selected_player = image_select(f"Select player for {slot}", list(selected_players.values()), captions=list(selected_players.keys()))
#         if selected_player:
#             formation[slot] = [k for k, v in selected_players.items() if v == selected_player][0]
#             display_player(selected_player, formation[slot])

# # Show the final formation
# if st.button("Show Formation"):
#     st.write("Current Formation:")
#     for slot, player in formation.items():
#         st.write(f"{slot}: {player}")
#         display_player(player_images[player], player)
