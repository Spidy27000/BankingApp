import tkinter as tk


class HomePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        self.top_bar_frame = tk.Frame(self, bg="black", height=20)
        self.name_label = tk.Label(self.top_bar_frame, text="name")
        self.name_label.pack()

        self.add_money_button = tk.Button(
            self, text="Add Cash", command=lambda: self.add_money()
        )
        self.withdraw_money_button = tk.Button(
            self, text="Withdraw Cash", command=lambda: self.withdraw_money()
        )
        self.transfer_money_button = tk.Button(
            self, text="Tranfer", command=lambda: self.transfer_money()
        )
        self.show_transation_button = tk.Button(
            self, text="Show all transtions", command=lambda: self.show_transation()
        )
        self.top_bar_frame.grid_configure(columnspan=2)
        self.top_bar_frame.grid(column=0, row=0)
        self.add_money_button.grid(column=0, row=1, padx=10, pady=10)
        self.withdraw_money_button.grid(column=1, row=1, padx=10, pady=10)
        self.transfer_money_button.grid(column=0, row=2, padx=10, pady=10)
        self.show_transation_button.grid(column=1, row=2, padx=10, pady=10)

    # TODO: add db
    def add_money(self):
        print("deposit")

    def withdraw_money(self):
        print("Withdraw")

    def transfer_money(self):
        print("tranfer")

    def show_transation(self):
        print("show transation")
