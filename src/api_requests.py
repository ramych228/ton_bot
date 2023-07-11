import requests

def get_active_games():
    response = requests.get('https://bookmakerapi.startech.live/games?only_active=true&only_inactive=false'
                            '&only_pending=false')
    json_response = response.json()
    active_games_id = []
    for x in json_response:
        if -1 < x['statistics']['increase_votes'] + x['statistics']['decrease_votes'] + \
                x['statistics']['no_change_votes'] < 6: # Диапазон чисел определяющий возможное количество участников в игре
            active_games_id.append(x['id'])

    return active_games_id


if __name__ == '__main__':
    print(get_active_games())
