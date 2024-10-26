import requests

# Define the API endpoint and parameters
api_key = '5JGRDZGJ2875NQD5Q2RIJ82MZNPP3FGNHB'
contract_address = '0x0395FA5e53e2a9C9528539360324Da422708aCbD'
from_block = 'earliest'
to_block = 'latest'

# Construct the API URL
url = f'https://api.basescan.org/api?module=logs&action=getLogs&address={contract_address}&fromBlock={from_block}&toBlock={to_block}&apikey={api_key}'

# Make the API request
response = requests.get(url)

# Print the response
print(response.json())
