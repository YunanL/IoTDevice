from web3 import Web3
import base64
import json
import requests
from datetime import datetime, timezone
import config
configs = config.config

INFURA_URL = configs["INFURA_URL"]
NFT_contract = configs["NFT_contract"]
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

contract_address = Web3.to_checksum_address("0x0db3bbc19549f724c7da68edbdf4048afc6a242d")
wallet_address = "0x35f9a271236232583747698a82c22dd6296aCdFc"

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

def check_nft_status():
    print(f"🔍 Checking NFTs for wallet: {wallet_address}")
    wallet_topic = "0x" + wallet_address[2:].rjust(64, '0')
    event_signature = web3.keccak(text="Transfer(address,address,uint256)")

    try:
        logs = web3.eth.get_logs({
            "fromBlock": 8082853,
            "toBlock": "latest",
            "address": contract_address,
            "topics": [event_signature, None, wallet_topic]
        })
    except Exception as e:
        print(f"Failed to get logs: {e}")
        return

    token_ids = set()
    for log in logs:
        try:
            token_id = int(log["topics"][3].hex(), 16)
            owner = contract.functions.ownerOf(token_id).call()
            if owner.lower() == wallet_address.lower():
                token_ids.add(token_id)
        except:
            continue

    if not token_ids:
        print("No NFTs currently owned.")
        return

    print(f"Found {len(token_ids)} NFT(s).")

    for token_id in token_ids:
        try:
            uri = contract.functions.tokenURI(token_id).call()
            metadata = decode_metadata(uri)
            expires_attr = next((a for a in metadata["attributes"] if a["trait_type"] == "Expires On"), None)

            if expires_attr:
                expires = datetime.fromisoformat(expires_attr["value"].replace("Z", "+00:00"))
                now = datetime.now(timezone.utc)
                status = "Usable" if now < expires else "Expired"

                print(f"\nToken ID: {token_id}")
                print(f"Expires On: {expires.isoformat()}")
                print(f"Status: {status}")
            else:
                print(f"No 'Expires On' attribute found in token {token_id}")
        except Exception as e:
            print(f"Error with token {token_id}: {e}")

if __name__ == "__main__":
    check_nft_status()
