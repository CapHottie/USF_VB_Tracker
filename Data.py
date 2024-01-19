import customtkinter as ctk

class dataCategoryButton(ctk.CTkButton):
    def __init__(self, master, title):
        super().__init__(master, text=title)
        
class DBView():
    def __init__(self, currentWindow):
        self = currentWindow
        # screen size
        yRes = self.winfo_screenheight()
        xRes = self.winfo_screenwidth()
        resStr = str(xRes) + 'x' + str(yRes)
        self.geometry(resStr)
        self.title("Karl Database")

        # set up frames
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        # category top bar
        self.topFrame = ctk.CTkFrame(self)
        TF = self.topFrame
        TF.grid(row=0, column=0, padx=5, pady=5, sticky="new", columnspan=2)  # Removed top padding

        # left side bar to toggle on/off player/match views
        self.leftToggleBar = ctk.CTkScrollableFrame(self)
        LB = self.leftToggleBar
        LB.grid(row=1, column=0, padx=(5, 0), pady=5, sticky="nsw")  # Removed top padding

        # where the data is displayed
        self.mainFrame = ctk.CTkFrame(self)
        MF = self.mainFrame
        MF.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")  # Removed top and bottom padding

        # populate top frame
        yearFilter = ctk.CTkOptionMenu(TF, values=["2024", "2023"])
        yearFilter.grid(row=0, column=5, padx=(20, 10), pady=10, sticky="nse")

        homeButton = ctk.CTkButton(TF, text="Home")
        homeButton.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")

        categories = ("Team", "Player", "Match")
        for i, category in enumerate(categories):
            categoryButton = dataCategoryButton(TF, category)
            categoryButton.grid(row=0, column=i + 1, padx=20, pady=10, sticky="ns")
        TF.grid_columnconfigure((1, 2, 3), weight=2)
        TF.grid_columnconfigure((0, 4, 5), weight=1)

        # populate left sidebar
        noViewSelected = ctk.CTkLabel(LB, text="Please select a data category")
        noViewSelected.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        LB.grid_columnconfigure(0, weight=1)
        LB.grid_rowconfigure(0, weight=1)


if __name__ == "__main__":
    ctk.set_default_color_theme("green")
    ctk.set_appearance_mode("dark")
    test = ctk.CTk()
    testA = DBView(test)
    test.mainloop()
