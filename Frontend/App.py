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
        self.db = Database()
        self.db.get_all_data()
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
                self.login_page.entry_username.delete(0, "end")
                self.login_page.entry_password.delete(0, "end")
            case PageType.SignUp:
                self.signup_page.place_forget()
                self.signup_page.entry_username.delete(0, "end")
                self.signup_page.entry_password.delete(0, "end")
                self.signup_page.entry_display_name.delete(0, "end")
            case PageType.Home:
                self.home_page.place_forget()
            case PageType.AddMoney:
                self.add_money_page.place_forget()
            case PageType.WithDrawMoney:
                self.withdraw_money_page.place_forget()
            case PageType.TransferMoney:
                self.transfer_money_page.place_forget()
                self.transfer_money_page.username_entry.delete(0,"end")
                self.transfer_money_page.password_entry.delete(0,"end")
                self.transfer_money_page.ammount_entry.delete(0,"end")

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
        if user_id is not None:
            self.user_id = user_id
            self.home_page.set_name(user_id)
        self.home_page.set_balance(self.user_id)
        self.home_page.place(
            relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center"
        )
        self._place_forget()
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

    def add_money(self, amount):
        self.db.deposit_money(self.user_id, amount)

    def withdraw_money(self, amount):
        self.db.withdraw_money(self.user_id, amount)
