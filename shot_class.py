"""
Shot Class
Nolan Krutonog

"""

class Shot:

    def __init__(self):
        # situational
        self.name = ""
        self.team = ""
        self.phase = ""
        self.position = 0

        # resultative
        self.style = ""
        self.result = ""
        self.shotLoc = 0
        self.skip = False
        self.lob = False
        self.backhand = False


"""
When creating or reading shot data, these lists below are the standard
references to create the dictionary
"""
phases = ["6V5", "FC", "COUNTER"]
styles = ["CS", "PU", "FAKE", "FOUL"]
positions = [1, 2, 3, 4, 5, 6]
shotLocs = [1, 2, 3, 4, 5]
results = ['G', 'B', 'M']
bools = ['Y', 'N']
createOrReads = ['C', 'R']
nameOrTeams = ['N', 'T']



