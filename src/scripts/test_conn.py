from web3 import Web3

def check_connection() -> bool:
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    return w3.is_connected()