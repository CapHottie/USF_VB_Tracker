# for pyinstaller 
# pyinstaller --noconfirm --onedir --windowed --add-data "<CustomTkinter Location>/customtkinter;customtkinter/"  "<Path to Python Script>"

import customtkinter as ctk

class Karl(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        ctk.set_default_color_theme("green")
        ctk.set_appearance_mode("dark")
        
        
        self.title("Karl - USF VB Tracker")
        self.geometry(f"{300}x{300}")
        self.grid_columnconfigure((0,1), weight = 1)
        # Start up frame, buttons, etc.
        OptionsMainMenu = ctk.CTkLabel(self, text = "What would you like to do?")
        OptionsMainMenu.grid(row = 0, column = 0, padx=20, pady=20, sticky = "new", columnspan = 2)
        
        DBViewButton = ctk.CTkButton(self, text = "View Team Data", command = self.viewDB)
        DBViewButton.grid(row=1, column=0, padx=20, pady=20)
        
        recordMatchButton = ctk.CTkButton(self, text = "Record New Match", command = self.startMatch)
        recordMatchButton.grid(row=1, column=1, padx=20,pady=20)
    
    def viewDB():
        print(0)
    
    def startMatch():
        print(1)


if __name__ == "__main__":
    karl = Karl()
    karl.mainloop()

