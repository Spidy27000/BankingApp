import tkinter as tk
from enum import Enum, auto
from Frontend.LoginPage import LoginPage
from Frontend.SignUpPage import SignUpPage
from Frontend.HomePage import HomePage


class PageType(Enum):
    Login = auto()
    SignUp = auto()
    Home = auto()
    NoneType = auto()


class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Login and Sign Up")
        self.home_page = HomePage(self)
        self.login_page = LoginPage(self)
        self.signup_page = SignUpPage(self)
        self.current_page = PageType.NoneType

        self.show_home()

    def _pack_forget(self):
        match self.current_page:
            case PageType.Login:
                self.login_page.pack_forget()
            case PageType.SignUp:
                self.signup_page.pack_forget()
            case PageType.Home:
                self.home_page.pack_forget()
            # NOTE: add all cases

    def show_login(self):
        self.login_page.pack()
        self._pack_forget()
        self.current_page = PageType.Login

    def show_signup(self):
        self.signup_page.pack()
        self._pack_forget()
        self.current_page = PageType.SignUp

    def show_home(self):
        self.home_page.pack()
        self._pack_forget()
        self.current_page = PageType.Home
