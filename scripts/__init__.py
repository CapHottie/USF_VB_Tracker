import tkinter as tk
from tkinter import ttk
import pandas as pd

class ExcelTableApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Dynamic Excel Table")

        # Load data from Excel file
        self.load_data()

        # Create Treeview for displaying data
        self.tree = ttk.Treeview(self.master, columns=self.df.columns, show="headings")
        for col in self.df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.CENTER, width=100)

        self.tree.pack(pady=10)

        # Create Combobox for selecting events
        self.events_combobox = ttk.Combobox(self.master, values=self.df['Event'].unique(), state="readonly")
        self.events_combobox.set("All Events")
        self.events_combobox.bind("<<ComboboxSelected>>", self.filter_data)
        self.events_combobox.pack(pady=5)

        # Create Button for sorting by column
        sort_button = tk.Button(self.master, text="Sort by Column", command=self.sort_data)
        sort_button.pack(pady=5)

    def load_data(self):
        # Load data from Excel file (replace 'your_excel_file.xlsx' with your file)
        self.df = pd.read_excel('sample_db.xlsx')

    def filter_data(self, event):
        selected_event = self.events_combobox.get()
        if selected_event == "All Events":
            self.tree.delete(*self.tree.get_children())
            self.load_data()
            self.populate_tree()
        else:
            filtered_df = self.df[self.df['Event'] == selected_event]
            self.tree.delete(*self.tree.get_children())
            self.populate_tree(filtered_df)

    def sort_data(self):
        # Implement sorting logic (replace 'your_column' with the column to sort)
        column_to_sort = 'your_column'
        self.df.sort_values(by=column_to_sort, inplace=True)
        self.tree.delete(*self.tree.get_children())
        self.populate_tree()

    def populate_tree(self, dataframe=None):
        if dataframe is None:
            dataframe = self.df
        for i, row in dataframe.iterrows():
            self.tree.insert("", i, values=list(row))

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelTableApp(root)
    root.mainloop()
