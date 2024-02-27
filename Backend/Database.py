from os import times_result
import sqlite3

DBNAME = "mydb.db"


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DBNAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """create table if not exists users(
            id integer primary key autoincrement,
            username text not null ,
            name text not null,
            password text not null
        );"""
        )
        self.conn.commit()
        self.conn.close()

    def add_user(self, username, name, password):
        self.conn = sqlite3.connect(DBNAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "insert into users(username,name,password) values(':username',':name',':password')",
            {"username": username, "name": name, "password": password},
        )
        self.conn.commit()
        self.conn.close()

    def is_username_taken(self, username):
        self.conn = sqlite3.connect(DBNAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            'select 1 from users where username =":username;"',
            {"username": username},
        )
        res = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        if len(res) > 0:
            return False
        else:
            return True

    def is_user_valid(self, username, password):
        self.conn = sqlite3.connect(DBNAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            'select 1 from users where username = ":username" AND password = ":password"',
            {"username": username, "password": password},
        )
        res = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        if len(res) > 0:
            return True
        else:
            return False

    def get_user_id(self, username):
        self.conn = sqlite3.connect(DBNAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            'select id from users where username = ":username"', {"username": username}
        )
        res = self.cursor.fetchone()
        self.conn.commit()
        self.conn.close()
        return res

    def get_name(self, user_id):
        self.conn = sqlite3.connect(DBNAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            'select name from users where id = ":user_id"', {"user_id": user_id}
        )
        res = self.cursor.fetchone()
        self.conn.commit()
        self.conn.close()
        return res
