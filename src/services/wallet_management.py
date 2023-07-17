from .ton_connector import TonConnector


class WalletManagement:
    def __init__(self, ton_connector: TonConnector, seed: [str]):
        self.wallet = None
        self.ton_connector = ton_connector
        self.client = ton_connector.client
        self.seed = seed

    async def async_init(self):
        await TonConnector.async_init(self.ton_connector)
        self.wallet = await self.client.import_wallet(str(self.seed))

    async def have_min_money(self): # TODO: как его назвать нормально? is_empty не совсем верно
        balance = await self.wallet.get_balance()
        return balance > 0  # вообще, здесь должен быть не 0, это временное решение в тз по-другому

    async def transfer_money(self, recipient_address: str, value: float, comment: str):
        await self.wallet.transfer(recipient_address, self.client.to_nano(value), comment=comment)
