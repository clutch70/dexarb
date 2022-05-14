from web3 import Web3
# from web3 import EthereumTesterProvider
import polygon
# create your own keys.py with an API token and whatever other private things you need
import keys
import common

url = "https://eth-mainnet.alchemyapi.io/v2/" + keys.urlToken
polygonUrl = "https://polygon-mainnet.g.alchemy.com/v2/" + keys.urlToken
wss = "wss://eth-mainnet.alchemyapi.io/v2/" + keys.urlToken
polygonWss = "wss://polygon-mainnet.g.alchemy.com/v2/" + keys.urlToken
address = keys.ledg01Addr
lpContract = "0xdC9232E2Df177d7a12FdFf6EcBAb114E2231198D"
tokenContract = "0x1bfd67037b42cf73acf2047067bd4f2c47d9bfd6"


# tokenData = [{"polygon":{"baseContract":"0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"},
#                {"lpContracts":
#                     []
#                 }


#            }]


def run():
    w3 = Web3(Web3.WebsocketProvider(polygonWss))
    # latest = w3.eth.get_block('latest')
    # print(latest)

    # balance = w3.fromWei(w3.eth.get_balance(address), 'ether')
    # decBalance = w3.fromWei(balance, 'ether')
    # print(balance,"MATIC")
    # abi = polygon.get_abi(w3, "address", lpContract)
    # eventually, the chain parameter (polygon) needs to be replaced with tokenData
    abi = common.get_abi(w3, "address", lpContract, "polygon")
    contract_instance = w3.eth.contract(address=lpContract, abi=abi)
    print(contract_instance.all_functions())
    print(contract_instance.functions.token0().call())


# def get_lp_prices:


if __name__ == '__main__':
    run()
