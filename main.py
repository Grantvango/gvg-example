import requests
import json

# Grab list of players -> https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/teams/18/athletes?limit=5
# Save all 5 players in player object (example endpont: https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/athletes/3728305?lang=en&region=us)
# Update one of the players age to 99
# Remove one of the players from list
# Save player object to file
# Upload player object file to Github

# Define the headers, including the User-Agent
headers = {
    'User-Agent': 'test'
}

def fetch_players():
    # Define the URL
    url = 'https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/teams/18/athletes?limit=5'
    
    try:
        # Make the GET request
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return data
        else:
            print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        # Handle exceptions that may occur during the request
        print(f"An error occurred: {e}")
        return None

def generate_list_of_players():

    players = []

    # Grab list of players
    data = fetch_players()
    for item in data['items']:
        url = item['$ref']
        req = requests.get(url, headers=headers)
        res = json.loads(req.text)
        players.append(res)

    return players

def edit_lisit_of_players():
    players = generate_list_of_players()
    for item in players:
        if item['fullName'] == 'Johnathan Abram':
            item['age'] = 99
        if item['fullName'] == 'Paulson Adebo':
            players.remove(item)

    return players

new_list = edit_lisit_of_players()
print(len(new_list)) # Should be 4

with open('players.txt', 'w') as f:
    for line in new_list:
        f.write(f"{line}\n")
