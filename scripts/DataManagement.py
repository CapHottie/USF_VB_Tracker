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

        # Initialize datasets fields 
        for attribute, file_path in datasets.items():
            setattr(self, attribute, pd.read_csv(f"../logs/{season}/{file_path}"))
        
        self.PlayerList = {} # dictionary containing Player obj instances 
        playerColumns = list(self.playerLog.columns)
        for i in range(self.playerLog.shape[0]):
            playerRow = self.playerLog.iloc[i].values
            player = Player(playerColumns, playerRow)
            self.PlayerList.setdefault(player.player_id, player)
    
    
class Player:
    # attributes is the list of column headings in the roster dataset
    # values is what is contained in that given player's file 
    def __init__(self, attributes, values) -> None:
        for i in enumerate(attributes):
            setattr(self, attributes[i], values[i])
    
    def generate_name(self):
        self.fullName = f"{self.first} {self.last}"
        self.fName = f"{self.first[0]}. {self.last}"

class Game:
    def __init__(self) -> None:
        pass