import tkinter as tk
from tkinter import messagebox


class LoginPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,bg="#505050", height=400,width=400)
        self.master = master

        self.label_username = tk.Label(self, text="Username:")
        self.label_password = tk.Label(self, text="Password:")

        self.entry_username = tk.Entry(self)
        self.entry_password = tk.Entry(self, show="*")

        self.label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        self.label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.button_login = tk.Button(self, text="Login", command=self.login)
        self.button_signup = tk.Button(
            self, text="Switch to Sign Up", command=lambda: master.show_signup()
        )

        self.button_login.grid(row=2, column=1, pady=10)
        self.button_signup.grid(row=3, column=1)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Basic login validation (you can replace this with your authentication logic)
        if username == "user" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
            self.master.show_home()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
