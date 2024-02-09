import tkinter as tk
from enum import Enum
from Frontend.LoginPage import LoginPage
from Frontend.SignUpPage import SignUpPage


class PageType(Enum):
    LoginPage = 1
    SignUpPage = 2


class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Login and Sign Up")
        self.login_page = LoginPage(self)
        self.signup_page = SignUpPage(self)

        self.show_login()

    def _pack_forget(self, type: PageType):
        match type:
            case PageType.LoginPage:
                self.login_page.pack_forget()
            case PageType.SignUpPage:
                self.signup_page.pack_forget()
            # NOTE: add all cases

    def show_login(self):
        self.login_page.pack()
        self._pack_forget(PageType.SignUpPage)

    def show_signup(self):
        self.signup_page.pack()
        self._pack_forget(PageType.LoginPage)

    def switch_to_signup(self):
        self.show_signup()

    def switch_to_login(self):
        self.show_login()
