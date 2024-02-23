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
        self.title("Banking App")
        self.home_page = HomePage(self)
        self.login_page = LoginPage(self)
        self.signup_page = SignUpPage(self)
        self.current_page = PageType.NoneType

        self.show_home()

    def _place_forget(self):
        match self.current_page:
            case PageType.Login:
                self.login_page.place_forget()
            case PageType.SignUp:
                self.signup_page.place_forget()
            case PageType.Home:
                self.home_page.place_forget()
            # NOTE: add all cases

    def show_login(self):
        self.login_page.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")
        self._place_forget()
        self.current_page = PageType.Login

    def show_signup(self):
        self.signup_page.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")
        self._place_forget()
        self.current_page = PageType.SignUp

    def show_home(self):
        self.home_page.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")
        self._place_forget()
        self.current_page = PageType.Home
    
    def add_money(self):
        print("deposit")

    def withdraw_money(self):
        print("Withdraw")

    def transfer_money(self):
        print("tranfer")

    def show_transation(self):
        print("show transation")
    
    def get_name(self):
        return "Hello"
