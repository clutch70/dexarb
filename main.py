from web3 import Web3
#from web3 import EthereumTesterProvider
import polygon
import keys

# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

url = "https://eth-mainnet.alchemyapi.io/v2/" + keys.urlToken
polygonUrl = "https://polygon-mainnet.g.alchemy.com/v2/" + keys.urlToken
wss = "wss://eth-mainnet.alchemyapi.io/v2/" + keys.urlToken
polygonWss = "wss://polygon-mainnet.g.alchemy.com/v2/" + keys.urlToken
address = "0x0F2e54b53570AD0f89F9AC2C697d846810F394D7"
lpContract = "0xdC9232E2Df177d7a12FdFf6EcBAb114E2231198D"
tokenContract = "0x1bfd67037b42cf73acf2047067bd4f2c47d9bfd6"

#def get_lp_prices:



def run():
    w3 = Web3(Web3.WebsocketProvider(polygonWss))
    #latest = w3.eth.get_block('latest')
    #print(latest)

    #balance = w3.fromWei(w3.eth.get_balance(address), 'ether')
    #decBalance = w3.fromWei(balance, 'ether')
    #print(balance,"MATIC")
    print(polygon.get_abi(w3,"address",lpContract))
    contractPageData = []
    #polygon.reset_page_data()
    print(polygon.get_abi(w3, "address", tokenContract))
    contractPageData = []
    #polygon.reset_page_data()

if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
