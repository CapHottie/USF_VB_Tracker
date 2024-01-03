#game level, not global


#rosters will be provided by csv file. that's for another script. assuming it's 5 columns and 15 rows of values
rosters = {}
rosterA = rosters.setdefault('A', open(pathA, "r")) #path is string for file location
rosterB = rosters.setdefault('B', open(pathB, "r"))

def generate_teams(rosters):
    teamA = [] #good guys
    teamA = rosters.get('A')[]
    teamB = [] #opponents aka. bad guys
