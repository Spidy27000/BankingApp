import tkinter as tk
from tkinter import messagebox


class AppBar(tk.Frame):
    def __init__(self, master, name, balance):
        self.master = master
        self.name = name
        self.balance = balance

        tk.Frame.__init__(
            self,
            master,
            padx=10,
            pady=5,
            bg="#253585",
            height=50,
            width=600,
            relief="ridge",
        )

        self.name_label = tk.Label(
            self, text=f"Welcome, {self.name}", fg="white", bg="#253585"
        )
        self.name_label.pack(side=tk.LEFT)

        self.balance_label = tk.Label(
            self, text=f"Balance:- ₹{self.balance}", fg="white", bg="#253585"
        )
        self.balance_label.pack(side=tk.LEFT, padx=(20, 0))
        # TODO: add logout and delete account button

    def logout(self):
        # Code for logging out
        messagebox.showinfo("Logout", "You have been logged out.")

    def delete_account(self):
        # Code for deleting account
        messagebox.showinfo("Delete Account", "Your account has been deleted.")


class HomePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="#FFFFFF")
        self.master = master

        self.app_bar_frame = AppBar(self, self.get_name(), self.get_balance())

        self.add_money_button = tk.Button(
            self,
            text="Add Cash",
            command=lambda: master.show_add_money(),
            height=4,
            width=30,
        )
        self.withdraw_money_button = tk.Button(
            self,
            text="Withdraw Cash",
            command=lambda: master.withdraw_money(),
            height=4,
            width=30,
        )
        self.transfer_money_button = tk.Button(
            self,
            text="Tranfer",
            command=lambda: master.transfer_money(),
            height=4,
            width=30,
        )
        self.show_transation_button = tk.Button(
            self,
            text="Show all transtions",
            command=lambda: master.show_transation(),
            height=4,
            width=30,
        )
        self.app_bar_frame.place(
            relx=0.5, rely=0.125, relwidth=1, relheight=50 / 400, anchor="s"
        )
        self.add_money_button.grid(
            column=0, row=1, padx=10, pady=(70, 10), sticky="nsew"
        )
        self.withdraw_money_button.grid(
            column=1, row=1, padx=10, pady=(70, 10), sticky="nsew"
        )
        self.transfer_money_button.grid(
            column=0, row=2, padx=10, pady=(10, 0), sticky="nsew"
        )
        self.show_transation_button.grid(
            column=1, row=2, padx=10, pady=(10, 0), sticky="nsew"
        )

    def get_name(self):
        return "tanish"

    def get_balance(self):
        return 10000
