import tkinter as tk


class HomePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,background="#202020")
        self.master = master

        self.top_bar_frame = tk.Frame(self, bg="#151E3D", height=50, width=400)
        self.name_label = tk.Label(self.top_bar_frame, text=master.get_name())
        # self.name_label.pack()

        self.add_money_button = tk.Button(
            self, text="Add Cash", command=lambda: master.add_money(),
            height=2,width=15
        )
        self.withdraw_money_button = tk.Button(
            self, text="Withdraw Cash", command=lambda: master.withdraw_money(),
            height=2,width=15
        )
        self.transfer_money_button = tk.Button(
            self, text="Tranfer", command=lambda: master.transfer_money(),
            height=2,width=15
        )
        self.show_transation_button = tk.Button(
            self, text="Show all transtions", command=lambda: master.show_transation(),
            height=2,width=15
        )
        self.top_bar_frame.grid_configure(columnspan=2)
        self.top_bar_frame.grid(column=0, row=0)
        self.add_money_button.grid(column=0, row=1, padx=10, pady=30)
        self.withdraw_money_button.grid(column=1, row=1, padx=10, pady=30)
        self.transfer_money_button.grid(column=0, row=2, padx=10, pady=30)
        self.show_transation_button.grid(column=1, row=2, padx=10, pady=30)

    
