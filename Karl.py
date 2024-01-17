import tkinter as tk 

if __name__ == "__main__":
    stats_categories = []
    with open("./stats.txt", "r") as statsConfig:
        stats_categories = statsConfig.read().split()

class Match:
    def create_team(roster):
        # takes in String array, each element is one part of the player description
        return

@dataclass(frozen = True)
class Player:
    #should store game-level elements
    #init function creates Player instance that stores individual stats
    def __init__(self, name, jersey, position, stats):
        self.name = name # example: Jorja Chambers. Should handle nicknames and possible mispells
        self.jersey = jersey # int type, jersey number. May change from one game to another.
        self.position = {"Primary": position} # String for abbreviation i.e. OPP, S, MB, etc.
        # dictionary that takes from local folder's txt file that lists stats like Kills, Assists, Digs, etc. 
        # Assumes it's formatted properly (I'm making the txt file). Listed stats outside of code to avoid clutter and portability
        self.stats = {}
        for label in stats:
            self.stats.setdefault(label, 0)
        
        return self
    
    def increment_stat(self, stat) -> int:
        self.stats[stat] += 1
        return self.stats.get(stat)

    def add_position(self, position): # limit of three positions
        if self.position.get("Secondary") is None: # only one position has been recorded 
            return self.position.setdefault("Secondary", position)
        return self.position.setdefault("Tertiary", position)