from ton.sync import TonlibClient


class TonConnector:
    def __init__(self):
        self.client = TonlibClient()
        TonlibClient.enable_unaudited_binaries()
        self.client.init_tonlib()
