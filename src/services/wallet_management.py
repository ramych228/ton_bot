from .ton_connector import TonConnector


class WalletManagement:
    def __init__(self, ton_connector: TonConnector):
        self.wallet = None
        self.ton_connector = ton_connector
        self.client = ton_connector.client

    async def async_init(self, seed):
        # TODO: мы не можем инициализировать один класс для нескольких кошельков, поэтому принимать сид в аргументах этой функции не нужно, перенести в инициализацию самого класса
        await TonConnector.async_init(self.ton_connector)
        self.wallet = await self.client.import_wallet(str(seed), source="v4r2")

    async def get_min_money(self):
        # TODO: относится внимательней к неймингу
        # get_min_money -> получить минимум денег, это верно? тем более отдаешь bool -> is_empty лучше?
        balance = await self.wallet.get_balance()
        return balance > 0

    async def transfer_money(self, recipient_address: str, value: int, comment: str):
        await self.wallet.transfer(recipient_address, self.client.to_nano(value), comment=comment)
