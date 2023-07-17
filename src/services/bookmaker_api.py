import asyncio

import requests
import datetime

from services.ton_connector import TonConnector
from services.wallet_management import WalletManagement


def timestamp_to_seconds(timestamp):
    dt = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')
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

        active_games_id = []
        for x in response:
            if -1 < x['statistics']['increase_votes'] + x['statistics']['decrease_votes'] + \
                    x['statistics']['no_change_votes'] < 6:
                # Диапазон чисел определяющий возможное количество участников в игре
                active_games_id.append({'id': x['id'], 'end_time': timestamp_to_seconds(x['finished_date'])})

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


async def deploy_wallet(wallet):
    tc = TonConnector()

    boc = wallet.create_init_external_message()['message'].to_boc(False)

    client = tc.client

    await client.raw_send_message(boc)


async def my_coroutine():
    tc = TonConnector()
    wm = WalletManagement(tc)
    await wm.async_init(
        seed1 # вставить сид)
    # await wm.async_init(
    #     ['approve', 'sound', 'effort', 'wear', 'hotel', 'afford', 'shoot', 'animal', 'pottery', 'response', 'skirt',
    #      'owner', 'rookie', 'trouble', 'sting', 'ritual', 'helmet', 'magic', 'prevent', 'squeeze', 'season', 'riot',
    #      'margin', 'give'])
    wallet = wm.wallet
    recipient = "EQD-ntoERuo_QqYpnQ5HXSaRDMxxmV5VGgJqaRbDJhjycSi3"

    account = await wm.client.find_account(recipient)

    txs = await account.get_state()
    txs_cur = await wallet.get_state()
    print(txs)
    print(txs_cur)

    await wm.transfer_money(recipient, 1, "1 try")
    print(wallet.address)


async def main():
    await my_coroutine()


if __name__ == '__main__':
    asyncio.run(main())
