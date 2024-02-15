import tkinter as tk
from tkinter import messagebox


class SignUpPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        self.label_username = tk.Label(self, text="Username:")
        self.label_display_name = tk.Label(self, text="Name:")
        self.label_password = tk.Label(self, text="Password:")

        self.entry_username = tk.Entry(self)
        self.entry_display_name = tk.Entry(self)
        self.entry_password = tk.Entry(self, show="*")

        self.label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        self.label_display_name.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.label_password.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)
        self.entry_display_name.grid(row=1, column=1, padx=10, pady=10)
        self.entry_password.grid(row=2, column=1, padx=10, pady=10)

        self.button_signup = tk.Button(self, text="Sign Up", command=self.signup)
        self.button_login = tk.Button(
            self, text="Switch to Login", command=lambda: master.show_login()
        )

        self.button_signup.grid(row=3, column=1, pady=10)
        self.button_login.grid(row=4, column=1)

    def signup(self):
        new_username = self.entry_username.get()
        new_password = self.entry_password.get()

        # Basic signup logic (you can replace this with your registration logic)
        messagebox.showinfo(
            "Sign Up Successful", "Account created for {}".format(new_username)
        )
