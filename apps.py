import requests
import json
import time

def fetch_paginated_data(api_url):
    results = []
    page = 1
    while True:
        try:
            response = requests.get(api_url, params={'page': page})
            if response.status_code == 429:
                print(f"Rate limit exceeded on page {page}. Retrying after a delay.")
                time.sleep(5)  # Sleep for 5 seconds before retrying
                continue
            elif response.status_code != 200:
                print(f"Error: Received status code {response.status_code} for page {page}")
                break

            try:
                data = response.json()
            except json.JSONDecodeError:
                print(f"Error decoding JSON for page {page}")
                break

            print(f"Fetched data for page {page}: {data}")  # Debug print

            if not data:
                break

            results.extend(data)
            page += 1
            
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {e}")
            break
    
    return results

def identify_citations(data):
    citations_list = []

    for item in data:
        if not isinstance(item, dict):
            print(f"Unexpected data format: {item}")
            continue

        response_text = item.get('response')
        sources = item.get('sources', [])
        citations = []

        if not response_text or not sources:
            continue  

        for source in sources:
            url = source.get('url')
            if url:
                citations.append({'id': source.get('id'), 'url': url})
        
        if citations:
            citations_list.append({
                'response': response_text,
                'citations': citations
            })
    return citations_list

def main():
    api_url = 'https://devapi.beyondchats.com/api/get_message_with_sources'
    data = fetch_paginated_data(api_url)
    citations_list = identify_citations(data)

    # Output the result
    print(json.dumps(citations_list, indent=2))
    
if __name__ == "__main__":
    main()
