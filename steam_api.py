import requests
import os

def steam_game_retrieve():
    """Retrieve list of user's Steam games."""
    apikey = os.environ["STEAM_API_KEY"]
    steamid = os.environ["STEAM_ID"]

    req = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={apikey}&format=json&steamid={steamid}&include_appinfo=true&include_played_free_games=true")

    try:
        data = req.json()
    except requests.JSONDecodeError:
        data = None

    # for i in data['response']['games']:
    #     print(i['name'])
        
    game_list = [i['name'] for i in data['response']['games']]
    
    return game_list