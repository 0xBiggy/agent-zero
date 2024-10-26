# Event Logs and Script

## Event Logs

1. **Log Address**: 0x0395fa5e53e2a9c9528539360324da422708acbd
   - **Topics**: [0xc565b045403dc03c2eea82b81a0465edad9e2e7fc4d97e11421c209da93d7a93]
   - **Data**: 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
   - **Block Number**: 0x12fd498
   - **Transaction Hash**: 0xc9e86b6a48f304e4e144854ab28ed6d30af619b8f25bc9f5a7db63a49280f760

2. **Log Address**: 0x0395fa5e53e2a9c9528539360324da422708acbd
   - **Topics**: [0x7e3f7f0708a84de9203036abaa450dccc85ad5ff52f78c170f3edb55cf5e8828]
   - **Data**: 0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000b2fa
   - **Block Number**: 0x12fd498
   - **Transaction Hash**: 0xc9e86b6a48f304e4e144854ab28ed6d30af619b8f25bc9f5a7db63a49280f760

## Script to Fetch Event Logs

```python
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
```

