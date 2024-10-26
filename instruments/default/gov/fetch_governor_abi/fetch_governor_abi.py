import requests
import os
import json

# Create the 'gov' folder if it doesn't exist
folder_name = 'gov'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# BaseScan API endpoint for getting contract ABI on the Base mainnet
api_key = '5JGRDZGJ2875NQD5Q2RIJ82MZNPP3FGNHB'
contract_address = '0x0395FA5e53e2a9C9528539360324Da422708aCbD'
url = f'https://api.basescan.org/api?module=contract&action=getabi&address={{contract_address}}&apikey={{api_key}}'

response = requests.get(url)
abi = response.json()

if abi['status'] == '1':
    # Save the ABI to a file in the 'gov' folder
    with open(os.path.join(folder_name, 'governor_abi.json'), 'w') as abi_file:
        json.dump(abi['result'], abi_file)
    print('ABI saved successfully.')
else:
    print('Error:', abi['message'])
