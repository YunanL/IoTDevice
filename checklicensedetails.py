from web3 import Web3
import base64
import json
import requests
import config
configs = config.config

INFURA_URL = configs["INFURA_URL"]
NFT_contract = configs["NFT_contract"]
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

contract_address = Web3.to_checksum_address(NFT_contract)  
wallet_address = configs["Machine2"]

with open("nftAbi.json", "r") as file:
    nft_abi = json.load(file)

contract = web3.eth.contract(address=contract_address, abi=nft_abi)

def decode_metadata(uri):
    if uri.startswith("data:application/json;base64,"):
        try:
            decoded = base64.b64decode(uri.split(",")[1]).decode("utf-8")
            return json.loads(decoded)
        except Exception as e:
            return {"error": f"Base64 decode error: {str(e)}"}
    elif uri.startswith("http"):
        try:
            return requests.get(uri).json()
        except Exception as e:
            return {"error": f"HTTP fetch error: {str(e)}"}
    else:
        return {"error": "Unknown metadata format"}

def list_owned_tokens():
    print(f"🔎 Checking NFTs in wallet: {wallet_address}")
    wallet_checksum = Web3.to_checksum_address(wallet_address)
    wallet_topic = "0x" + wallet_checksum[2:].rjust(64, "0")

    event_signature_hash = web3.keccak(text="Transfer(address,address,uint256)")
    
    try:
        logs = web3.eth.get_logs({
            "fromBlock": 8082853,
            "toBlock": "latest",
            "address": contract_address,
            "topics": [event_signature_hash, None, wallet_topic]
        })
    except Exception as e:
        print(f"Error fetching logs: {e}")
        return []

    token_ids = set()
    for log in logs:
        try:
            token_id = int(log["topics"][3].hex(), 16)
            current_owner = contract.functions.ownerOf(token_id).call()
            if current_owner.lower() == wallet_address.lower():
                token_ids.add(token_id)
        except Exception:
            continue

    nft_metadata_list = []

    for token_id in token_ids:
        try:
            uri = contract.functions.tokenURI(token_id).call()
            metadata = decode_metadata(uri)
            if isinstance(metadata, dict):
                metadata["token_id"] = token_id
                metadata["uri"] = uri
                nft_metadata_list.append(metadata)
        except Exception as e:
            print(f"Token {token_id} error: {e}")

    return nft_metadata_list


if __name__ == "__main__":
    output = list_owned_tokens()
    print(output)