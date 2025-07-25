import streamlit as st
from steam_api import steam_game_retrieve, games_by_time_played, create_game_df
import random
from typing import List, Dict, Union

def choose_and_display_game_name(games: List[Dict[str, str]]) -> Dict[str, str]:
    """Choose a random game from the list and display its name.
    
    Arguments:
    - games (List[Dict[str, str]]): List of games to choose from.
    
    Returns:
    - game (Dict[str, str]): Dictionary containing the chosen game's name and appid.
    """
    
    game = random.choice(games)
    st.markdown(f"**{game['name']}**")
    
    return game


def display_game_image(game: Dict[str, str]) -> None:
    """Choose a random game from the list and display its name.
    
    Arguments:
    - game (Dict[str, str]): Dictionary containing the game's name and appid.
    
    Returns:
    - None
    """
    
    if game['library_hero']:
        st.image(game['library_hero'], width=200)
    else:
        st.markdown("No image available :(")
    
    return None


def game_row(type: str, played=None, game1=None, game2=None, game3=None) -> Union[Dict[str, str], None]:
    """Create a row of three game names, or images depending on type selected. Used for the randomised game display.
    
    Arguments:
    - type (str): Type of content to display ('game' for names, 'img' for images).
    - played (List[Dict[str, str]]): List of games to choose from if type is 'game'.
    - game1, game2, game3 (Dict[str, str]): Game whose images should be displayed if type == 'img'.
    
    Returns:
    - game1, game2, game3 (Dict[str, str]): Dictionaries containing the chosen games' names and appids if type == 'game'.
    - None: If type == 'img', the function displays images and returns None."""
    
    if type=='game':
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            game1 = choose_and_display_game_name(played)
            
        with col2:
            game2 = choose_and_display_game_name(played)
            
        with col3:
            game3 = choose_and_display_game_name(played)
            
        return game1, game2, game3
    
    elif type=='img':
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            display_game_image(game1)
            
        with col2:
            display_game_image(game2)
            
        with col3:
            display_game_image(game3)
            
        return None


def display_games(time_lower_bound: float, time_upper_bound: float, custom_alert_message: str) -> None:
    """Display three random games in a row based on time played, along with their artwork underneath.
    
    Arguments:
    - time_lower_bound (float): Minimum time played in minutes.
    - time_upper_bound (float): Maximum time played in minutes.
    - custom_alert_message (str): Message to display if no games are found.
    
    Returns:
    - None
    """

    played = games_by_time_played(time_lower_bound, time_upper_bound)

    if played:
        game1, game2, game3 = game_row('game', played)
        game_row('img', None, game1, game2, game3)
        
    if not played:
        st.success(custom_alert_message)
        
    return None