This script performs various operations on a movie dataset using Python and pandas. This is intended for people with an interest in data science techniques and explores the ways we can manipulate a CSV file to extract meaningful insights. 

Users are given a CSV file containing data on movies and the program will generate an interactive dashboard that includes:  
1. data overview
2. String manipulation
3. Options to perform operations like extracting specific substrings, counting occurrences, or converting cases
3. Interactive dashboard
4. Use pandas for data manipulation 


How users interact:
- Users can run program from the command line
- Users can input specified answers to create a new column of data 


## Requirements

- Python 3.x
- pandas library

## Usage

1. Clone the repository:

   ```bash
   git clone <https://github.com/ruthayele/final-project-movies.gitrepository_url>

cd <Final - folder >
pip install pandas 
python script.py <csv_path> <output_csv_path><output_modifying_path><output_adding_row_path>

Script Overview

The script performs the following operations:

1. Separating Movie List: Creates a new column 'movie_list' by splitting the 'movie' column based on spaces.
Checking Release Date Format:

2. Uses regular expressions to check if all entries in the 'release_date' column match the YYYY-MM-DD pattern.

3. Filtering Movies Released After 2010: Creates a subset DataFrame with movies released after 2010.
Exporting Subset to CSV:

4. Writes the subset DataFrame to a new CSV file ('movies_after_2010.csv').

5. Creating a Dictionary: Creates a dictionary ('movies_before_2010_info_dict') with movie information released before 2010.

6. Updates the release dates in the dictionary.

7. Exporting Dictionary to JSON: Exports the updated dictionary to a JSON file ('rest_of_movies.json').

8. Adding Movie Ratings Column: Adds a new 'movie_rating' column with random values between 5 and 10.

9. Adding a New Row: Adds a new row to the DataFrame using tuples. Exports the updated DataFrame to a new CSV file ('adding_row.csv').

10. Processing Movie Titles: Adds a new column 'movie length' with the length of movie titles.

11. Performing Vectorized Computation: Uses NumPy to perform vectorized computation on the 'movie_id' column.

12. User Ratings: Accepts user ratings from a file. Adds a new column 'your_movie_ratings' with user ratings.

13. Exporting Results: Displays the updated DataFrame. Exits the script.

License: This project is licensed under the MIT License - see the LICENSE.md file for details.