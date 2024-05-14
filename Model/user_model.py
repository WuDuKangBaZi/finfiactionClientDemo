from Util.sqlite_util import sqliteUtil


def create_table():
    sqlutil = sqliteUtil()
    sqlutil.execute("""
        create table if not exists user(
        user_id integer primary key autoincrement,
        user_name text,
        account text,
        user_password text
        )
    """)


def login_util(account, password):
    sqlutil = sqliteUtil()
    result = sqlutil.query(f"select user_name from user where account = '{account}' and user_password = '{password}'")
    return result

def insert_user(user_name, account, user_password):
    sqlutil = sqliteUtil()
    sqlutil.execute(f"insert into user(user_name,account,user_password) values('{user_name}','{account}','{user_password}')")