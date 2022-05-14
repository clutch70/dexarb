from web3 import Web3
#from web3 import EthereumTesterProvider
import polygon
#create your own keys.py with an API token and whatever other private things you need
import keys

# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

url = "https://eth-mainnet.alchemyapi.io/v2/" + keys.urlToken
polygonUrl = "https://polygon-mainnet.g.alchemy.com/v2/" + keys.urlToken
wss = "wss://eth-mainnet.alchemyapi.io/v2/" + keys.urlToken
polygonWss = "wss://polygon-mainnet.g.alchemy.com/v2/" + keys.urlToken
address = keys.ledg01Addr
lpContract = "0xdC9232E2Df177d7a12FdFf6EcBAb114E2231198D"
tokenContract = "0x1bfd67037b42cf73acf2047067bd4f2c47d9bfd6"

def run():
    w3 = Web3(Web3.WebsocketProvider(polygonWss))
    #latest = w3.eth.get_block('latest')
    #print(latest)

    #balance = w3.fromWei(w3.eth.get_balance(address), 'ether')
    #decBalance = w3.fromWei(balance, 'ether')
    #print(balance,"MATIC")
    abi = polygon.get_abi(w3,"address",lpContract)
    contract_instance = w3.eth.contract(address = lpContract, abi = abi)
    print(contract_instance.all_functions())
    print(contract_instance.functions.token0().call())

    contractPageData = []
    #polygon.reset_page_data()
    #print(polygon.get_abi(w3, "address", tokenContract))
    contractPageData = []
    #polygon.reset_page_data()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#def get_lp_prices:




if __name__ == '__main__':
    run()