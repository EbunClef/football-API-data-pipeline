import auth
import dlt
import duckdb
from dlt.sources.helpers import requests

def main_request(page):
    try:
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&sort_by=popularity.desc&year=2023&page={page}"
        response = requests.get(url, headers=auth.headers)
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
all_movies = []

for page in range(1, 21):  # Pages from 1 to 20
    data = main_request(page)
    if data is not None:
        movies_on_page = parse_json(data)
        all_movies.extend(movies_on_page)
# print(page)
# print("Total movies retrieved:", len(all_movies)) 

# loading the data into duckdb

pipeline = dlt.pipeline(
    pipeline_name='movie_api_pipeline',
    destination='duckdb',
    dataset_name='all_movies',
)

# The response contains a list of movies
load_info = pipeline.run(
    all_movies,
    table_name="movies",
    write_disposition="replace"  # <-- Add this line
)

# print(load_info)


