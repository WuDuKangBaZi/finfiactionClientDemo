import sqlite3 as sql


class sqliteUtil():
    def __init__(self):
        self.connect = sql.connect("save.db")
        self.cursor = self.connect.cursor()

    def query(self, sql_str):
        self.cursor.execute(sql_str)
        data = self.cursor.fetchall()
        self.close()
        return data

    def close(self):
        self.cursor.close()
        self.connect.close()

    def execute(self, sql_str):
        self.cursor.execute(sql_str)
        self.connect.commit()
        self.close()
