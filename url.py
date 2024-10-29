import pandas as pd

# Load the CSV file
file_path = 'pokemon_url_data.csv'
df = pd.read_csv(file_path)

# Create the URL using the id column
df['url'] = df['id'].apply(lambda x: f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/{x}.png')

# Save the updated dataframe to a new CSV file
output_file = 'pokemon_url_data_with_urls.csv'
df.to_csv(output_file, index=False)

output_file
