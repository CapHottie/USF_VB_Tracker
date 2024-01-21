import customtkinter as ctk
import pandas as pd
from ViewManagement import *

class DataCategoryButton(ctk.CTkButton):
    def __init__(self, master, title):
        super().__init__(master, text=title)
        
class DataView():
    def __init__(self, currentWindow):
        full_res_window(currentWindow)
        currentWindow.title("Karl Database")

        # set up frames
        currentWindow.grid_columnconfigure(0, weight=0)
        currentWindow.grid_columnconfigure(1, weight=1)
        currentWindow.grid_rowconfigure(0, weight=0)
        currentWindow.grid_rowconfigure(1, weight=1)

        # category top bar
        self.topFrame = ctk.CTkFrame(currentWindow)
        TF = self.topFrame
        TF.grid(row=0, column=0, padx=5, pady=5, sticky="new", columnspan=2) 

        # left side bar to toggle on/off player/match views
        self.leftToggleBar = ctk.CTkScrollableFrame(currentWindow)
        LB = self.leftToggleBar
        LB.grid(row=1, column=0, padx=(5, 0), pady=5, sticky="nsw")  

        # where the data is displayed
        self.mainFrame = ctk.CTkFrame(currentWindow)
        MF = self.mainFrame
        MF.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")  

        # populate top frame
        yearFilter = ctk.CTkOptionMenu(TF, values=["2024", "2023"])
        yearFilter.grid(row=0, column=5, padx=(20, 10), pady=10, sticky="nse")

        homeButton = ctk.CTkButton(TF, text="Home")
        homeButton.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")

        categories = ("Team", "Player", "Match")
        for i, category in enumerate(categories):
            categoryButton = DataCategoryButton(TF, category)
            categoryButton.grid(row=0, column=i + 1, padx=20, pady=10, sticky="ns")
        TF.grid_columnconfigure((1, 2, 3), weight=2)
        TF.grid_columnconfigure((0, 4, 5), weight=1)
        
        self.blank_window()
        self.df = Database()

    def view_season_options(self, )
    
    def view_player_options(self):
        LB = self.leftToggleBar
        clear_view(LB)
        
    def view_match_options(self):
        LB = self.leftToggleBar
        clear_view(LB)

    def view_team_options(self):
        LB = self.leftToggleBar
        clear_view(LB)
    
    def blank_window(self):
        clear_view(self.leftToggleBar)
        clear_view(self.mainFrame)
        # populate left sidebar with default text
        noViewSelected = ctk.CTkLabel(self.leftToggleBar, text="Please select a data category")
        noViewSelected.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.leftToggleBar.grid_columnconfigure(0, weight=1)
        self.leftToggleBar.grid_rowconfigure(0, weight=0)
        
        # populate main frame with default text
        emptyView = ctk.CTkLabel(self.mainFrame, text="No data queried")
        emptyView.grid(row=0, column=0, sticky="nsew")
        self.mainFrame.grid_columnconfigure(0, weight=1)
        self.mainFrame.grid_rowconfigure(0, weight=1)

if __name__ == "__main__":
    ctk.set_default_color_theme("green")
    ctk.set_appearance_mode("dark")
    test = ctk.CTk()
    testA = DataView(test)
    test.mainloop()
