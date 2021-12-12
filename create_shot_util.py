"""
Create Data Utility
This file contains utility functions to assist in creating shot instances.
Each function returns a value of each shot instance

Nolan Krutonog
"""

from shot_class import *
from player_search import *

"""
This function returns a list where the first elem is the shot's player in lower
case and the second elem is the team they are on
"""
def selectPlayer():
    return playerSearch()

"""
This function returns the shot's phase of the game as a char/string
"""
def selectPhase():
    phase = input("PHASE ('6v5', 'FC', 'Counter'): ").upper()
    while phase not in phases:
        phase = input("PHASE ('6v5', 'FC', 'Counter'): ").upper()

    return phase

"""
This function returns the shooters position as an int
"""
def selectPosition():
    position = input("POSITION (if at center, type '6'): ")
    while int(position) not in positions:
        position = input("POSITION (if at center, type '6'): ")

    return int(position)

"""
This function returns the shot's style as a string
"""
def selectStyle():
    print("'CS' for catch and shoot, 'PU' for pickup and shoot, 'FAKE', or 'FOUL'")
    style = input("STYLE: ").upper()
    while style not in styles:
        style = input("STYLE: ")

    return style

"""
This function returns the shot's result as a char/string
"""
def selectResult():
    result = input("RESULT ('G' for goal, 'B' for block, 'M' for miss): ")
    while result.upper() not in results:
        result = input("RESULT ('G' for goal, 'B' for block, 'M' for miss): ")

    return result.upper()

"""
This function displays the possible codeable shot locations
"""
def displayShotLocs():
    print('1' + " -> " + "gk right low")
    print('2' + " -> " + "gk right high")
    print('3' + " -> " + "nut")
    print('4' + " -> " + "gk left high")
    print('5' + " -> " + "gk left low")

"""
This function returns the shot's location as a int
"""
def selectShotLoc():
    shotLoc = input("SHOT LOCATION (enter 'd' to display the different shot locations): ")
    if shotLoc == 'd':
        displayShotLocs()
        shotLoc = input("SHOT LOCATION: ")
    while not shotLoc.isdecimal() or int(shotLoc) not in shotLocs:
        shotLoc = input("SHOT LOCATION: ")

    return int(shotLoc)

"""
This function asks the user if the shot was a skip or not
"""
def isSkip():
    skip = input("SKIP? (y/n): ").upper()
    while skip not in bools:
        skip = input("SKIP? (y/n): ").upper()

    if skip == 'Y':
        return True
    else:
        return False


"""
This function asks the user if the shot was a lob or not
"""
def isLob():
    lob = input("LOB? (y/n): ").upper()
    while lob not in bools:
        lob = input("LOB? (y/n): ").upper()

    if lob == 'Y':
        return True
    else:
        return False

"""
This function asks the user if the shot was a backhand or not
"""
def isBackhand():
    backhand = input("BACKHAND? (y/n): ").upper()
    while backhand not in bools:
        backhand = input("BACKHAND? (y/n): ").upper()

    if backhand == 'Y':
        return True
    else:
        return False
