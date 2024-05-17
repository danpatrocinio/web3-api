import json
from pathlib import Path

def get_contratc_abi():
    # Metodo para pegar a abi do contrato HelloHardhat
    try:
        file_path = Path(__file__).resolve().parents[3] / "hardhat-hello-world/ignition/deployments/chain-31337/artifacts/HelloHardhat#HelloHardhat.json"
        with open (file_path) as content:
            data = json.load(content)
            return data["abi"]
    except FileNotFoundError:
        raise FileNotFoundError("Verifique se a abi do contrato está no caminho indicado:\n", file_path) 

def get_contract_address():
    # Método para pegar o address do contrato HelloHardhat
    try:
        file_path = Path(__file__).resolve().parents[3] / "hardhat-hello-world/ignition/deployments/chain-31337/deployed_addresses.json"
        with open (file_path, "r") as cinfo:
            data = json.load(cinfo)
            return data["HelloHardhat#HelloHardhat"]
    except FileNotFoundError:
        raise FileNotFoundError("Verifique se o arquivo com o address do contrato está no caminho indicado:\n", file_path)