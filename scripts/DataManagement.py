import pandas as pd

# each Database object will correspond to a season
# to compare or join data from previous years, a different method will be reached since
# the purpose of this object is to facilitate access to data from a given season rather than maintaining all-time data
class Database():
    def __init__(self, season) -> None:
        # Define file paths and corresponding attribute names
        datasets = {
            'playerLog': 'roster.csv',
            'gameLog': 'matches/games_info.csv',
            'setsLog': 'matches/sets_log.csv',
            'hitsLog': 'events/hits_log.csv',
            'serviceLog': 'events/serves_log.csv',
            'assistsLog': 'events/assists_log.csv',
            'blockingLog': 'events/blocks_log.csv',
            'digsLog': 'events/digs_log.csv',
            'receivesLog': 'events/receives_log.csv',
        }

        # Initialize fields using a loop
        for attribute_name, file_path in datasets.items():
            setattr(self, attribute_name, pd.read_csv(f"../logs/{season}/{file_path}"))

        # Initialize eventCategories
        self.eventCategories = ("hits", "serves", "assists", "blocks", "digs", "receives")
    
    def list_players(self):
        self.playerLog
        pass
    
    def filter_by_player(self, player):
        pass
    
    def filter_by_match(self):
        pass

    def filter_by_column(self, category):
        pass
class Player:
    def __init__(self) -> None:
        pass

class Game:
    def __init__(self) -> None:
        pass