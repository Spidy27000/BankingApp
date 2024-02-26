import tkinter as tk
from tkinter import messagebox


class AddMoneyPage(tk.Frame):
    def __init__(self, master, user_id):
        tk.Frame.__init__(self, master, bg="#FFFFFF")
        self.user_id = user_id
        self.amount_label = tk.Label(
            self, bg="#FFFFFF", text="Enter the Amount to be added:"
        )
        self.amount_entry = tk.Entry(self, relief="solid", bg="#FFFFFF", borderwidth=1)
        self.submit_button = tk.Button(
            self,
            relief="ridge",
            text="Submit",
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
                "Money Added", f"The ammonut of {ammount} was aaded to your Account "
            )
            self.master.show_home()
        else:
            if ammount.isspace() or (ammount == ""):
                messagebox.showerror(
                    "Invalid input format", "The input field can not be empty"
                )
            else:
                messagebox.showerror(
                    "Invalid input format", "Add the ammount in numbers"
                )
