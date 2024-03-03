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
            password text not null,
            balance integer default 0
        );"""
        )
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS transtion(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            withdraw INTEGER DEFAULT 0,
            deposit INTEGER DEFAULT 0,
            user_id INTEGER NOT NULL,
            other_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (other_id) REFERENCES users(id)
            )"""
        )
        self.conn.commit()
        self.conn.close()

    def add_user(self, username, name, password):
        self.conn = sqlite3.connect(DBNAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "insert into users(username,name,password) values(?,?,?)",
            (
                username,
                name,
                password,
            ),
        )
        self.conn.commit()
        self.conn.close()

    def is_username_taken(self, username):
        self.conn = sqlite3.connect(DBNAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute("select 1 from users where username =?", (username,))
        res = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        if len(res) > 0:
            return True
        else:
            return False

    def is_user_valid(self, username, password):
        self.conn = sqlite3.connect(DBNAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "select 1 from users where username =? AND password = ?;",
            (
                username,
                password,
            ),
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
        self.cursor.execute("select id from users where username =?", (username,))
        res = self.cursor.fetchone()
        self.conn.commit()
        self.conn.close()
        return res[0]

    def get_name(self, user_id):
        self.conn = sqlite3.connect(DBNAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT name FROM users WHERE id=?", (user_id,))
        res = self.cursor.fetchone()
        self.conn.commit()
        self.conn.close()
        if res:
            return res[0]
        else:
            return None

    def get_balance(self, user_id):
        self.conn = sqlite3.connect(DBNAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT balance FROM users WHERE id=?", (user_id,))
        res = self.cursor.fetchone()
        self.conn.commit()
        self.conn.close()
        if res:
            return res[0]
        else:
            return None

    def update_balance(self, id, amount):
        self.conn = sqlite3.connect(DBNAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "update users set balance =balance + ? where id = ?",
            (
                amount,
                id,
            ),
        )
        self.conn.commit()
        self.conn.close()

    def delete_user(self, id):
        self.conn = sqlite3.connect(DBNAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute("delete from users where id = ?", (id,))
        self.conn.commit()
        self.conn.close()

    def deposit_money(self, id, amount):
        print("money added")

    def withdraw_money(self, id, amount):
        print("money withdrawn")

    def transfer_money(self, id, other_id, amount):
        print("money transfer_money")

    def get_all_data(self):
        self.conn = sqlite3.connect(DBNAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute("select * from users")
        res = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        for row in res:
            for info in row:
                print(info, end=",")
            print()
