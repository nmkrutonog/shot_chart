"""
Read Data Utility Functions
All of these functions return a list of shots from a given shot list filtering
specific situational characteristics about the shots, and the characteristics
chosen. The situational characteristics are player, team, phase, and position

Nolan Krutonog
"""
from shot_class import *
from player_search import *

"""
This function receives a shooter name from the user input and returns a list
of all shots by that shooter and the player list [name, team]
"""
def getShotsByName(shotList):
    player = playerSearch()  # get the first element 'name' of player
    name = player[0]
    team = player[1]

    # create a list of shots of just that player
    nameShots = []
    for shot in shotList:
        if shot["name"] == name:
            nameShots.append(shot)

    return nameShots, player


"""
This function returns a list of shots filtered by a particular team, and the name
of the team
"""
def getShotsByTeam(shotList):
    # populate empty list of teams
    playersList = open("player_list.csv", "r")
    teams = []
    for player in playersList:
        player = player.strip()
        player = player.split(',')
        if player[1] not in teams:
            teams.append(player[1])
    playersList.close()

    # get user input
    for i in range(len(teams)):
        print(str(i + 1) + "->" + teams[i])

    searchTerm = input("Select a number above to pick the team: ")
    while int(searchTerm) > len(teams):
        searchTerm = input("Select a number above to pick the team: ")

    team = teams[int(searchTerm) - 1]

    # populate list of team shots
    teamShots = []
    for shot in shotList:
        if shot["team"] == team:
            teamShots.append(shot)

    return teamShots, team


"""
This function returns a list of shots in a particular phase of the game (6v5, FC, Counter)
and the name of that phase. if none is specified, '' is returned as the phase
"""
def getShotsByPhase(shotList):
    # get user input
    phase = input("PHASE? (6v5, FC, COUNTER): ").upper()
    while phase not in phases and phase != '':
        phase = input("PHASE? (6v5, FC, COUNTER): ").upper()  # populate list

    phaseShots = []

    if phase == '':
        return shotList, phase

    if phase == "6V5":
        for shot in shotList:
            if shot["phase"] == "6V5":
                phaseShots.append(shot)

    if phase == "FC":
        for shot in shotList:
            if shot["phase"] == "FC":
                phaseShots.append(shot)

    if phase == "COUNTER":
        for shot in shotList:
            if shot["phase"] == "COUNTER":
                phaseShots.append(shot)

    return phaseShots, phase


"""
This function returns a list of shots filtered by shot's position and the position
filtered for. If no position is selected, '' is returned for position
"""
def getShotsByPosition(shotList):
    # get user input
    position = input("POSITION (1, 2, 3, 4, 5, 6 (center)): ")
    while position != '' and int(position) not in positions:
        position = input("POSITION (1, 2, 3, 4, 5, 6 (center)): ")

    if position == '':
        return shotList, position

    # populate list
    posShots = []
    for shot in shotList:
        if shot["position"] == int(position):
            posShots.append(shot)

    return posShots, position