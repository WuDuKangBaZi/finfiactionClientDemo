from Util.sqlite_util import sqliteUtil


def insert(invoice_number, order_id, invoice_date, subtotal, tax, total_amount, payment_status, buyer_enterprise,
           seller_enterprise, invoice_type):
    sql_str = f"insert into Invoices values({invoice_number}, {order_id}, {invoice_date}, {subtotal}, {tax}, {total_amount}, {payment_status}, {buyer_enterprise}, {seller_enterprise}, {invoice_type},'')"
    sqliteUtil().execute(sql_str)
    return True


def update(invoice_number, order_id, invoice_date, subtotal, tax, total_amount, payment_status, buyer_enterprise,
           seller_enterprise, invoice_type):
    sql_str = f"update Invoices set order_id={order_id}, invoice_date={invoice_date}, subtotal={subtotal}, tax={tax}, total_amount={total_amount}, payment_status={payment_status}, buyer_enterprise={buyer_enterprise}, seller_enterprise={seller_enterprise}, invoice_type={invoice_type} where invoice_number={invoice_number}"
    sqliteUtil().execute(sql_str)
    return True


def delete(invoice_number):
    sql_str = f"delete from invoice where invoice_number={invoice_number}"
    sqliteUtil().execute(sql_str)
    return True


def list_invoice():
    sql_str = "select  * from Invoices"
    result = sqliteUtil().query(sql_str)
    return result


def query_by(seach_res):
    sql_str = f"""
        select * from Invoices 
        where invoice_number like %{seach_res}%
        or buyer_enterprise like %{seach_res}%
        or seller_enterprise like %{seach_res}%
    """
    result = sqliteUtil().query(sql_str)
    return result
