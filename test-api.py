import api_request_dlt
import duckdb
import pandas as pd


# Connect to DuckDB
con = duckdb.connect(database='movie_api_pipeline.duckdb')

# Count the number of movies
result = con.execute("SELECT COUNT(*) FROM all_movies.movies")
# print("Total number of movies:", result.fetchone()[0])

# Calculate the average popularity of movies
result = con.execute("SELECT ROUND(AVG(popularity),2) FROM all_movies.movies")
# print("Average popularity of movies:", result.fetchone()[0])

# Find the highest-rated movie
result = con.execute("SELECT title, MAX(vote_average) FROM all_movies.movies GROUP BY title")
highest_rated_movie = result.fetchone()
# print("Highest-rated movie:", highest_rated_movie[0], "with a rating of", highest_rated_movie[1])

# view the data table
result = con.execute("SELECT * FROM all_movies.movies LIMIT 10")
# print(result.fetchall())

# further analysis
result = con.execute("SELECT title, popularity, vote_count FROM all_movies.movies ORDER BY vote_count DESC LIMIT 10")
df = pd.DataFrame(result.fetchall())
print(df)

# Close the connection
con.close()