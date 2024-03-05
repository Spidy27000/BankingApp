import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from Backend.Database import Database


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
        amount = self.amount_entry.get()
        if amount.isnumeric():
            amount = int(amount)
            self.master.add_money(amount)
            messagebox.showinfo(
                "Money Deposited",
                f"The amount of {amount} was Deposited to your Account ",
            )
            self.master.show_home()
        else:
            if check_is_empty(amount):
                messagebox.showerror(
                    "Invalid input format", "The input field can not be empty"
                )
            else:
                messagebox.showerror(
                    "Invalid input format", "Enter the amount in numbers"
                )
        self.amount_entry.delete(0, "end")


class WithDrawMoneyPage(tk.Frame):
    def __init__(self, master):
        self.master = master
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
        amount = self.amount_entry.get()
        db = Database()
        if amount.isnumeric():
            amount = int(amount)
            self.master.withdraw_money(amount)
            if db.get_balance(self.master.user_id) < int(amount):
                messagebox.showerror("Invalid ammount", "You dont have enough balance")
                return
            messagebox.showinfo(
                "Money withdrawn",
                f"The amount of {amount} was withdrawn from your Account ",
            )
            self.master.show_home()
        else:
            if check_is_empty(amount):
                messagebox.showerror(
                    "Invalid input format", "The input field can not be empty"
                )
            else:
                messagebox.showerror(
                    "Invalid input format", "enter the amount in numbers"
                )
        self.amount_entry.delete(0, "end")


class TransferMoneyPage(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, master, bg="#FFFFFF")
        self.username_label = tk.Label(self, text=" Enter username:", bg="white")
        self.username_entry = tk.Entry(
            self, relief="solid", bg="#FFFFFF", borderwidth=1
        )
        self.ammount_label = tk.Label(self, text="Enter amount:", bg="white")
        self.ammount_entry = tk.Entry(self, relief="solid", bg="#FFFFFF", borderwidth=1)

        self.password_label = tk.Label(self, text="Enter Password:", bg="white")
        self.password_entry = tk.Entry(
            self, relief="solid", bg="#FFFFFF", borderwidth=1, show="*"
        )
        self.db = Database()

        self.submit_button = tk.Button(
            self,
            text="Transfer",
            relief="solid",
            bg="white",
            command=lambda: self.tranfer_money(),
        )

        self.username_label.grid(row=0, column=0, padx=(170, 10), pady=(50, 10))
        self.ammount_label.grid(row=1, column=0, padx=(170, 10), pady=(10, 10))
        self.password_label.grid(row=2, column=0, padx=(170, 10), pady=(10, 10))
        self.username_entry.grid(row=0, column=1, padx=(10, 50), pady=(50, 10))
        self.ammount_entry.grid(row=1, column=1, padx=(10, 50), pady=(10, 10))
        self.password_entry.grid(row=2, column=1, padx=(10, 50), pady=(10, 10))

        self.submit_button.grid(row=3, column=0, padx=(170, 0), columnspan=2, pady=10)

    def tranfer_money(self):
        username = self.username_entry.get()
        amount = self.ammount_entry.get()
        password = self.password_entry.get()
        main_username = self.db.get_name(self.master.user_id)
        other_id = self.db.get_user_id(username)
        print(username, amount, password)
        if (
            check_is_empty(username)
            or check_is_empty(amount)
            or check_is_empty(password)
        ):
            messagebox.showerror("Invalid input", "the input field can not be empty")
            return

        if self.db.is_username_taken(username) and (other_id == self.master.user_id):
            messagebox.showerror("Invalid user", "the username does not exists")
            return
        if not self.db.is_user_valid(main_username, password):
            messagebox.showerror("Invalid password", "u have inputed wrong password")
            return
        if self.db.get_balance(self.master.user_id) <int(amount):
            messagebox.showerror("Invalid ammount", "You dont have enough balance")
            return

        self.db.transfer_money(self.master.user_id, other_id, amount)
        self.master.show_home()


class TranstionsPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#FFFFFF")
        self.master = master
        self.treeveiw_frame = tk.Frame(self, width=600, height=400)
        self.treeveiw_frame.place(
            relx=0.5, rely=0.435, relwidth=1, relheight=350 / 400, anchor="center"
        )
        self.table = ttk.Treeview(
            self.treeveiw_frame,
            columns=("Money_from", "Date", "Withdraw", "Deposit"),
            show="headings",
        )
        self.to_home_button = tk.Button(
            self, text="Return to home", command=lambda: master.show_home()
        )
        self.table.heading("Money_from", text="Trantion_From")
        self.table.heading("Date", text="Date")
        self.table.heading("Withdraw", text="Credit")
        self.table.heading("Deposit", text="Debit")
        self.table.column("Money_from", width=150)
        self.table.column("Date", width=150)
        self.table.column("Withdraw", width=150)
        self.table.column("Deposit", width=150)

        self.table.pack(side=tk.LEFT, fill="y", expand=False)
        self.to_home_button.pack(side="bottom", pady=(0, 10))

    def fill_data(self):
        self.table.delete(*self.table.get_children())
        db = Database()
        data = db.get_transtion_data(self.master.user_id)
        for item in data:
            self.table.insert("", "end", values=item)


def check_is_empty(str):
    return str.isspace() or (str == "")
