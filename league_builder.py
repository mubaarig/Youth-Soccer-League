"""

Author @ Mubarig CISMAN

Build a Youth Soccer League - Treahouse Techdegree Python Web Development
In your Python program, read the data from the supplied CSV file.
Store that data in an appropriate data type so that it can be used in the next task.
Read Players data from the supplied CSV File and divide players data into three
teams.
experienced players should be equally distributed among teams, putting those with experience as 
first in teams. The balanced and equally distributed Team names and member's Info should be written 
to a text File respectively.

Extra Credit.
    Creating 18 text Files for each Player of the Team.
    Creating a personalized letter to the guardians of each player 
    on the team. The text should contain the the following Info's
        Team Placement of the Child and Practice time.
    The final output text should be  player’s name as the name of the file,
    in lowercase and with underscores and ending in .txt and its contents are:        
        player's name, team name, guardians name and practice date/time
        
Program Output:
    a) the program outputs a text file named -- teams.txt -- that contains the league roster listing the team name,
     and each player on the team including the player's information: name, whether they've played soccer 
     before and their guardians' names. 
    2.Extra Credit 18 letters, one to each player's guardian(s), Files should be named as follows
      the player’s name as the name of the file, in lowercase and with underscores and ending in .txt.
       For example, firstname_lastname.txt.
    
       
  teams.txt: output 
  
Sharks
  Joe Smith, YES, 42, Jim and Jan Smith
  Jill Tanner, YES, 36, Clara Tanner
  Bill Bon, YES, 43, Sara and Jenny Bon
  Eva Gordon, NO, 45, Wendy and Mike Gordon
  Matt Gill, NO, 40, Charles and Sylvia Gill
  Kimmy Stein, NO, 41, Bill and Hillary Stein

Dragons:
  Sammy Adams, NO, 45, Jeff Adams
  Karl Saygan, YES, 42, Heather Bledsoe
  Suzane Greenberg, YES, 44, Henrietta Dumas
  Sal Dali, NO, 41, Gala Dali
  Joe Kavalier, NO, 39, Sam and Elaine Kavalier
  Ben Finkelstein, NO, 44, Aaron and Jill Finkelstein

Raptors:
  Diego Soto, YES, 41, Robin and Sarika Soto
  Chloe Alaska, NO, 47, David and Jamie Alaska
  Arnold Willis, NO, 43, Claire Willis
  Phillip Helm, YES, 44, Thomas Helm and Eva Jones
  Les Clay, YES, 42, Wynonna Brown
  Herschel Krustofski, YES, 45, Hyman and Rachel Krustofski
  
"""

import csv

CSV_SUPPLIED = 'soccer_players.csv'

LETTER_TEXT = """Dear {},

Your child, {}, will be playing for the {}!
The first practice session is on {}.

We will see you there!
Coach
"""

# Team names Sharks, Dragons and Raptors stored in a list
TEAM_NAMES = ['Sharks', 'Dragons', 'Raptors']

PRACTICE_TIME = {
    'Sharks': "June 20, 2017 @ 3:00PM",
    'Dragons': "June 19, 2017 @ 2:00PM", 
    'Raptors': "June 21, 2017 @ 2:00PM",
}

def get_players_data_from_csv(csv_file=CSV_SUPPLIED):
    """Read a CSV datafile, convert player data to dictionary data type
       and return list of player dicts
    """
    with open(csv_file) as csv_fl:
        players_reader = csv.DictReader(csv_fl)
        players = list(players_reader)
        return players

def create_team(name):
    """
    Generate dictionary representation of the Team    
    """
    return {'name': name, 'players': []}

def create_team_roster(teams):
    """Write team names and assigned players to text file 
    teams.txt
    """
    filename = "teams.txt"
    with open(filename, 'w') as file:
        for team in teams:
            # write team name
            file.write("{}:\n".format(team['name']))
            
            # write roster of players to the file
            for player in team['players']:
                file.write("  {}, {}, {}, {}\n".format(
                    player['Name'],
                    player['Soccer Experience'],
                    player['Height (inches)'],
                    player['Guardian Name(s)']
                ))
            file.write("\n")  # Add space between teams

def create_player_letters(teams):
    """Create personalized letters to the guardians of each player"""
    for team in teams:
        for player in team['players']:
            # Create filename from player's name
            filename = "_".join(player['Name'].split()).lower() + ".txt"
            
            with open(filename, 'w') as file:
                file.write(LETTER_TEXT.format(
                    player['Guardian Name(s)'],
                    player['Name'],
                    team['name'],
                    PRACTICE_TIME[team['name']]
                ))

def distribute_players_equally(players_list, teams):
    """Distribute players from a list equally among teams using round-robin"""
    for i, player in enumerate(players_list):
        team_index = i % len(teams)
        teams[team_index]['players'].append(player)

def main():
    """
    Coordinate youth soccer league from player data in CSV File.
    """
    # Get players data from the CSV File
    players = get_players_data_from_csv()
    
    print(f"Total players: {len(players)}")
    
    # Separate players by experience
    experienced_players = []
    non_experienced_players = []
    
    for player in players:
        if player['Soccer Experience'] == 'YES':
            experienced_players.append(player)
        else:
            non_experienced_players.append(player)
    
    print(f"Experienced players: {len(experienced_players)}")
    print(f"Non-experienced players: {len(non_experienced_players)}")
    
    # Create teams
    soccer_league = [create_team(name) for name in TEAM_NAMES]
    
    # Distribute experienced players first (equally)
    distribute_players_equally(experienced_players, soccer_league)
    
    # Then distribute non-experienced players
    distribute_players_equally(non_experienced_players, soccer_league)
    
    # Print distribution for verification
    for team in soccer_league:
        exp_count = sum(1 for p in team['players'] if p['Soccer Experience'] == 'YES')
        print(f"{team['name']}: {len(team['players'])} players ({exp_count} experienced)")
    
    # Output team rosters and player letters
    create_team_roster(soccer_league)
    create_player_letters(soccer_league)
    
    print("\nTeam roster created: teams.txt")
    print("Personalized letters created for all players")

if __name__ == '__main__':
    main()
