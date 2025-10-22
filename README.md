#  python
#  Build a soccer league


# Read the CSV file and store the data. We'll use the csv module to read the data and convert it into a list of dictionaries.

# Separate the players into two groups: experienced (YES) and non-experienced (NO).

 We have three teams. We want to distribute the experienced players equally among the three teams and then the non-experienced players to fill the rest.
Since there are 18 players, each team will have 6 players. There are 9 experienced players and 9 non-experienced players. So each team gets 3 experienced and 3 non-experienced. 

We can do this by:

Shuffling the experienced and non-experienced lists to avoid any bias (but the problem doesn't require shuffling, so we can just use the order in the CSV).

However, the problem says: "experienced players should be equally distributed among teams, putting those with experience as first in teams."

We can simply take the first 3 experienced for the first team, next 3 for the second, and so on. Similarly for non-experienced.

Then, we assign the players to the teams. We'll create a data structure for the teams.

Write the teams to a file named teams.txt with the format:
Team Name
Player Name, Soccer Experience, Height, Guardian Name(s)
... (all players in the team)

For the extra credit, we create 18 text files, one for each player, named with the player's name in lowercase with underscores (e.g., joe_smith.txt).
The content of the file should be the letter that includes:
- Player's name
- Team name
- Guardian names
- Practice date/time (from the PRACTICE_TIME dictionary)





