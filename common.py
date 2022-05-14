import polygon


version = 0.001

# Functions implemented in this module should handle all supported chains in main.tokenData


def get_abi(w3, addrType, contractAddr, chain):
    if chain == "polygon":
        return polygon.get_abi(w3, addrType, contractAddr)


def run():
    pass


if __name__ == '__main__':
    run()
