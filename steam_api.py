"""Module for serving Steam API requests and adjacent operations to do with obtained game data."""
import requests
import os
import pandas as pd
from typing import Dict, List, Union
import time

def request_decode(link):
    """Make a GET request to the provided link and decode the JSON response."""
    req = requests.get(f"{link}")

    try:
        data = req.json()
    except requests.JSONDecodeError:
        data = None

    return data

def obtain_credentials() -> Dict[str, str]:
    """Obtain Steam API key and Steam ID from environment variables.
    
    Arguments:
    - None
    
    Returns:
    - os.environ.get("STEAM_API_KEY"), os.environ.get("STEAM_ID"): the user's Steam API key and Steam ID, respectively.
    
    Raises:
    - KeyError if the variables are not set.
    """
    try:
        return os.environ.get("STEAM_API_KEY"), os.environ.get("STEAM_ID")
    except KeyError:
        raise KeyError("The variables STEAM_API_KEY and STEAM_ID have not been set.")


def process_game_data(api_response):
    """Process the API response for a single game and extract relevant details.
    
    Arguments:
    - api_response (Dict): The API response for a single game.
    
    Returns:
    - Dict: A dictionary containing the processed game data with relevant fields.
    """
    app_id = list(api_response.keys())[0]
    game_data = api_response[app_id]
    
    if not game_data.get('success', False):
        return {'app_id': app_id, 'name': None, 'error': 'API request failed'}
    
    data = game_data['data']
    
    return {
        'app_id': data.get('steam_appid'),
        'name': data.get('name'),
        'genres': [g['description'] for g in data.get('genres', [])],
        'primary_genre': data.get('genres', [{}])[0].get('description') if data.get('genres') else None,
        'release_date': data.get('release_date', {}).get('date'),
        'coming_soon': data.get('release_date', {}).get('coming_soon', False),
        'developers': data.get('developers', []),
        'publishers': data.get('publishers', []),
        'primary_developer': data.get('developers', [None])[0],
        'categories': [c['description'] for c in data.get('categories', [])],
        'price_currency': data.get('price_overview', {}).get('currency'),
        'price_final': data.get('price_overview', {}).get('final') / 100 if data.get('price_overview') else None,
        'windows': data.get('platforms', {}).get('windows', False),
        'mac': data.get('platforms', {}).get('mac', False),
        'linux': data.get('platforms', {}).get('linux', False),
        'metacritic_score': data.get('metacritic', {}).get('score'),
        'type': data.get('type'),
    }


def get_game_data(app_ids, delay=1.5):
    """Retrieve details for a batch of Steam games using their app IDs. Used to create a DataFrame of games for downstream analysis.
    Contains rate-limiting to not hit quota for querying Steam API.
    
    """
    games_data = []
    for i, app_id in enumerate(app_ids):

        response = requests.get(f"https://store.steampowered.com/api/appdetails?appids={app_id}")

        games_data.append(process_game_data(response.json()))

        time.sleep(delay)

        if i % 50 == 0:
            print(f"Processed {i}/{len(app_ids)} games")

    return pd.DataFrame(games_data)


def get_games():
    """Retrieve user's Steam games using the Steam API.
    
    Arguments:
    - None
    
    Returns:
    - data (Dict[str, Union[List[Dict[str, str]], None]]): Dictionary containing the user's games and their details.
    """
    apikey, steamid = obtain_credentials()

    data = request_decode(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={apikey}&format=json&steamid={steamid}&include_appinfo=true&include_played_free_games=true")
        
    return data


def steam_game_retrieve() -> List[List[str]]:
    """Retrieve list of user's Steam games along with an associated header image for each.
    
    Arguments:
    - None
    
    Returns:
    - game_list (List[List[str]]): List of lists containing game names and their header images.
    """
    
    data = get_games()

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
    
    apikey, steamid = obtain_credentials()
    
    data = request_decode(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={apikey}&format=json&steamid={steamid}&include_appinfo=true&include_played_free_games=false")
    
    played = []
    
    for game in data['response']['games']:
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
    apikey, steamid = obtain_credentials()
    
    data = request_decode(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={apikey}&format=json&steamid={steamid}&include_appinfo=true&include_played_free_games=true")
    app_ids = [i['appid'] for i in data['response']['games']]
    
    game_data = get_game_data(app_ids, delay=1.5)
    game_data.to_csv('my_steam_games.csv', index=False)
    
    return game_data