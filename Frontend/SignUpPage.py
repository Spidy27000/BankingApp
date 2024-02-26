import tkinter as tk
from tkinter import messagebox


class SignUpPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#FFFFFF")
        self.master = master

        self.label_username = tk.Label(self, text="Username:", bg="#FFFFFF")
        self.label_display_name = tk.Label(self, text="Name:", bg="#FFFFFF")
        self.label_password = tk.Label(self, text="Password:", bg="#FFFFFF")

        self.entry_username = tk.Entry(self)
        self.entry_display_name = tk.Entry(self)
        self.entry_password = tk.Entry(self, show="*")

        self.button_signup = tk.Button(
            self,
            text="Sign up",
            command=lambda: self.signup(),
            bg="#FFFFFF",
            relief="solid",
            borderwidth=1,
        )
        self.button_login = tk.Button(
            self,
            text="Switch to Login",
            command=lambda: master.show_login(),
            relief="solid",
            borderwidth=1,
            bg="#FFFFFF",
        )

        self.label_username.grid(row=0, column=0, padx=(170, 10), pady=(40, 10))
        self.label_display_name.grid(row=1, column=0, padx=(170, 10), pady=(10, 10))
        self.label_password.grid(row=2, column=0, padx=(170, 10), pady=(10, 10))
        self.entry_username.grid(row=0, column=1, padx=(10, 50), pady=(40, 10))
        self.entry_display_name.grid(row=1, column=1, padx=(10, 50), pady=(10, 10))
        self.entry_password.grid(row=2, column=1, padx=(10, 50), pady=(10, 10))

        self.button_signup.grid(row=3, column=0, padx=(170, 0), columnspan=2, pady=10)
        self.button_login.grid(row=4, column=0, padx=(170, 0), columnspan=2)

    def signup(self):
        new_username = self.entry_username.get()
        new_password = self.entry_password.get()
        new_display_name = self.entry_display_name.get()

        # Basic signup logic (you can replace this with your registration logic)
        messagebox.showinfo(
            "Sign Up Successful", "Account created for {}".format(new_username)
        )
        id = 0
        # TODO: add a db function to get if from user id
        self.master.show_home(id)
