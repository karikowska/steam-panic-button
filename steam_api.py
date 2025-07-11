import requests
import os
import pandas as pd
from typing import Dict, List, Union

def steam_game_retrieve() -> List[List[str]]:
    """Retrieve list of user's Steam games along with an associated header image for each."""
    apikey = os.environ["STEAM_API_KEY"]
    steamid = os.environ["STEAM_ID"]

    req = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={apikey}&format=json&steamid={steamid}&include_appinfo=true&include_played_free_games=true")

    try:
        data = req.json()
    except requests.JSONDecodeError:
        data = None

    game_list = [(i['name'], f"https://cdn.akamai.steamstatic.com/steam/apps/{i['appid']}/header.jpg") for i in data['response']['games']]
    
    return game_list


def games_by_time_played(lower_bound_time: float, upper_bound_time: float) -> List[dict]:
    """Retrieve list of user's Steam games based on time played."""
    apikey = os.environ["STEAM_API_KEY"]
    steamid = os.environ["STEAM_ID"]
    
    req = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={apikey}&format=json&steamid={steamid}&include_appinfo=true&include_played_free_games=false")
    
    games = req.json()['response']['games']
    
    played = []
    
    for game in games:
        if game.get('playtime_forever', 0) <= upper_bound_time and game.get('playtime_forever', 0) >= lower_bound_time:
            appid = game['appid']
            
            game_info = {
                'name': game['name'],
                'appid': appid,
                'library_hero': f"https://cdn.akamai.steamstatic.com/steam/apps/{appid}/header.jpg",
                'playtime': game['playtime_forever']
            }
            
            played.append(game_info)
    
    return played


def create_game_df() -> pd.DataFrame:
    """Create a df out of the user's Steam data, for usage in data analysis in the dashboard."""

    req = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={apikey}&format=json&steamid={steamid}&include_appinfo=true&include_played_free_games=true")

    games = data['response']['games']
    
    df = pd.DataFrame(games)
    
    return df


