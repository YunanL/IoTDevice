# 🛠️ Blockchain-Based Machine License Interface

This project enables a Raspberry Pi-based system to interact with blockchain-based licenses (represented as NFTs). It provides a GUI for operators to check license availability and start machines if a valid license NFT is present. It also logs machine start events on-chain.

---

## 📦 Features

- ✅ Fetches license NFTs from the blockchain
- ✅ Displays machine license metadata in a clean UI
- ✅ Allows selection of licenses and machine startup
- ✅ Sends transactions to log machine start events on-chain
- ✅ Designed for Raspberry Pi with touch-friendly layout

---

## 📷 Functionalities

**Mint Your Machine License NFT**
Visit our Web3 interface at https://mint-machine-license.vercel.app/ to mint your machine license NFT.
Use any Ethereum-compatible wallet and make sure to switch to the Sepolia Testnet.
To obtain Sepolia ETH for transactions, you can use the following faucet:
👉 https://www.alchemy.com/faucets/ethereum-sepolia

**Minting Process**

Select Machine2 (this project is specifically designed for Machine2).

Enter any desired function (e.g., "cutting", "drilling", etc.).

Choose the desired usage duration.

Click “Mint NFT” to complete the process.

Once minted, the license NFT will automatically be sent to the wallet assigned to Machine2:
0xe78785561Cc77dE5251dfA68027D826CAB1FcFa1
(Each machine has its own unique wallet address.)

**On-Chain License Verification by the Machine**
The IoT device embedded in Machine2 will detect the newly received license NFT and read its metadata directly from the blockchain.
This enables the machine to autonomously determine:

Which function it should perform,

How long the license is valid,

And whether the machine is currently allowed to operate.

**Starting the Machine**
When the client initiates the machine:

They select the desired license from a list (in case multiple licenses have been issued).

Review all license details on the interface.

Press “Start Machine”.

Upon starting, a transaction will be sent on-chain from the Machine2 wallet, logging:

The Machine ID,

The License (NFT) ID, and

The timestamp of machine activation.

---

## 📁 Folder Structure

```
├── machine_ui.py             # Main UI interface
├── checklicensedetails.py   # Lists NFTs owned by wallet
├── start_machine.py         # Sends transaction to log machine start
├── startIoT.py              # Start the IoT Device 
├── requirements.txt         # Python dependencies
├── license.desktop          # Launchable app shortcut (for Raspberry Pi GUI)
├── README.md
```

---

## ⚙️ Requirements

- Raspberry Pi (or any Linux machine)
- Python 3.7+
- An Ethereum Blockchain wallet (MetaMask) 
- Access to a Web3 provider (e.g., Infura, Alchemy)
- NFTs minted from the smart contract must include:
  - `Machine ID`
  - `Function`
  - `Usage Duration`
  - `Expires On`
  - `Token ID`

---

## 🧪 Setup Instructions (on Linux Device)

### 1. Clone the repo

```bash
git clone https://https://github.com/YunanL/IoTDevice.git
cd -/IoTDevice
```

### 2. Create and activate a Python virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🖥️ Running the IoT

```bash
python3 startIoT.py
```

Or from Raspberry Pi desktop by creating a `.desktop` file 
(by Exec'/home/pi/myenv/bin/python' use the python on your env path
and '/home/pi/startIoT.py' should be the path where startIoT is located):

```ini
[Desktop Entry]
Name=Machine License UI
Comment=Raspberry Pi Machine NFT Checker
Exec=/home/pi/myenv/bin/python /home/pi/startIoT.py
Icon=computer
Terminal=false
Type=Application
Categories=Utility;
```

---

## 🛡️ Advantages Over Traditional Licensing

| Traditional Licensing | Blockchain Licensing |
|------------------------|----------------------|
| Centralized server | Decentralized ledger |
| Hard to audit | Fully transparent |
| Prone to tampering | Tamper-proof |
| Manual license revocation | Automatically expires on-chain |
| Difficult to transfer | NFT licenses are transferable |

---

## 🤝 Contributors

- **Yunan Li** – Department LC IP LTA STA, Siemens  
- Feel free to open issues or submit pull requests!

---

## 📜 License

This project is open-sourced under the [MIT License](LICENSE).
