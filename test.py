import os
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()
infura_key = os.environ.get("INFURA")
pokt_network_eth = os.environ.get("POKT_NETWORK_ETH")
pokt_network_harmony = os.environ.get("POKT_NETWORK_HARMONY")
moralis_key = os.environ.get("MORALIS")

exponent = 10 **18

w3_eth = Web3(Web3.HTTPProvider(infura_key))
w3_one = Web3(Web3.HTTPProvider(pokt_network_harmony))

lp_address = "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9"
town_star_address = "0x3Dd98C8A089dBCFF7e8FC8d4f532BD493501Ab7F"
test_address = "0xf34f0420b588b6cf956f66beabab3f75deb10a63"

print(w3_eth.eth.get_block(12345))
print(w3_one.eth.get_block(12345))
checksummed_contract = w3_eth.toChecksumAddress(town_star_address)
checksummed_address = w3_eth.toChecksumAddress(test_address)

with open("abis/TOWN.json") as f:
    town_star = json.load(f)

contract = w3_eth.eth.contract(address = checksummed_contract, abi = town_star)
data = contract.functions.balanceOf(checksummed_address).call()

print(data)
