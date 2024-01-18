import customtkinter as ctk

class DBView():
    def __init__(self):
        # screen size
        yRes = self.winfo_screenheight()
        xRes = self.winfo_screenwidth()
        resStr = str(xRes) + 'x' + str(yRes)
        self.geometry(resStr)
        
        self.title("Karl Database")