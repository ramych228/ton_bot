from ton import TonlibClient

client = TonlibClient()
TonlibClient.enable_unaudited_binaries()
await client.init_tonlib()