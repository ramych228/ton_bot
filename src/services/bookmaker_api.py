import requests


class BookMakerAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None, headers=None):
        url = self.base_url + endpoint
        response = requests.get(url, params=params, headers=headers)
        return response.json()

    def get_active_games(self, endpoint='/games'):
        params = {'only_active': 'true', 'only_inactive': 'false', 'only_pending': 'false'}
        response = self.get(endpoint, params=params)

        active_games_id = []
        for x in response:
            if -1 < x['statistics']['increase_votes'] + x['statistics']['decrease_votes'] + \
                    x['statistics']['no_change_votes'] < 6:
                # Диапазон чисел определяющий возможное количество участников в игре
                active_games_id.append(x['id'])

        return active_games_id

    def post(self, endpoint, data=None, headers=None):
        url = self.base_url + endpoint
        response = requests.post(url, json=data, headers=headers)
        return response.json()

    def put(self, endpoint, data=None, headers=None):
        url = self.base_url + endpoint
        response = requests.put(url, json=data, headers=headers)
        return response.json()

    def delete(self, endpoint, headers=None):
        url = self.base_url + endpoint
        response = requests.delete(url, headers=headers)
        return response.json()
