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


'''
 PRACTICE_TIME:a dict representation
 Dragons - June 19, 2017 @ 2:00PM,
 Sharks - June 20, 2017 @ 3:00PM, 
 Raptors - June 21, 2017 @ 2:00PM
'''
PRACTICE_TIME = {
    'Dragons': "June 19, 2017 @ 2:00PM",
    'Sharks': "June 20, 2017 @ 3:00PM",
    'Raptors': "June 21, 2017 @ 2:00PM",
}

def get_players_data_from_csv(scv_file = CSV_SUPPLIED):
    """Read a CSV datafile, convert player data to dictionary data type
       and return list of player dicts
       """
    with open(scv_file) as  csv_fl:
        players_reader = csv.DictReader(csv_fl)
        players = list(players_reader)
        csv_fl.close()
        return players


def create_team(name):
    """
    Generate dictionary representation of the Team    
    """
    return {'name': name, 'avg_height': 0, 'players': []}


def create_team_roster(teams):
    """Write team names and assigned players to text file 
    team.txt
    """
    filename = "text.txt"
    with open(filename, 'a') as file:
        #write team name
        file.write("{} \n".format(teams['name']))

        # write roster of players to the file
        for player in teams['players']:
            file.write(player['Name'])
            file.write(" {},  {},  {}\n"
                       "".format(player['Soccer Experience'],
                                 player['Height (inches)'],
                                 player['Guardian Name(s)']))
        file.close()


def create_player_letters(team):
    """Extra Credit.
    Creating 18 text Files for each Player of the Team.
    Creating a personalized letter to the guardians of each player 
    on the team. The text should contain the the following Info's
        Team Placement of the Child and Practice time.
    The final output text should be  player’s name as the name of the file,
    in lowercase and with underscores and ending in .txt and its contents are:        
        player's name, team name, guardians name and practice date/time
    """
    for player in team['players']:
        # split on name spices (no other condition given)
        player_name = player['Name'].split()
        # make file names from player's names and rejoin them with underscores
        filename = "_".join(player_name).lower() + ".txt"
        with open(filename, 'w') as file:
            # write the team mate soccer name
            file.write("Youth Soccer League -- Team {} --\n\n".format(team['name']))
            # LETTER TEXT
            file.write(LETTER_TEXT.format(player['Guardian Name(s)'], player['Name'],PRACTICE_TIME[team['name']],PRACTICE_TIME[team['name']]))





def distribute_exper_players_equally(players, league):
    # distribute experienced players into teams
    while players:
        # add player to each team
        for team in league:
            # add the next player (experienced first)
            # Move the experienced players at the first indexes
            team['players'].insert(0, players.pop(0))


def main():
    """
    Coordinate youth soccer league from player data in CSV File.
    Distribute 18 Children equally among three Teams with respect to
    the player's soccer experience. Generate the balanced three 
    teams in --text.txt-- file. 
    Finally send personalized Text Letters to the Guardians of the Children, 
    letting know about each player's team mate, practice time and etc.
    """
    # generate soccer league team list
    soccer_legue = []
    for name in TEAM_NAMES:
        soccer_legue.append(create_team(name))

    # get players data from the CSV File
    players = get_players_data_from_csv()
    # experienced  players
    experienced_players = []
    # non experienced  players
    non_experienced_players = []
    for player in players:
        if player['Soccer Experience'] == 'YES':
            experienced_players.append(player)
        else:
            non_experienced_players.append(player)

    # distribute the  non-experienced players into teams
    distribute_exper_players_equally(non_experienced_players, soccer_legue)
    # distribute experienced players into teams
    distribute_exper_players_equally(experienced_players, soccer_legue)

    #output team rosters and player letters
    for team in soccer_legue:
        create_player_letters(team)
        create_team_roster(team)



if __name__ == '__main__':
    main()
