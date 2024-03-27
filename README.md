# Movie Data Retrieval and Parsing

## Overview
This project aims to retrieve movie data from an external API and parse the retrieved JSON data into a more structured format for further processing. The API used in this project provides information about various movies, including their titles, popularity, release dates, average ratings, and vote counts.

## Requirements
- Python 3.x
- Pandas library
- requests library (install via `pip install requests`)
- duck db

## Usage
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Ensure that you have Python 3.x installed.
4. Install the required dependencies using the following command:
    ```
    pip install -r requirements.txt
    ```
5. Modify the `auth.url` and `auth.headers` variables in the `main_request` function to point to the desired API endpoint and include any required headers for authentication.
6. Run the Python script `main.py` using the following command:
    ```
    python main.py
    ```
7. The script will fetch data from the API using the `main_request` function and parse the JSON response using the `parse_json` function.
8. The parsed movie data will be printed to the console, displaying the title, popularity, release date, average rating, and vote count for each movie.

## Functionality
- **main_request**: This function sends an HTTP GET request to the specified API endpoint and returns the JSON response.
- **parse_json**: This function takes the JSON response as input, extracts relevant movie information from it, and returns a list of dictionaries containing movie details such as title, popularity, release date, average rating, and vote count.
- **Printing**: The script iterates over the parsed movie data and prints each movie's details to the console.

## Error Handling
- The script includes error handling to catch any exceptions that may occur during the API request or JSON parsing process.
- If an error occurs, the script will print an error message to the console, providing information about the nature of the error.

## Contributing
Contributions are welcome! If you have any suggestions, improvements, or feature requests, please feel free to open an issue or submit a pull request.
