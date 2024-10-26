# Process Outline for Fetching Event Logs

## Overview
This document outlines the steps taken to fetch event logs from the Base chain using the BaseScan API and save the relevant information for further analysis.

## Steps Taken
1. **Setup**: Defined the API endpoint and parameters, including the contract address and API key.
2. **API Request**: Made a request to the BaseScan API to fetch logs related to the specified contract.
3. **Response Handling**: Processed the API response to extract relevant log details.
4. **Data Storage**: Saved the logs output to a JSON file (`logs_output.json`) and documented the event logs in a Markdown file (`event_logs_info.md`).
5. **Script Creation**: Created a Python script (`fetch_event_logs.py`) to automate the fetching of logs and saving the output.

## Key Learnings
- Understanding how to interact with blockchain APIs to retrieve event logs.
- Importance of structuring data for easy access and analysis.
- Automation of processes using scripts to streamline repetitive tasks.

## Future Improvements
- Consider implementing error handling in the script to manage API request failures.
- Explore additional features of the BaseScan API for more comprehensive data retrieval.

## Updated Steps
- Created a new script (`fetch_proposals.py`) to extract proposal details from logs and save them to a JSON file.
- The script checks for specific event topics related to proposals and extracts relevant information.
## Updated Steps
- Created a new script (`fetch_proposals_with_call_data.py`) to extract proposal details and call data from logs and save them to a JSON file.
- The script checks for specific event topics related to proposals and extracts relevant information including call data.
