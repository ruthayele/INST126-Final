import pandas as pd
import os
import sys
current_folder = '/Users/selamawitbeyene/inst123 imports:exports'
csv_path = 'movies - Sheet1.csv'
output_csv_path = 'movies_after_2010.csv'
output_modifying_path = 'adding_columns.csv'
output_adding_row_path = 'adding_row.csv'
df = pd.read_csv(csv_path)


def process_movies(csv_path):
# Read the CSV file into a DataFrame
 print(df)


print('\nThe first task we can do with our dataset is modify the rows! Here we seperate the movie_list column with commas using the space as the delimiter')
# Create a new column with the list of movie names
df['movie_list'] = df['movie'].str.split(' ')




# Display the new column with the list of movie names
print('\nDataFrame with a New Column "movie_list":')
print(df[['movie_id', 'movie', 'movie_list']])




print('\n Using a regular expression, lets check that the release_date column matches the same pattern.')
print('\n this is good to catch any inconsistencies in our data formatt')
# Pattern for YYYY-MM-DD
date_pattern = r'\d{4}-\d{2}-\d{2}'


# Checking if all entries in the 'release_date' column match the specified pattern
matches_pattern = df['release_date'].str.match(date_pattern)


# Displaying the result


print(matches_pattern)




# Pattern with groups for YYYY-MM-DD
print('\n Lets examine further into our data and filter around')
print('\n Here, we are finding all the movies released after 2010 and extracting our findings to a seperate file')
date_pattern_with_groups = r'(\d{4})-(\d{2})-(\d{2})'




condition = df['release_date'] > '2010-01-01'
subset_df = df[condition]
# Display the subset DataFrame
print('\n Subset of the DataFrame (Movies released after 2010):')
print(subset_df)


# Example: Write the modified DataFrame to a new CSV file
output_csv_filename = 'movies_after_2010.csv'
output_csv_path = os.path.join(current_folder, output_csv_filename)
subset_df.to_csv(output_csv_path, index=False)
print(f'\nSubset DataFrame has been written to: {output_csv_path}')




print('/n lets create a dictionary of the movies released before 2010 and extract them to a file')


import json


import sys


# Assuming movies_before_2010_info_dict is your dictionary
movies_before_2010_info_dict = {
   1: {'movie': 'Iron Man', 'director': 'Jon Fave', 'release_date': 'unknown'},
   2: {'movie': 'The Incredible Hulk', 'director': 'Louis Leterrier', 'release_date': 'unknown'}
}


# Check if the dictionary is empty
if not movies_before_2010_info_dict:
   print("Error: The dictionary is empty. Please provide valid data.")
   sys.exit(1)


# Accessing the keys of the dict
keys_list = list(movies_before_2010_info_dict.keys())
print("Keys using keys() method:", keys_list)


# Update release_date
new_release_date = '2010>'
for key, value in movies_before_2010_info_dict.items():
   value['release_date'] = new_release_date


# Display the updated dictionary
print(movies_before_2010_info_dict)


# Export the updated dictionary to a JSON file
output_file_path = 'rest_of_movies.json'
try:
   with open(output_file_path, 'w') as json_file:
       json.dump(movies_before_2010_info_dict, json_file)


   print(f'Updated dictionary has been exported to: {output_file_path}')


except Exception as e:
   print(f"Error: {e}")
   sys.exit(1)






################################################################################
print('\n Manipulating the dataset! Lets add a new column, add some data, and extract to a new file')
print('\n We are going to create a movie ratings column, generate values between 5-10 and randomly assign a score to each movie')
import random


df.to_csv(output_modifying_path, index=False, mode='a', header=os.path.exists(output_modifying_path))




df = pd.read_csv(csv_path)


# Check if the 'movie_rating' column already exists in the DataFrame
if 'movie_rating' not in df.columns:
   df['movie_rating'] = None  # Create the column if it doesn't exist


# Define the range of ratings you want to assign randomly
rating_range = [5.0, 10.0]


# Loop through each row and assign a random rating from the range
for index, row in df.iterrows():
   df.at[index, 'movie_rating'] = round(random.uniform(*rating_range), 1)


# Export the DataFrame to a new CSV file
output_modifying_path = 'adding_columns.csv'
df.to_csv(output_modifying_path, index=False)


# Display a message indicating the successful write
print(f'Results have been appended to: {output_modifying_path}')




print('\n How about adding a new row? lets use tuples to add a new row and export the results to a new file')
def read_csv_and_process(csv_path, output_adding_row_path):
   # Read the CSV file into a DataFrame
   df = pd.read_csv(csv_path)


new_row = (8,'Interstellar', 'Christopher Nolan', 2014-12-10, 8.6)
df.loc[len(df)] = new_row


# Export the updated DataFrame to a new CSV file
df.to_csv(output_adding_row_path, index=False)


# Display the updated DataFrame
print(df)


print('\n What about examing more into the out values? Lets count the length of the movie titles')
def read_csv_and_process(csv_path):
   # Read the CSV file into a DataFrame
   df = pd.read_csv(csv_path)


   # Process the DataFrame or perform any desired operations
   # For example, let's add a new column 'processed' with the length of the movie names
   df['movie length'] = df['movie'].apply(lambda x: len(str(x)))


   # Return the DataFrame and some additional information as a tuple
   return df, len(df), df['movie length'].mean()


# Sample CSV path
csv_path = 'movies - Sheet1.csv'


# Call the function and receive the tuple
result_tuple = read_csv_and_process(csv_path)


# Unpack the tuple into variables
df_result, num_rows, mean_processed_length = result_tuple


# Display the processed DataFrame
print('\nProcessed DataFrame:')
print(df_result)








################################################################################


print('\n lets group parts of strings with regular expressions')
# Applying the regular expression and creating new columns for extracted parts
df[['year', 'month', 'day']] = df['release_date'].str.extract(date_pattern_with_groups)








# Displaying the DataFrame with the new columns
print(df[['release_date', 'year', 'month', 'day']])






import numpy as np
df['squared_movie_id'] = np.square(df['movie_id'])




# Displaying the DataFrame with the new column


print('\n Lets use NumPy to perform vectorized computation on the \'movie_id\' column:')
print(df[['movie_id', 'squared_movie_id']])




#################################################################################################################
print('\n How do you feel about these movies? Here we are going to ask for your personal ratings and add a new column to a new file')


def add_your_movie_ratings(csv_path, ratings_file_path):
   # Read the CSV file into a DataFrame
   df = pd.read_csv(csv_path)


   # Check if the 'your_movie_ratings' column already exists in the DataFrame
   if 'your_movie_ratings' not in df.columns:
       df['your_movie_ratings'] = None  # Create the column if it doesn't exist


   # Read user ratings from a file
   try:
       with open(ratings_file_path, 'r') as ratings_file:
           user_ratings = [line.strip() for line in ratings_file.readlines()]
   except FileNotFoundError:
       print(f"Error: Ratings file '{ratings_file_path}' not found.")
       sys.exit(1)


   # Check if the number of user ratings matches the number of rows in the DataFrame
   if len(user_ratings) != len(df):
       print(f"Error: Number of user ratings provided ({len(user_ratings)}) does not match the number of movies ({len(df)}).")
       sys.exit(1)


   # Assign user ratings to the 'your_movie_ratings' column
   df['your_movie_ratings'] = user_ratings
  
   # Display the updated DataFrame
   print('\nUpdated DataFrame:')
   print(df)
  
   return df


if __name__ == "__main__":
   # Check if the correct number of command-line arguments is provided
   if len(sys.argv) < 4:
       print("Usage: python script.py <csv_path> <ratings_file_path>")
       sys.exit(1)


   # Get command-line arguments
   csv_path = sys.argv[1]
   ratings_file_path = sys.argv[3]
  
   # Check if the input CSV file exists
   if not os.path.exists(csv_path):
       print(f"Error: Input CSV file '{csv_path}' not found.")
       sys.exit(1)


   updated_df = add_your_movie_ratings(csv_path, ratings_file_path)
   print('\n Updated DataFrame:')
   print(updated_df)

print('\n Thats it for today! Thank you\n')

