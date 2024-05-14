from Util.sqlite_util import sqliteUtil


class ReimburseUtil():
    def __init__(self):
        pass

    def query(self, invoiceGroupNumber):
       # query_sql = "select * from invoice where invoiceGroupNumber = '%s'" % invoiceGroupNumber
        query_sql =f"""
        select row_number() over (order by ol.order_number), ol.order_number,'',w.sap_order,'','','',I.buyer_enterprise,'','',I.total_amount,I.subtotal,I.tax,'',''
        from Invoices i
        left join Orders ol on i.order_id == ol.order_id
        left join Inbounds w on w.order_id = w.order_id
where cast(i.invoice_number as text) like '%{invoiceGroupNumber}%'
        """
        print(query_sql)
        sqlutil = sqliteUtil()
        result = sqlutil.query(query_sql)
        return result
    def query_by_type(self,type_list:list):
        query_sql = """ select row_number() over (order by ol.order_number), ol.order_number,'',w.sap_order,'','','',I.buyer_enterprise,'','',I.total_amount,I.subtotal,I.tax,'',''
        from Invoices i
        left join Orders ol on i.order_id == ol.order_id
        left join Inbounds w on w.order_id = w.order_id
        where i.invoice_type in ('%s')""" % '\',\''.join(type_list)
        print(query_sql)
        sqlutil = sqliteUtil()
        result = sqlutil.query(query_sql)
        return result

    def get_invoice_type(self):
        sql_util = sqliteUtil()
        sql_str = "select invoice_type from Invoices group by invoice_type"
        result = sql_util.query(sql_str)
        return result
    def get_list(self):
        sql_util = sqliteUtil()
        sql_str = """
        select o.order_number,'',I2.sap_order,'','','',I.buyer_enterprise,'','',I.total_amount,I.subtotal,I.tax,'','' from Orders o
        left join main.Invoices I on o.order_id = I.order_id
        left join main.Inbounds I2 on I.order_id = I2.order_id
        """
        result = sql_util.query(sql_str)
        return result