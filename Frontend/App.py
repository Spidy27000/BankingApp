import tkinter as tk
from enum import Enum, auto
from Backend.Database import Database
from Frontend.LoginPage import LoginPage
from Frontend.SignUpPage import SignUpPage
from Frontend.HomePage import HomePage
from Frontend.Utils import (
    AddMoneyPage,
    TransferMoneyPage,
    TranstionsPage,
    WithDrawMoneyPage,
)


class PageType(Enum):
    Login = auto()
    SignUp = auto()
    Home = auto()
    AddMoney = auto()
    WithDrawMoney = auto()
    TransferMoney = auto()
    Transtions = auto()
    NoneType = auto()


class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Banking App")
        self.user_id = 0
        self.home_page = HomePage(self)
        self.login_page = LoginPage(self)
        self.signup_page = SignUpPage(self)
        self.add_money_page = AddMoneyPage(self)
        self.withdraw_money_page = WithDrawMoneyPage(self)
        self.transfer_money_page = TransferMoneyPage(self)
        self.transtions_page = TranstionsPage(self)
        self.current_page = PageType.NoneType

        self.show_login()

    def _place_forget(self):
        match self.current_page:
            case PageType.Login:
                self.login_page.place_forget()
            case PageType.SignUp:
                self.signup_page.place_forget()
            case PageType.Home:
                self.home_page.place_forget()
            case PageType.AddMoney:
                self.add_money_page.place_forget()
            case PageType.WithDrawMoney:
                self.withdraw_money_page.place_forget()
            case PageType.TransferMoney:
                self.transfer_money_page.place_forget()
            case PageType.Transtions:
                self.transtions_page.place_forget()
            case _:
                return

    def show_login(self):
        self.login_page.place(
            relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center"
        )
        self._place_forget()
        self.current_page = PageType.Login

    def show_signup(self):
        self.signup_page.place(
            relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center"
        )
        self._place_forget()
        self.current_page = PageType.SignUp

    def show_home(self, user_id=None):
        self.home_page.place(
            relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center"
        )
        self._place_forget()
        if user_id is not None:
            self.user_id = user_id
            self.home_page.user_id = user_id
        self.current_page = PageType.Home

    def show_transfer_money(self):
        self.transfer_money_page.place(
            relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center"
        )
        self._place_forget()
        self.current_page = PageType.TransferMoney

    def show_add_money(self):
        self.add_money_page.place(
            relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center"
        )
        self._place_forget()
        self.current_page = PageType.AddMoney

    def show_withdraw_money(self):
        self.withdraw_money_page.place(
            relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center"
        )
        self._place_forget()
        self.current_page = PageType.WithDrawMoney

    def show_transation(self):
        self.transtions_page.fill_data()
        self.transtions_page.place(
            relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center"
        )
        self._place_forget()
        self.current_page = PageType.Transtions

    def add_money(self, ammount):
        print(f"{ammount} add to account")

    def withdraw_money(self, ammount):
        print(f"{ammount} is withdrawn")

    def get_name(self):
        db = Database()
        res = db.get_name(self.user_id)
        return res

    def get_balance(self):
        return 10000
