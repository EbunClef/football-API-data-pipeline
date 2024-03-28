# Movie Data Retrieval and Parsing 🎬🎥

## Overview 👀
This project aims to retrieve movie data from an external API and parse the retrieved JSON data into a more structured format for further processing. The API used in this project provides information about various movies, including their titles, popularity, release dates, average ratings, and vote counts.

## Requirements 📃
- Python 3.x
- Pandas library
- requests library (install via `pip install requests`)
- duck db

## Functionality 📌
- **main_request**: This function sends an HTTP GET request to the specified API endpoint and returns the JSON response.
- **parse_json**: This function takes the JSON response as input, extracts relevant movie information from it, and returns a list of dictionaries containing movie details such as title, popularity, release date, average rating, and vote count.
- **Printing**: The script iterates over the parsed movie data and prints each movie's details to the console.

## Error Handling 💀
- The script includes error handling to catch any exceptions that may occur during the API request or JSON parsing process.
- If an error occurs, the script will print an error message to the console, providing information about the nature of the error.

## Contributing 👍🏾
Contributions are welcome! If you have any suggestions, improvements, or feature requests, please feel free to open an issue or submit a pull request.
