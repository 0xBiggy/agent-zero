import json

# Load the logs output from the JSON file
with open('gov/logs_output.json', 'r') as file:
    logs = json.load(file)

# Initialize a list to store proposal details
proposals = []

# Iterate through the logs to find proposal-related entries
for log in logs['result']:
    # Check for 'ProposalCreated' event topic
    if log['topics'][0] == '0xc565b045403dc03c2eea82b81a0465edad9e2e7fc4d97e11421c209da93d7a93':
        proposal_id = log['data']  # Extract proposal ID from data
        proposal_description = 'Extracted description based on log data'  # Placeholder for actual description extraction
        proposals.append({
            'id': proposal_id,
            'description': proposal_description,
            'transactionHash': log['transactionHash'],
            'blockNumber': log['blockNumber'],
        })

# Save the proposals to a file for reference
with open('gov/proposals_extracted.json', 'w') as output_file:
    json.dump(proposals, output_file, indent=4)
