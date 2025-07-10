import streamlit as st
from steam_api import steam_game_retrieve, games_by_time_played, create_game_df
import random
from typing import List, Dict, Union

def choose_and_display_game_name(games: List[Dict[str, str]]) -> Dict[str, str]:
    """Choose a random game from the list and display its name."""
    game = random.choice(games)
    print(game)
    st.markdown(f"**{game[0]}**")
    
    return game


def display_game_image(game: Dict[str, str]) -> None:
    """Choose a random game from the list and display its name."""
    if game[1]:
        st.image(game[1], width=200)
    else:
        st.markdown("No image available :(")
    
    return None


def game_row(type: str, game1=None, game2=None, game3=None) -> Union[Dict[str, str], None]:
    """Create a row of three game names, or images depending on need."""
    
    if type=='game':
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            game1 = choose_and_display_game_name(steam_game_retrieve())
            
        with col2:
            game2 = choose_and_display_game_name(steam_game_retrieve())
            
        with col3:
            game3 = choose_and_display_game_name(steam_game_retrieve())
            
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
    """Display three random games in a row based on time played, along with their artwork underneath."""
    # TODO #1 is broken - doesn't accurately retrieve games by time played
    # TODO #2 also now retrieves games as lists not dict, which are insanely slow - needs fix

    played = games_by_time_played(time_lower_bound, time_upper_bound)

    if played:
        game1, game2, game3 = game_row('game')
        game_row('img', game1, game2, game3)
        
    if not played:
        st.success(custom_alert_message)
        
    return None