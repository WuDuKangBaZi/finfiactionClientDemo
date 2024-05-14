import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as ttkbs
from Util.sqlite_util import sqliteUtil
from Model import invoice
from Util.mrpax import Mrapx


class InvoiceReview(tk.Frame):
    """
    发票审核界面
    """
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.select_value_id = None
        self.master = master
        master.title("财务流程自动化 - 发票审核")
        style = ttkbs.Style(theme="minty")
        table_frame = ttk.Frame(self)
        table_frame.pack(fill="both", expand=True, padx=10, pady=5)  # 调整表格的间距

        style.configure("Treeview", background="#f9f9f9", foreground="black", font=('微软雅黑', 10))
        style.configure("Treeview.Heading", font=('微软雅黑', 10, 'bold'))

        # columns = ("序号", "报销单号", "发票代码", "发票号码", "购买方企业名称", "销方名称",
        #            "发票组号码", "价税合计", "金额", "税额", "是否核验成功", "备注")
        columns = ("序号","发票号","工单号","发票日期","金额","税额","价税合计","购买方企业名称","销方名称","发票类型","鉴真结果")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        # 设置列宽度
        for col in columns:
            self.tree.heading(col, text=col, anchor=tk.CENTER)
            self.tree.column(col, anchor=tk.CENTER, minwidth=50, width=100)  # 调整列宽度

        # 添加示例数据
        # data = invoice.list_invoice()
        query_str = "select ROWID,invoice_number,order_id,invoice_date,subtotal,tax,total_amount,buyer_enterprise,seller_enterprise,invoice_type,disting from Invoices"
        sq_util = sqliteUtil()
        data = sq_util.query(query_str)
        for item in data:
            self.tree.insert("", "end", values=item)

        # 编造示例数据并添加到表格中，总共40行

        self.tree.pack(fill="both", expand=True)

        # 创建底部框架
        bottom_frame = ttk.Frame(self, padding=10)
        bottom_frame.pack(fill="x", side="bottom")

        # 添加按钮：取消
        # button_cancel = ttk.Button(bottom_frame, text="取消", style="danger.TButton")
        # button_cancel.pack(side="right", padx=5, pady=5)

        # 添加按钮：保存设置
        button_save_settings = ttk.Button(bottom_frame, text="发票验证", style="primary.TButton",command=lambda :self.review())
        button_save_settings.pack(side="right", padx=5, pady=5)
        self.pack(fill="both", expand=True)


    def review(self):
        select_invoice = self.tree.selection()
        print(select_invoice)
        if select_invoice == ():
            messagebox.showinfo("提示","未选择发票!")
            return
        row_data = []
        self.select_value_id = self.tree.selection()
        for item in select_invoice:
            row_item = self.tree.item(item)['values']
            row_data.append([row_item[1],row_item[3],row_item[6]])
        mrpax = Mrapx()
        robot_status = mrpax.check_status()
        if robot_status == {}:
            messagebox.showerror(
                "警告!", "流程机器人状态不可用!请检查流程机器人状态!", icon="warning")
        else:
            rpa_dict = mrpax.list_mrpax()
            if "发票鉴真" not in rpa_dict.keys():
                messagebox.showerror("警告!", "流程机器人中没有发票鉴真流程!请导入发票识别流程!", icon="warning")
            else:
                messagebox.showinfo("提示!",
                                    "点击确定以启动流程机器人执行发票鉴真流程!\n机器人执行过程中非必要请勿触碰鼠标和键盘!",
                                    icon="info")
                self.work_id = mrpax.execute(rpa_dict['发票鉴真'],{"arr2_发票信息":row_data})
                self.reface_reuslt()

    def reface_reuslt(self):
        try:
            mrpax = Mrapx()
            result = mrpax.check_workflow_result(self.work_id)
            if result:
                result_data = result['arr_发票鉴别结果']
                for i in range(0,len(self.select_value_id)):
                    self.tree.set(self.select_value_id[i],result_data[i])
            else:
                raise Exception("未获取到数据!")
        except Exception as e:
            self.after(1000, self.reface_reuslt)
