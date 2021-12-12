"""
Read Data Main
This file contains functions which create a shot list of all shots with situational qualities
chosen by the user. It then displays the qualities

Nolan Krutonog
"""

from read_data_util import *

"""
This function creates a list of shots filtered by name or team, then by phase or position, and
returns the shot list, name, team, phase, and position requested
"""
def getFinalShotList(shotList):
    finalShotList = []

    # filter by name or by team
    nameOrTeam = input("Filter by NAME or TEAM? (n/t): ").upper()
    while nameOrTeam not in nameOrTeams:
        nameOrTeam = input("Filter by NAME or TEAM? (n/t): ").upper()

    name = ''
    team = ''
    if nameOrTeam == 'N':
        nameShots, player = getShotsByName(shotList)
        name = player[0]
        team = player[1]
        for shot in nameShots:
            finalShotList.append(shot)

    if nameOrTeam == 'T':
        teamShots, team = getShotsByTeam(shotList)
        for shot in teamShots:
            finalShotList.append(shot)

    # filter by phase
    finalShotList, phase = getShotsByPhase(finalShotList)

    # filter by position
    finalShotList, position = getShotsByPosition(finalShotList)

    return finalShotList, name, team, phase, position

"""
This function displays the shot list on the terminal to the user
"""
def displayData(finalShotList, name, team, phase, position):
    if name == '':
        name = "N/A"
    if phase == '':
        phase = "N/A"
    if position == '':
        position = "N/A"

    totalShots = len(finalShotList)
    goals = CS = CSG = PU = PUG = FAKE = FAKEG = FOUL = FOULG = 0
    loc1 = loc1G = loc2 = loc2G = loc3 = loc3G = loc4 = loc4G = loc5 = loc5G = 0
    skips = skipsG = lobs = lobsG = backhands = backhandsG = 0

    for shot in finalShotList:
        isGoal = False
        if shot["result"] == 'G':
            goals += 1
            isGoal = True
        if shot["style"] == "CS":
            CS += 1
            if isGoal:
                CSG += 1
        if shot["style"] == "PU":
            PU += 1
            if isGoal:
                PUG += 1
        if shot["style"] == "FAKE":
            FAKE += 1
            if isGoal:
                FAKEG += 1
        if shot["style"] == "FOUL":
            FOUL += 1
            if isGoal:
                FOULG += 1
        if shot["shotLoc"] == 1:
            loc1 += 1
            if isGoal:
                loc1G += 1
        if shot["shotLoc"] == 2:
            loc2 += 1
            if isGoal:
                loc2G += 1
        if shot["shotLoc"] == 3:
            loc3 += 1
            if isGoal:
                loc3G += 1
        if shot["shotLoc"] == 4:
            loc4 += 1
            if isGoal:
                loc4G += 1
        if shot["shotLoc"] == 5:
            loc5 += 1
            if isGoal:
                loc5G += 1
        if shot["skip"] == True:
            skips += 1
            if isGoal:
                skipsG += 1
        if shot["lob"] == True:
            lobs += 1
            if isGoal:
                lobsG += 1
        if shot["backhand"] == True:
            backhands += 1
            if isGoal:
                backhandsG += 1

    if totalShots == 0:
        print("There is no data for your specifications")
        return

    goalP = (goals / totalShots) * 100

    CSP = (CS / totalShots) * 100
    if CS > 0:
        CSGP = (CSG / CS) * 100
    else:
        CSGP = 0

    PUP = (PU / totalShots) * 100
    if PU > 0:
        PUGP = (PUG / PU) * 100
    else:
        PUGP = 0

    FAKEP = (FAKE / totalShots) * 100
    if FAKE > 0:
        FAKEGP = (FAKEG / FAKE) * 100
    else:
        FAKEGP = 0

    FOULP = (FOUL / totalShots) * 100
    if FOUL > 0:
        FOULGP = (FOULG / FOUL) * 100
    else:
        FOULGP = 0

    loc1P = (loc1 / totalShots) * 100
    if loc1 > 0:
        loc1GP = (loc1G / loc1) * 100
    else:
        loc1GP = 0

    loc2P = (loc2 / totalShots) * 100
    if loc2 > 0:
        loc2GP = (loc2G / loc2) * 100
    else:
        loc2GP = 0

    loc3P = int(loc3 / totalShots)
    if loc3 > 0:
        loc3GP = int(loc3G / loc3)
    else:
        loc3GP = 0

    loc4P = (loc4 / totalShots) * 100
    if loc4 > 0:
        loc4GP = (loc4G / loc4) * 100
    else:
        loc4GP = 0

    loc5P = (loc5 / totalShots) * 100
    if loc5 > 0:
        loc5GP = (loc5G / loc5) * 100
    else:
        loc5GP = 0

    skipP = (skips / totalShots) * 100
    if skips > 0:
        skipsGP = (skipsG / skips) * 100
    else:
        skipsGP = 0

    lobP = (lobs / totalShots) * 100
    if lobs > 0:
        lobGP = (lobsG / lobs) * 100
    else:
        lobGP = 0

    backhandP = (backhands / totalShots) * 100
    if backhands > 0:
        backhandsGP = (backhandsG / backhands) * 100
    else:
        backhandsGP = 0

    print("")
    print("Shot List Analysis")
    print("Shooter: " + name)
    print("Team: " + team)
    print("Phase: " + phase)
    print("Position: " + position)
    print("Total Shots: " + str(totalShots))
    print("Goals :" + str(goals) + " -- Goal Percentage: " + str(goalP))
    print("Catch and Shoot Shots :" + str(CS) + " -- percentage: " + str(CSP) + " --- CS goal percentage: " + str(CSGP))
    print("Pickup and Shoot :" + str(PU) + " --- percentage: " + str(PUP) + " --- PUS goal percentage: " + str(PUGP))
    print("Fakes: " + str(FAKE) + " --- percentage: " + str(FAKEP) + " --- Fake goal percentage: " + str(FAKEGP))
    print("Fouls: " + str(FOUL) + " --- percentage: " + str(FOULP) + " --- Foul goal percentage: " + str(FOULGP))
    print("Gk right low: " + str(loc1) + " --- percentage: " + str(loc1P) + " --- Location 1 goal percentage: " + str(
        loc1GP))
    print("Gk right high: " + str(loc2) + " --- percentage: " + str(loc2P) + " --- Location 2 goal percentage: " + str(
        loc2GP))
    print("Nut: " + str(loc3) + " --- percentage: " + str(loc3P) + " --- Location 3 goal percentage: " + str(loc3GP))
    print("Gk left high: " + str(loc4) + " --- percentage: " + str(loc4P) + " --- Location 4 goal percentage: " + str(
        loc4GP))
    print("Gk left low: " + str(loc5) + " --- percentage: " + str(loc5P) + " --- Location 5 goal percentage: " + str(
        loc5GP))
    print("Skips: " + str(skips) + " --- percentage: " + str(skipP) + " --- Skip goal percentage: " + str(skipsGP))
    print("Lobs: " + str(lobs) + " --- percentage: " + str(lobP) + " --- Lobs goal percentage: " + str(lobGP))
    print(
        "Backhands: " + str(backhands) + " --- percentage: " + str(backhandP) + " --- Backhand goal percentage: " + str(
            backhandsGP))

