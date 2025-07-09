import requests
import os

def steam_game_retrieve():
    """Retrieve list of user's Steam games along with a header image."""
    apikey = os.environ["STEAM_API_KEY"]
    steamid = os.environ["STEAM_ID"]

    req = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={apikey}&format=json&steamid={steamid}&include_appinfo=true&include_played_free_games=true")

    try:
        data = req.json()
    except requests.JSONDecodeError:
        data = None

    game_list = [[i['name'], f"https://cdn.akamai.steamstatic.com/steam/apps/{i['appid']}/header.jpg"] for i in data['response']['games']]
    
    return game_list


def steam_game_unplayed(lower_bound_time: float, upper_bound_time: float):
    """Retrieve list of user's Steam games that are unplayed."""
    apikey = os.environ["STEAM_API_KEY"]
    steamid = os.environ["STEAM_ID"]
    
    req = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={apikey}&format=json&steamid={steamid}&include_appinfo=true&include_played_free_games=false")
    
    games = req.json()['response']['games']
    
    unplayed = []
    
    for game in games:
        if game.get('playtime_forever', 0) <= upper_bound_time and game.get('playtime_forever', 0) >= lower_bound_time:
            appid = game['appid']
            
            game_info = {
                'name': game['name'],
                'appid': appid,
                'library_hero': f"https://cdn.akamai.steamstatic.com/steam/apps/{appid}/header.jpg"
                'playtime': game.get('playtime_forever', 0),
            }
            
            unplayed.append(game_info)
    
    return unplayed

