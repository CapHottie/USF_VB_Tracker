import pandas as pd

# each Database object will correspond to a season
# to compare or join data from previous years, a different method will be reached since
# the purpose of this object is to facilitate access to data from a given season rather than maintaining all-time data
class Database():
    def __init__(self, season) -> None:
        # field declarations
        self.playerLog = pd.read_csv(f"../logs/{season}/roster.csv")
        self.gameLog = pd.read_csv(f"../logs/{season}/matches/games_info.csv")
        self.setsLog = pd.read_csv(f"../logs/{season}/matches/sets_log.csv")
        # event-specific records
        self.eventsLog = pd.read_csv(f"../logs/{season}/events/events_log.csv")
        self.hitsLog = pd.read_csv(f"../logs/{season}/events/hits_log.csv")
        self.serviceLog = pd.read_csv(f"../logs/{season}/events/serves_log.csv")
        self.assistsLog = pd.read_csv(f"../logs/{season}/events/assists_log.csv")
        self.blockingLog = pd.read_csv(f"../logs/{season}/events/blocks_log.csv")
        self.digsLog = pd.read_csv(f"../logs/{season}/events/digs_log.csv")
        self.receivesLog = pd.read_csv(f"../logs/{season}/events/receives_log.csv")
        self.eventCategories = ("hits", "serves", "assists", "blocks", "digs", "receives")
    
    def filter_by_player(self, player):
        pass
    
    def filter_by_match(self):
        pass

    def filter_by_column(self, category):
        pass