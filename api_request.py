import auth
import requests
import json


def main_request():
    try:
        response = requests.get(auth.url, headers=auth.headers)
        response.raise_for_status()  # Raise an exception for HTTP errors (status codes >= 400)
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

def parse_json(response):
    if response is None:
        return None
    
    charlist = []
    for movie in response.get('results', []):
        char = {
            'title': movie.get('title'),
            'popularity': movie.get('popularity'),
            'release_date': movie.get('release_date'),
            'vote_average': movie.get('vote_average'),
            'vote_count': movie.get('vote_count')
        }
        charlist.append(char)
    return charlist

# Fetch data from the API
data = main_request()
if data is not None:
    # Parse the JSON response
    characters = parse_json(data)
    if characters is not None:
        # Print parsed data
        for char in characters:
            print(char)
    else:
        print("No data to parse.")
else:
    print("No data fetched from the API.")
