import asyncio

from ton.sync import TonlibClient


class TonConnector:
    client = TonlibClient()
    TonlibClient.enable_unaudited_binaries()

    def __init__(self):
        self.loop = asyncio.get_event_loop()

    async def async_init(self):
        await self.client.init_tonlib()
        print("ton_client init successfully")
