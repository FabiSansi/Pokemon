import requests
import pandas as pd

# Step 1: Load the CSV file
csv_file = "pokemon_stats.csv"
df = pd.read_csv(csv_file)

# Check if the required columns already exist, if not, add them
columns_to_add = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']
for col in columns_to_add:
    if col not in df.columns:
        df[col] = None  # Initialize with None

# Step 2: Function to get Pokémon stats by ID from the API
def get_pokemon_stats(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
        return stats
    else:
        return None

# Step 3: Update the DataFrame with stats for each Pokémon ID
for index, row in df.iterrows():
    pokemon_id = row['id']  # Assuming 'id' is the column with the Pokémon IDs
    stats = get_pokemon_stats(pokemon_id)
    
    if stats:
        df.at[index, 'hp'] = stats.get('hp', None)
        df.at[index, 'attack'] = stats.get('attack', None)
        df.at[index, 'defense'] = stats.get('defense', None)
        df.at[index, 'special-attack'] = stats.get('special-attack', None)
        df.at[index, 'special-defense'] = stats.get('special-defense', None)
        df.at[index, 'speed'] = stats.get('speed', None)

# Step 4: Save the updated DataFrame back to CSV
df.to_csv(csv_file, index=False)

print("CSV updated with Pokémon stats.")
