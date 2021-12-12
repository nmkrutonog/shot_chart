"""
Shot Chart Main
This file combines the functions of create_shot_main.py and read_shot_main.py
in order to give the user an easy way to either add shots to the shot chart or
read the data in a useful way

Nolan Krutonog
"""

from read_data_main import *
from create_shot_main import *

def main():
    print("Shot Chart")
    # download shot list and turn text into list
    shotList_initial = open("shot_list_data.txt", "r+")
    shotList = shotList_initial.read()
    shotList_initial.close()

    if shotList != '':
        shotList = eval(shotList)
    else:
        shotList = []

    # user select option
    createOrRead = input("Create shots or read shotlist? (c/r): ").upper()
    while createOrRead not in createOrReads:
        createOrRead = input("Create shots or read shotlist? (c/r): ").upper()

    # to create more data
    if createOrRead == 'C':
        newShotList = createShotList()
        updateShots = input("Update newShotList to shot_list.txt? (y/n): ").upper()
        if updateShots == 'Y':
            for shot in newShotList:
                shotList.append(shot)
        shotList_initial = open("shot_list_data.txt", "w")
        shotList_initial.write(str(shotList))
        shotList_initial.close()

    if createOrRead == 'R':
        if shotList != '':
            finalShotList, name, team, phase, position = getFinalShotList(shotList)
            displayData(finalShotList, name, team, phase, position)


main()