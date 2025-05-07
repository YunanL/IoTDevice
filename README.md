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

First thing first, you need to mint an Machine License NFT at https://mint-machine-license.vercel.app/,
this is a web3 Website we developed to mint the license, you can use any ethereum wallet and switch the 
network to sepolia testnet, and get some sepolia eth from here: https://www.alchemy.com/faucets/ethereum-sepolia
now you are ready to mint, select Machine2 (this project is designed for Machine2), write random function as
you wish, and select Duration, then click 'Mint NFT'. The NFT will be minted and it will directly send to the 
wallet of Machine2. 

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
