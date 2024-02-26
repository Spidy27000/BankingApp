import tkinter as tk
from tkinter import messagebox


class AddMoneyPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#FFFFFF")
        self.amount_label = tk.Label(
            self, bg="#FFFFFF", text="Enter the Amount to be deposited:"
        )
        self.amount_entry = tk.Entry(self, relief="solid", bg="#FFFFFF", borderwidth=1)
        self.submit_button = tk.Button(
            self,
            relief="ridge",
            text="Deposit",
            borderwidth=1,
            bg="#FFFFFF",
            command=lambda: self.add(),
        )

        self.amount_label.pack(pady=(100, 10))
        self.amount_entry.pack(pady=(10, 10))
        self.submit_button.pack(pady=(10, 0))

    def add(self):
        ammount = self.amount_entry.get()
        if ammount.isnumeric():
            ammount = int(ammount)
            self.master.add_money(ammount)
            messagebox.showinfo(
                "Money Deposited",
                f"The ammonut of {ammount} was Deposited to your Account ",
            )
            self.master.show_home()
        else:
            if ammount.isspace() or (ammount == ""):
                messagebox.showerror(
                    "Invalid input format", "The input field can not be empty"
                )
            else:
                messagebox.showerror(
                    "Invalid input format", "Enter the ammount in numbers"
                )


class WithDrawMoneyPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#FFFFFF")
        self.amount_label = tk.Label(
            self, bg="#FFFFFF", text="Enter the Amount to be withdrawn:"
        )
        self.amount_entry = tk.Entry(self, relief="solid", bg="#FFFFFF", borderwidth=1)
        self.submit_button = tk.Button(
            self,
            relief="ridge",
            text="Withdraw",
            borderwidth=1,
            bg="#FFFFFF",
            command=lambda: self.withdraw(),
        )

        self.amount_label.pack(pady=(100, 10))
        self.amount_entry.pack(pady=(10, 10))
        self.submit_button.pack(pady=(10, 0))

    def withdraw(self):
        ammount = self.amount_entry.get()
        if ammount.isnumeric():
            ammount = int(ammount)
            self.master.withdraw_money(ammount)
            messagebox.showinfo(
                "Money withdrawn",
                f"The ammonut of {ammount} was withdrawn from your Account ",
            )
            self.master.show_home()
        else:
            if ammount.isspace() or (ammount == ""):
                messagebox.showerror(
                    "Invalid input format", "The input field can not be empty"
                )
            else:
                messagebox.showerror(
                    "Invalid input format", "enter the ammount in numbers"
                )
