import sqlite3
from datetime import datetime

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
            date TEXT NOT NULL,
            withdraw INTEGER DEFAULT 0,
            deposit INTEGER DEFAULT 0,
            user_id INTEGER NOT NULL,
            other_id INTEGER default NULL,
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

    def delete_user(self, id):
        self.conn = sqlite3.connect(DBNAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute("delete from users where id = ?", (id,))
        self.conn.commit()
        self.conn.close()

    def deposit_money(self, id, amount):
        conn = sqlite3.connect(DBNAME)
        curr = conn.cursor()
        curr.execute(
            "insert into transtion(date,deposit,user_id) values (?,?,?)",
            (datetime.today().strftime("%d/%m/%Y"), amount, id),
        )
        curr.execute(
            "update users set balance =balance + ? where id = ?",
            (
                amount,
                id,
            ),
        )
        conn.commit()
        conn.close()

    def withdraw_money(self, id, amount):
        conn = sqlite3.connect(DBNAME)
        curr = conn.cursor()
        curr.execute(
            "insert into transtion(date,withdraw,user_id) values (?,?,?)",
            (datetime.today().strftime("%d/%m/%Y"), amount, id),
        )
        curr.execute(
            "update users set balance =balance - ? where id = ?",
            (
                amount,
                id,
            ),
        )
        conn.commit()
        conn.close()

    def transfer_money(self, id, other_id, amount):
        conn = sqlite3.connect(DBNAME)
        curr = conn.cursor()
        curr.execute(
            "insert into transtion(date,deposit,user_id,other_id) values (?,?,?,?)",
            (datetime.today().strftime("%d/%m/%Y"), amount, id, other_id),
        )
        curr.execute(
            "insert into transtion(date,withdraw,user_id,other_id) values (?,?,?,?)",
            (datetime.today().strftime("%d/%m/%Y"), amount, other_id, id),
        )
        curr.execute(
            "update users set balance =balance - ? where id = ?",
            (
                amount,
                id,
            ),
        )
        curr.execute(
            "update users set balance =balance + ? where id = ?",
            (
                amount,
                other_id,
            ),
        )
        conn.commit()
        conn.close()

    def get_transtion_data(self, id):
        conn = sqlite3.connect(DBNAME)
        curr = conn.cursor()
        # trastion from date withdraw deposit
        curr.execute(
            """SELECT 
                CASE 
                    WHEN t.other_id IS NULL THEN '' 
                    ELSE u.name 
                END AS name,
                t.date AS date,
                t.withdraw AS withdraw,
                t.deposit AS deposit 
            FROM transtion AS t 
            LEFT JOIN users AS u ON t.other_id = u.id 
            WHERE t.user_id = ?;
        """,
            (id,),
        )
        res = curr.fetchall()
        conn.commit()
        conn.close()
        return res
