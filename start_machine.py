from web3 import Web3
import config
configs = config.config

INFURA_URL = configs["INFURA_URL"]
SENDER_ADDRESS = configs["Machine2"]
PRIVATE_KEY = configs["Machine2PK"]
RECEIVER_ADDRESS = configs["Receiver"]

web3 = Web3(Web3.HTTPProvider(INFURA_URL))
sender = web3.to_checksum_address(SENDER_ADDRESS)
receiver = web3.to_checksum_address(RECEIVER_ADDRESS)

def log_machine_start(machine_id: int, nft_id: int):
    try:
        message = f"machine:{machine_id};nft:{nft_id}"
        data = web3.to_hex(text=message)

        nonce = web3.eth.get_transaction_count(sender)

        tx = {
            'nonce': nonce,
            'to': receiver,
            'value': 0, 
            'gas': 50000 + len(data) * 10,
            'gasPrice': web3.to_wei("500", "gwei"),
            'data': data
        }

        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        print(f"✅ Sent: machine_id={machine_id}, nft_id={nft_id}")
        print(f"🔗 TX: {web3.to_hex(tx_hash)}")
        return web3.to_hex(tx_hash)

    except Exception as e:
        print(f"❌ Error: {e}")
        return None
