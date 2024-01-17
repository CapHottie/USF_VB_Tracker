# for pyinstaller 
# pyinstaller --noconfirm --onedir --windowed --add-data "<CustomTkinter Location>/customtkinter;customtkinter/"  "<Path to Python Script>"

import tkinter as tk 
import customtkinter as ctk 

ctk.set_default_color_theme("green")
ctk.set_appearance_mode("dark")

# Open main window
Karl = ctk.CTk()
Karl.title("Karl - USF VB Tracker")
yRes = Karl.winfo_screenheight()
xRes = Karl.winfo_screenwidth()
resStr = str(xRes) + 'x' + str(yRes)
print(resStr)
Karl.geometry(resStr)
Karl.configure()

def openDb():
    print("el chavo")

# Start up frame, buttons, etc.
dbButton = ctk.CTkButton(Karl, text = "View Team Data", command = openDb)
dbButton.grid(row=0, column=0, padx=20, pady=20)
mainFrame = ctk.CTkFrame(master = Karl, width = 200, height = 200)


Karl.mainloop()



