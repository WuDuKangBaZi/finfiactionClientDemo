from Util.sqlite_util import sqliteUtil


def list_inbounds():
    sql_str = ("select ROWID,inbound_number,order_id,buyer_enterprise,details,total_amount,sap_order,inbound_date from "
               "inbounds")
    result = sqliteUtil().query(sql_str)
    return result


def insert(inbound_number, inbound_date, details, total_amount, buyer_enterprise, order_id, sap_order):
    sql_str = f"insert into inbounds values('{inbound_number}', '{inbound_date}', '{details}', '{total_amount}','{sap_order}', '{buyer_enterprise}',''{order_id}','{sap_order}'')"
    sqliteUtil().execute(sql_str)
    return True


def update(inbound_id, inbound_number, inbound_date, details, total_amount, buyer_enterprise, order_id, sap_order):
    sql_str = f"update inbounds set inbound_number='{inbound_number}', order_id='{order_id}', inbound_date='{inbound_date}', details='{details}', total_amount='{total_amount}', buyer_enterprise='{buyer_enterprise}',sap_order = '{sap_order}' where inbound_id='{inbound_id}'"
    print(sql_str)
    sqliteUtil().execute(sql_str)
    return True


def delte(inbound_id):
    sql_str = f"delete from inbounds where inbound_id={inbound_id}"
    sqliteUtil().execute(sql_str)
    return True
