# TODO: все интеграции выносим в /services
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
    r = requests.get("https://app.tonkeeper.com/transfer/EQC2hxtAOioThqliO_U3pinztJQnNj90IpFKCF92E9cpKBZb?text=64ae95f12a0fca5568db6c21-UP")
    print(r) # вопрос, как нормально сделать этот самый запрос