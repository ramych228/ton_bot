import asyncio

from .ton_connector import TonConnector


class WalletManagement:
    def __init__(self, ton_connector: TonConnector):
        self.wallet = None
        self.ton_connector = ton_connector
        self.client = ton_connector.client

    async def async_init(self, seed):
        await TonConnector.async_init(self.ton_connector)
        self.wallet = await self.client.import_wallet(str(seed), source="v4r2")

    async def get_min_money(self):
        balance = await self.wallet.get_balance()
        return balance > 0

    async def transfer_money(self, recipient_address: str, value: int, comment: str):
        await self.wallet.transfer(recipient_address, self.client.to_nano(value), comment=str)


async def my_coroutine():
    tc = TonConnector()
    con = WalletManagement(tc)
    await con.try1()


async def main():
    await my_coroutine()


if __name__ == '__main__':
    asyncio.run(main())
