import queue
import threading
import time
import tkinter as tk
import traceback
from tkinter import ttk, filedialog, messagebox
import ttkbootstrap as ttkbs

from Model import invoice
from Util.mrpax import Mrapx
from Util.sqlite_util import sqliteUtil


class InvoicePrepare(tk.Frame):
    """
    发票预制
    """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.work_id = None
        self.master = master
        self.queue = queue.Queue()
        master.title("财务流程自动化 - 发票预制")
        style = ttkbs.Style(theme="minty")
        # 左侧功能框架
        left_frame = ttk.Frame(self, style="primary.TFrame", padding=10)
        left_frame.pack(fill="y", side="left")
        # 发票录入按钮
        button_invoice_entry = ttk.Button(left_frame, text="发票录入", style="primary.Outline.TButton",
                                          command=lambda: self.ocr_invoice())
        button_invoice_entry.pack(side="top", pady=5)
        # 预制设置
        button_prep_settings = ttk.Button(
            left_frame, text="预制设置", style="primary.Outline.TButton")
        button_prep_settings.pack(side="top", padx=5, pady=5)
        # 添加“自动填充”按钮
        button_auto_fill = ttk.Button(
            left_frame, text="自动填充", style="primary.Outline.TButton")
        button_auto_fill.pack(side="top", padx=5, pady=5)

        # 添加“人工编辑”按钮
        button_manual_edit = ttk.Button(
            left_frame, text="人工编辑", style="primary.Outline.TButton")
        button_manual_edit.pack(side="top", padx=5, pady=5)

        # 创建新的框架1
        new_frame1 = ttk.Frame(self, style="New.TFrame", padding=5)
        new_frame1.pack(fill="both", pady=5)  # 填充X方向并添加垂直间距

        # 设置新框架1的背景色
        style.configure("New.TFrame", background="#4287f5")
        # 创建新的框架3
        style.configure("Third.TFrame", background="#FFB6C1")
        new_frame3 = ttk.Frame(self, style="Third.TFrame", padding=10)
        new_frame3.pack(fill="both", expand=True)  # 填充X方向并添加垂直间距
        # 在新框架3中添加表格
        table_frame = ttk.Frame(new_frame3)
        table_frame.pack(fill="both", expand=True, padx=10, pady=5)  # 调整表格的间距

        style.configure("Treeview", background="#f9f9f9",
                        foreground="black", font=('微软雅黑', 10))
        style.configure("Treeview.Heading", font=('微软雅黑', 10, 'bold'))

        # 定义表头和列宽度
        columns = ('序号','购方企业名称','销方企业名称','关联订单','不含税金额','税额','含税金额','支付状态','发票类型','发票编号','开票日期')
        column_widths = [30, 250, 250, 150, 100, 100, 100,100,100,200,150]  # 每列的宽度

        # 创建表格
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        # 设置表头和列宽度
        for col, width in zip(columns, column_widths):
            self.tree.heading(col, text=col, anchor=tk.CENTER)
            self.tree.column(col, anchor=tk.CENTER, minwidth=50, width=width)
        self.pack(fill="both", expand=True)
        # 编造虚构的表格数据

        # 插入数据到表格中
        self.invoke_tree(None)

        self.tree.pack(fill="both", expand=True)


    def invoke_tree(self, data):
        if data is None:
            sql_util = sqliteUtil()
            query_str = "select ROWID,buyer_enterprise,seller_enterprise,order_id,subtotal,tax,total_amount,payment_status,invoice_type,invoice_number,invoice_date from Invoices"
            data = sql_util.query(query_str)
        self.tree.delete(*self.tree.get_children())
        for item in data:

            self.tree.insert("", "end", values=item)
            self.tree.update()

    def get_work_result(self):
        print(f"--- run as --- get_work_result {self.work_id}")
        if self.work_id:
            mrpax = Mrapx()
            for i in range(0, 100):
                result = mrpax.check_workflow_result(self.work_id)
                if result:
                    self.queue.put(result)
                    break
                else:
                    time.sleep(2)
                    continue

    def reface_result(self):
        try:
            if self.work_id:
                mrpax = Mrapx()
                result = mrpax.check_workflow_result(self.work_id)
                if result:
                    print(result)
                    result_data = result['obj_发票识别结果']
                    invoice.insert(result_data['发票组号码'],'',result_data['开票日期'],result_data['金额'],
                                   result_data['税额'],result_data['价税合计'],'',
                                   result_data['购买方企业名称'],result_data['销方名称'],result_data['发票类别'])
                    result = invoice.list_invoice()
                    self.invoke_tree(result)
                else:
                    self.after(1000, self.reface_result)
        except Exception as e:
            traceback.print_exc()
            print("Error:", e)

    def ocr_invoice(self):
        # 点击后弹出文件选择窗口
        file_path = filedialog.askopenfilename(
            filetypes=[("图片文件", "*.jpg;*.png")])
        if file_path == "":
            return
        # 使用接口调用流程
        mrpax = Mrapx()
        robot_status = mrpax.check_status()
        if robot_status == {}:
            messagebox.showerror(
                "警告!", "流程机器人状态不可用!请检查流程机器人状态!", icon="warning")
        else:
            rpa_dict = mrpax.list_mrpax()
            if "发票识别" not in rpa_dict.keys():
                messagebox.showerror(
                    "警告!", "流程机器人中没有发票识别流程!请导入发票识别流程!", icon="warning")
            else:
                messagebox.showinfo("提示!", "点击确定以启动流程机器人执行发票识别流程!\n机器人执行过程中非必要请勿触碰鼠标和键盘!", icon="info")
                self.work_id = mrpax.execute(
                    rpa_dict["发票识别"], {"str_发票图片路径": file_path})
                self.reface_result()
