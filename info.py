import requests
import time
import csv

# URL for fetching all Pokémon with limit and offset
BASE_URL = "https://pokeapi.co/api/v2/pokemon?offset=1000&limit=2001"

# Fetch data from the base API
def fetch_all_pokemon():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Fetch details for each Pokémon
def fetch_pokemon_details(pokemon_url):
    response = requests.get(pokemon_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching details for {pokemon_url}: {response.status_code}")
        return None

# Function to extract Pokémon data
def extract_pokemon_data(pokemon_details):
    pokemon_data = {
        'id': pokemon_details['id'],
        'name': pokemon_details['name'],
        'height': pokemon_details['height'],
        'weight': pokemon_details['weight'],
        'primary_type': pokemon_details['types'][0]['type']['name'] if pokemon_details['types'] else None,
        'secondary_type': pokemon_details['types'][1]['type']['name'] if len(pokemon_details['types']) > 1 else None,
        'moves': ', '.join([move['move']['name'] for move in pokemon_details['moves']]),  # Joining moves as a string
    }
    return pokemon_data

# Save Pokémon data to a CSV file
def save_to_csv(pokemon_data_list, filename="pokemon_data.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=pokemon_data_list[0].keys())
        writer.writeheader()  # Write header
        for pokemon_data in pokemon_data_list:
            writer.writerow(pokemon_data)  # Write each Pokémon's data as a row

# Main process
def main():
    all_pokemon = fetch_all_pokemon()
    if all_pokemon:
        pokemon_data_list = []
        
        # Loop through all Pokémon and fetch their details
        for pokemon in all_pokemon:
            pokemon_details = fetch_pokemon_details(pokemon['url'])
            if pokemon_details:
                pokemon_data = extract_pokemon_data(pokemon_details)
                pokemon_data_list.append(pokemon_data)  # Add to list
                
            time.sleep(0.5)  # To prevent overwhelming the API with requests

        # Save all Pokémon data to CSV
        save_to_csv(pokemon_data_list)
        print(f"Data saved to pokemon_data.csv")

if __name__ == "__main__":
    main()
