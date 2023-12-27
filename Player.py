class Player:
    #should store game-level elements
    #init function creates Player instance that stores individual stats
    def __init__(self, name, jersey, position, path) -> Player:
        self.name = name # example: Jorja Chambers. Should handle nicknames and possible mispells
        self.jersey = jersey # int type, jersey number. May change from one game to another.
        self.position = position # String for abbreviation i.e. OPP, S, MB, etc.
        # dictionary that takes from local folder's txt file that lists stats like Kills, Assists, Digs, etc. 
        # Assumes it's formatted properly (I'm making the txt file). Listed stats outside of code to avoid clutter and portability
        self.stats = {}
        with open(path, mode = "r") as statsConfig:
            columns = list(statsConfig.read())
            for label in columns:
                self.stats.setdefault(label, 0)
        return self
    
    def increment_stat(self, stat) -> int:
        self.stats[stat] += 1
        return self.stats.get(stat)