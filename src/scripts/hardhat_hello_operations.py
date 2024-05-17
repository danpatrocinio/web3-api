import json
from web3 import Web3
from contracts import read_contracts

def getMessage() -> bool:
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    try:
        abi = read_contracts.get_contratc_abi()
        contract_address = read_contracts.get_contract_address()
    except FileNotFoundError as e:
        print(str(e))
        return None
    
    contract = w3.eth.contract(address=contract_address, abi=abi)

    # get message
    message = contract.functions.getMessage().call()
    print("Get message from address:", contract_address, "=>", message)
    response = w3.to_json({ 'message': message })

    return json.loads(response)


def setMessage(message: str, account_caller: str, private_key: str) -> bool:
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    try:
        abi = read_contracts.get_contratc_abi()
        contract_address = read_contracts.get_contract_address()
    except FileNotFoundError as e:
        print(str(e))
        return None
    
    contract = w3.eth.contract(address=contract_address, abi=abi)
    nonce = w3.eth.get_transaction_count(account_caller)
    attributes_transaction = { 'from': account_caller, 'gasPrice': w3.to_wei(1, 'gwei'), 'nonce': nonce }
    tx = contract.functions.setMessage(message).build_transaction(attributes_transaction)
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)

    # Setting new message
    print("Setting message to address:", contract_address, "=>", message, "by account:", account_caller)
    send_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction) 
    
    tx_receipt = w3.eth.wait_for_transaction_receipt(send_tx)
    response = w3.to_json(tx_receipt)

    return json.loads(response)


def clearMessage(account_caller: str, private_key: str) -> bool:
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    try:
        abi = read_contracts.get_contratc_abi()
        contract_address = read_contracts.get_contract_address()
    except FileNotFoundError as e:
        print(str(e))
        return None
    
    contract = w3.eth.contract(address=contract_address, abi=abi)
    nonce = w3.eth.get_transaction_count(account_caller)
    attributes_transaction = { 'from': account_caller, 'gasPrice': w3.to_wei(1, 'gwei'), 'nonce': nonce }
    tx = contract.functions.clearMessage().build_transaction(attributes_transaction)
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    
    # clear message by contract method
    print("Cleared message from address:", contract_address)
    send_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction) 

    tx_receipt = w3.eth.wait_for_transaction_receipt(send_tx)
    response = w3.to_json(tx_receipt)

    return json.loads(response)