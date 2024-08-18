import requests
from bs4 import BeautifulSoup
import csv

# Define the base URL and the teams
base_url = "https://www.profootballarchives.com/"
teams = [
    'ari', 'atl', 'bal', 'buf', 'car', 'chi', 'cin', 'cle', 'dal', 'den', 'det', 'gb', 'hou', 'ind', 'jax',
    'kc', 'lv', 'lac', 'lar', 'mia', 'min', 'ne', 'no', 'nyg', 'nyj', 'phi', 'pit', 'sf', 'sea', 'tb', 'ten', 'wsh'
]

team_names = {
    'ari': 'Arizona Cardinals', 'atl': 'Atlanta Falcons', 'bal': 'Baltimore Ravens', 'buf': 'Buffalo Bills',
    'car': 'Carolina Panthers', 'chi': 'Chicago Bears', 'cin': 'Cincinnati Bengals', 'cle': 'Cleveland Browns',
    'dal': 'Dallas Cowboys', 'den': 'Denver Broncos', 'det': 'Detroit Lions', 'gb': 'Green Bay Packers',
    'hou': 'Houston Texans', 'ind': 'Indianapolis Colts', 'jax': 'Jacksonville Jaguars', 'kc': 'Kansas City Chiefs',
    'lv': 'Las Vegas Raiders', 'lac': 'Los Angeles Chargers', 'lar': 'Los Angeles Rams', 'mia': 'Miami Dolphins',
    'min': 'Minnesota Vikings', 'ne': 'New England Patriots', 'no': 'New Orleans Saints', 'nyg': 'New York Giants',
    'nyj': 'New York Jets', 'phi': 'Philadelphia Eagles', 'pit': 'Pittsburgh Steelers', 'sf': 'San Francisco 49ers',
    'sea': 'Seattle Seahawks', 'tb': 'Tampa Bay Buccaneers', 'ten': 'Tennessee Titans', 'wsh': 'Washington Commanders'
}
years = range(1999, 2024)

def get_roster_for_team_and_year(year, team):
    url = f"{base_url}{year}nfl{team}.html"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        roster_section = soup.find('div', {'class': 'stats'})

        if roster_section:
            player_names = []
            for item in roster_section.find_all('a'):
                name = item.get_text(strip=True)
                if name:  # Check if the name is not empty
                    player_names.append(name)
            return player_names
        else:
            print(f"No roster found for {team} in {year}.")
            return []
    else:
        print(f"Failed to fetch page for {team} in {year}. Status code: {response.status_code}")
        return []

def scrape_and_save_rosters_to_csv():
    csv_file = 'nfl_rosters_1999_2002.csv'
    
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Player Name', 'Year', 'Team'])

        for year in years:
            for team in teams:
                print(f"Fetching roster for {team_names[team]} in {year}...")
                roster = get_roster_for_team_and_year(year, team)
                if roster:
                    for player in roster:
                        writer.writerow([player, year, team_names[team]])
                else:
                    print(f"No players found for {team_names[team]} in {year}.")

    print(f"Data successfully written to {csv_file}")

if __name__ == "__main__":
    scrape_and_save_rosters_to_csv()
