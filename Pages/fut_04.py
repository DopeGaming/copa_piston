import streamlit as st
from jinja2 import Environment, FileSystemLoader
import os

def main():

    image_path = "Images/alineacion1.png"
    st.title("Alineación San Juan")
    st.image(image_path, use_column_width=True)


    # # Setup Jinja2 environment
    # env = Environment(loader=FileSystemLoader('templates'))

    # # Load player images
    # player_images = {
    # "Player 1": "Images/card1.png",
    # "Player 2": "Images/card2.png",
    # "Player 3": "Images/card3.png",
    # "Player 4": "Images/card4.png",
    # "Player 5": "Images/card5.png",
    # "Player 6": "Images/card6.png",
    # "Player 7": "Images/card7.png",
    # "Player 8": "Images/card8.png",
    # "Player 9": "Images/card9.png",
    # "Player 10": "Images/card10.png",
    # "Player 11": "Images/card11.png"
    # }
    # players = [{"id": f"player-{i}", "image": image, "name": name} for i, (name, image) in enumerate(player_images.items())]

    # # Render the HTML template
    # template = env.get_template('formation.html')
    # html_content = template.render(players=players)

    # # Display the custom HTML in Streamlit
    # st.components.v1.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()