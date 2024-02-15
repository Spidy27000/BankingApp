import tkinter as tk


class HomePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.label_username = tk.Label(self, text="Username:")
        self.label_username.pack()
