import tkinter as tk
from tkinter import messagebox

from Backend.Database import Database


class AppBar(tk.Frame):
    def __init__(self, master):
        self.master = master

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

        self.name_label = tk.Label(self, fg="white", bg="#253585")

        self.balance_label = tk.Label(self, fg="white", bg="#253585")
        self.logout_button = tk.Button(
            self,
            text="Logout",
            bg="#253285",
            fg="white",
            relief="solid",
            borderwidth=0,
            command=lambda: self.logout(),
        )
        self.delete_button = tk.Button(
            self,
            text="Delete Account",
            bg="#253285",
            fg="white",
            relief="solid",
            borderwidth=0,
            command=lambda: self.delete_account(),
        )
        self.name_label.pack(side=tk.LEFT)
        self.balance_label.pack(side=tk.LEFT, padx=(20, 0))
        self.logout_button.pack(side=tk.RIGHT, padx=(10, 10))
        self.delete_button.pack(side=tk.RIGHT)

    def logout(self):
        # Code for logging out
        messagebox.showinfo("Logout", "You have been logged out.")
        self.master.master.show_login()

    def delete_account(self):
        # Code for deleting account
        messagebox.showinfo("Delete Account", "Your account has been deleted.")
        db = Database()
        db.delete_user(self.master.master.user_id)
        self.master.master.show_login()


class HomePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="#FFFFFF")
        self.master = master

        self.app_bar_frame = AppBar(self)
        self.user_id: int

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
            command=lambda: master.show_withdraw_money(),
            height=4,
            width=30,
        )
        self.transfer_money_button = tk.Button(
            self,
            text="Tranfer",
            command=lambda: master.show_transfer_money(),
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
            column=0, row=1, padx=(20,10), pady=(70, 10), sticky="nsew"
        )
        self.withdraw_money_button.grid(
            column=1, row=1, padx=10, pady=(70, 10), sticky="nsew"
        )
        self.transfer_money_button.grid(
            column=0, row=2, padx=(20,10), pady=(10, 0), sticky="nsew"
        )
        self.show_transation_button.grid(
            column=1, row=2, padx=10, pady=(10, 0), sticky="nsew"
        )

    def set_name(self, id):
        db = Database()
        name = db.get_name(id)
        self.app_bar_frame.name_label.configure(text=f"Welcome, {name}")

    def set_balance(self, id):
        db = Database()
        balance = db.get_balance(id)
        self.app_bar_frame.balance_label.configure(text=f"Balance:- {balance}")
