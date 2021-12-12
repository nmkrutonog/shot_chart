"""
Create Data Main
This file creates a new shot instance according to the user's specifications
on all shot qualities both situational and resultative

Nolan Krutonog
"""
from create_shot_util import *
from player_search import *
from shot_class import *

"""
This helper function converts the shot to a dictionary in order to be properly
stored into shot_list_data
"""
def shotToDict(shot):
    dic = {"name": shot.name, "team": shot.team, "phase": shot.phase, "position": shot.position,
           "style": shot.style, "result": shot.result, "shotLoc": shot.shotLoc, "skip": shot.skip,
           "lob": shot.lob, "backhand": shot.backhand}
    return dic


"""
This function creates a shot instance according to the user's specifications on
all shot qualities both situational and resultative. It then returns a shot
in the form of a dictionary
"""
def createShot(name, team):
    shot = Shot()
    player = []
    if name:
        player.append(name)
        player.append(team)
    else:
        player = playerSearch()

    # situational
    shot.name = player[0]
    shot.team = player[1]
    shot.phase = selectPhase()
    shot.position = selectPosition()

    # resultative
    shot.style = selectStyle()
    shot.result = selectResult()
    shot.shotLoc = selectShotLoc()
    shot.skip = isSkip()
    shot.lob = isLob()
    shot.backhand = isBackhand()

    return shot


"""
This function creates a new list of shots to be appended to the already existing list of shots,
and returns the new list
"""
def createShotList():
    newShotList = []
    shot = createShot(name="", team="")  # shot is dict, not shot class
    shot = shotToDict(shot)
    newShotList.append(shot)
    oneMore = input("Add another shot with " + shot["name"] + "? (y/n): ").upper()
    while oneMore == 'Y':
        shot = createShot(shot["name"], shot["team"])
        newShotList.append(shot)
        oneMore = input("Add another shot with same player? (y/n): ").upper()

    return newShotList
