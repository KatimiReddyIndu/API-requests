# Project: Fetch and Identify Citations from API

This project involves fetching paginated data from an API endpoint, processing the data to identify specific citations, and then outputting the results in a structured format.

## Requiremen
+ Python 3.x
+ requests library

You can install the required library using pip:pip install requests

# Project Structure

## fetch_paginated_data(api_url): 
This function fetches data from the API in a paginated manner.

## identify_citations(data):
This function processes the fetched data to identify and extract citations.

## main():
The main function that orchestrates the fetching and processing of data, and then prints the results

# Functions
This project involves fetching paginated data from an API endpoint, processing the data to identify specific citations, and then outputting the results in a structured format.

## Parameters
api_url (str): The URL of the API to fetch data from.


## Returns:
results (list): A list of all fetched data items.

## Behavior:
+ The function makes GET requests to the API, incrementing the page number with each request.

+ If a rate limit (status code 429) is enc↓ntered, the function waits for 5 seconds before retrying.
+ If any other status code is received, the function prints an error message and stops.

+ Fetched data for each page is appended to the results list.

+ If the response contains no data, the function stops.

# identify_citations(data)

This function identifies citations within the fetched data.

## Parameters:

data (list): The data fetched from the API.

## Returns:

citations_list (list): A list of dictionaries containing the response text and corresponding citations.

## Behavior:

+ The function iterates over each item he data list
+ For each item, it extracts the response text and sources.
+ It then identifies citations by checking if each source's context is present in the response text.
+ If citations are found, they are appended to the citations list.

# main()

The main function that orchestrates the workflow.

## Behavior:

+ Calls fetch_paginated_data to fetch the data.

+ Calls identify_citations to process the fetched data.

+ Prints the citations list in a structured JSON format.
# Usage

+ Ensure you have Python 3.x and the requests' library installed.
+ Replace api_url in the 'main' function with the actual API endpoint.
+ Run the script using Python:

## bash
python script_name.py

