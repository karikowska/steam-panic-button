import requests
import os
import pandas as pd
from typing import Dict, List, Union

def obtain_credentials() -> Dict[str, str]:
    """Obtain Steam API key and Steam ID from environment variables.
    
    Arguments:
    - None
    
    Returns:
    - Dict[str, str]: Dictionary containing 'apikey' and 'steamid'.
    """
    return os.environ.get("STEAM_API_KEY"), os.environ.get("STEAM_ID")

def steam_game_retrieve() -> List[List[str]]:
    """Retrieve list of user's Steam games along with an associated header image for each.
    
    Arguments:
    - None
    
    Returns:
    - game_list (List[List[str]]): List of lists containing game names and their header images.
    """
    
    apikey, steamid = obtain_credentials()

    req = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={apikey}&format=json&steamid={steamid}&include_appinfo=true&include_played_free_games=true")

    try:
        data = req.json()
    except requests.JSONDecodeError:
        data = None

    game_list = [(i['name'], f"https://cdn.akamai.steamstatic.com/steam/apps/{i['appid']}/header.jpg") for i in data['response']['games']]
    
    return game_list


def games_by_time_played(lower_bound_time: float, upper_bound_time: float) -> List[dict]:
    """Retrieve list of user's Steam games based on time played, bounded on both sides.
    
    Arguments:
    - lower_bound_time (float): Minimum time played in minutes.
    - upper_bound_time (float): Maximum time played in minutes.
    
    Returns:
    - played (List[dict]): List of dicts containing game name, appid, library hero image, and playtime.
    """
    
    apikey, steamid = obtain_credentials().values()
    
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
    """Create a df out of the user's Steam data, for usage in data analysis in the dashboard.
    
    Arguments:
    - None
    
    Returns:
    - df (pd.DataFrame): DataFrame containing the user's Steam games.
    """

    req = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={apikey}&format=json&steamid={steamid}&include_appinfo=true&include_played_free_games=true")

    games = req['response']['games']
    
    df = pd.DataFrame(games)
    
    return df


