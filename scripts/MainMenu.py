# for pyinstaller 
# pyinstaller --noconfirm --onedir --windowed --add-data "<CustomTkinter Location>/customtkinter;customtkinter/"  "<Path to Python Script>"

import customtkinter as ctk

from DataWindow import DBView, DataCategoryButton
from ViewManagement import clear_view

class Karl(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_default_color_theme("green")
        ctk.set_appearance_mode("dark")
        
        self.title("Karl - USF VB Tracker")
        self.geometry(f"{300}x{300}")
        self.grid_columnconfigure((0,1), weight=1)
        # Start up frame, buttons, etc.
        OptionsMainMenu = ctk.CTkLabel(self, text="What would you like to do?")
        OptionsMainMenu.grid(row=0, column=0, padx=20, pady=20, sticky="new", columnspan=2)
        
        DBViewButton = ctk.CTkButton(self, text="View Team Data", command=self.view_DB)
        DBViewButton.grid(row=1, column=0, padx=20, pady=20)
        
        recordMatchButton = ctk.CTkButton(self, text="Record New Match", command=self.start_match)
        recordMatchButton.grid(row=1, column=1, padx=20,pady=20)
    
    def view_DB(self):
        clear_view(self)
        self = DBView(self)
    
    def start_match(self):
        clear_view(self)
        print(1)
        
if __name__ == "__main__":
    karl = Karl()
    karl.mainloop()

