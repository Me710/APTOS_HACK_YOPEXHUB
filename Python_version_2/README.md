# Yopex Aptos - Project's Marketplace

This project is a Python implementation of the Yopex smart contract on the Aptos blockchain. It demonstrates creating projects, listing projects, and buying projects between users using the Aptos SDK.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git

## 1 - Clone the Repository

To get started, clone the repository to your local machine:

```
   git clone https://github.com/Me710/APTOS_HACK_YOPEXHUB.git
   cd APTOS_HACK_YOPEXHUB\Python_version
```

## 2 - Set Up a Virtual Environment (Optional but Recommended)


```
   python -m venv env
```

Activate the virtual environement
- On mac/linux
```
source env/bin/activate
```
- On windows
```
env\activate\Scripts
```

## Install Dependencies

Install the required packages using pip:

```
pip install -r requirements.txt
```
If you don't have a `requirements.txt` file, create one with the following content:

`PyYAML==6.0`
`requests`
`aptos-sdk==0.4.0`

Then run the install command above.

## Initialise Aptos

```
aptos init
```
A config/config.yaml will be generated having your private and public keys..

## Configure the Project

Update the `src/utils/constants.py` file with your Aptos module address and other necessary constants:

```
NODE_URL = "https://fullnode.devnet.aptoslabs.com/v1"
FAUCET_URL = "https://faucet.devnet.aptoslabs.com"
YOPEX_MODULE_ADDRESS = "your_module_address_here"
YOPEX_MODULE_NAME = "yopex"
```

In main.py, update Alice's private key:

```
alice = Account.load_key("your_private_key_here")

```

## Run the Project

To run the project, execute:

```
python main.py
```