from Util.sqlite_util import sqliteUtil


def list_order():
    sql_str = "select * from orders"
    result = sqliteUtil().query(sql_str)
    return result


class Orders():
    def __init__(self):
        self.order_id = None
        self.order_number = None
        self.order_date = None
        self.status = None
        self.total_amount = None

    def update(self):
        sql_str = f"update orders set order_number={self.order_number}, order_date={self.order_date}, status={self.status}, total_amount={self.total_amount} where order_id={self.order_id}"
        sqliteUtil().execute(sql_str)
        return True

    def delete(self):
        sql_str = f"delete from orders where order_id={self.order_id}"
        sqliteUtil().execute(sql_str)
        return True

