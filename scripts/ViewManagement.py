import customtkinter as ctk

def clear_view(view):
        for element in view.winfo_children():
            element.grid_remove()
def full_res_window(window):
    # screen size
    yRes = window.winfo_screenheight()
    xRes = window.winfo_screenwidth()
    resStr = f'{xRes}x{yRes}'
    window.geometry(resStr)

def balance_grid_weights(higherWeightFrame, lowerWeightFrame):
    pass