"""
Player Search

Nolan Krutonog
"""

"""
This function is a helper function for playerSearch() which populates the list
called potentialMatches. All player names in potentialMatches are in lowercase
"""

def popPotMatches(players, searchTerm):
    potentialMatches = []
    for i in range(len(players)):
        player = players[i]  # player is the list [name, team], player[0] is name of player
        if searchTerm in player[0].upper():
            potentialMatches.append(player)

    return potentialMatches

"""
This function gets the user input to search player_list.csv for a player, which
consists of a name and a team, then returns a list of the player and the team
they are on
"""

def playerSearch():
    # create list of players, a 'player' is a [name, team]
    playersFile = open("player_list.csv", "r")
    players = []
    for line in playersFile:
        line = line.split(',')
        players.append(line)
    playersFile.close()

    # find the correct player
    searchTerm = input("Search for Player: ").upper()
    while len(searchTerm) < 3:
        searchTerm = input("Search for Player (3chars+): ").upper()

    potentialMatches = popPotMatches(players, searchTerm)  # all players in lowercase
    while len(potentialMatches) == 0:  # if no players found
        print("There were no matches from your entry. ")
        searchTerm = input("Search for Player: ").upper()
        while len(searchTerm) < 3:
            searchTerm = input("Search for Player (3chars+): ").upper()
        potentialMatches = popPotMatches(players, searchTerm)

    if len(potentialMatches) > 1:  # if there are 2 or more players in who match
        for i in range(1, len(potentialMatches) + 1):
            print(str(i) + "->" + potentialMatches[i - 1][0])
        userSel = input("Select a number above to pick a player: ")

        while int(userSel) > len(potentialMatches) or int(userSel) < 1:
            userSel = input("Select a number above to pick a player: ")

        name = potentialMatches[int(userSel) - 1][0]
        team = potentialMatches[int(userSel) - 1][1]
        print(name)

    else:
        name = potentialMatches[0][0]  # if there is exactly one player in the list
        print(name)
        team = potentialMatches[0][1]

    return [name, team]



