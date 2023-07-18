import asyncio

import requests
import datetime

from database.bets import put_new_bet, get_all_bets
from db_init import bet_col_init


def timestamp_to_seconds(timestamp: str):
    dt = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S+00:00')
    return dt.timestamp()


class BookMakerAPI:
    def __init__(self):
        self.base_url = 'https://bookmakerapi.startech.live'

    def get(self, endpoint, params=None, headers=None):
        url = self.base_url + endpoint
        response = requests.get(url, params=params, headers=headers)
        return response.json()

    def get_active_games(self, endpoint='/games'):
        params = {'only_active': 'true', 'only_inactive': 'false', 'only_pending': 'false'}
        response = self.get(endpoint, params=params)

        active_games = []
        for x in response:
            if -1 < x['statistics']['increase_votes'] + x['statistics']['decrease_votes'] + x['statistics']['no_change_votes'] < 6:
                active_games.append({'id': x['id'], 'end_time': timestamp_to_seconds(x['finished_date']),
                                     'recipient': x['address']})

        return active_games

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


async def polling():
    await bet_col_init()
    x = await get_all_bets()
    print(x)


async def main():
    await polling()


if __name__ == '__main__':
    asyncio.run(main())
