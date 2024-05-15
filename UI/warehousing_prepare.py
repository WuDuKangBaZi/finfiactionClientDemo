import queue
import threading
import time
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import ttkbootstrap as ttkbs

from Model import invoice, inbounds
from UI.modify_Inbounds import ModifyInbounds
from Util.mrpax import Mrapx
from Util.sqlite_util import sqliteUtil


class WarehousingPrepare(tk.Frame):
    """
    发票预制
    """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.work_id = None
        self.master = master
        self.queue = queue.Queue()
        master.title("财务流程自动化 - 入库单录入")
        style = ttkbs.Style(theme="minty")
        # 左侧功能框架
        left_frame = ttk.Frame(self, style="primary.TFrame", padding=10)
        left_frame.pack(fill="y", side="left")
        # 发票录入按钮
        button_invoice_entry = ttk.Button(left_frame, text="采购入库", style="primary.Outline.TButton",
                                          command=lambda: self.read_inbounds())
        button_invoice_entry.pack(side="top", pady=5)

        # 创建新的框架2
        new_frame2 = ttk.Frame(self, style="Third.TFrame", padding=10)
        new_frame2.pack(fill="both",expand=True)  # 填充X方向并添加垂直间距
        # 创建表格框架
        table_frame = ttk.Frame(new_frame2)
        table_frame.pack(fill="both", expand=True)  # 调整表格的间距

        # 设置表格样式
        style.configure("Treeview", background="#f9f9f9",
                        foreground="black", font=('微软雅黑', 10))
        style.configure("Treeview.Heading", font=('微软雅黑', 10, 'bold'))

        # 定义表头和列宽度
        columns = ("序号","入库单号","订单编号","购方企业名称","入库详情","入库单金额","SAP订单","入库日期")
        column_widths = [50, 150, 150, 200, 400, 100, 100, 100]  # 每列的宽度

        # 创建表格
        self.warehousing_tree = ttk.Treeview(
            table_frame, columns=columns, show="headings")

        # 设置表头和列宽度
        for col, width in zip(columns, column_widths):
            self.warehousing_tree.heading(col, text=col, anchor=tk.CENTER)
            self.warehousing_tree.column(col, anchor=tk.CENTER, minwidth=50, width=width)

        # 表格绑定双击触发

        self.warehousing_tree.bind("<Double-1>", self.modify_inbounds)
        self.warehousing_tree.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)
       # self.test_data()
        self.list_inbounds()

    def test_data(self):
        data = [['1','10032','','山东及时雨汽车科技有限公司','*运输服务*客运服务费','17.90','','2024-3-22'],
                ['2','10042','','郑州兴隆石化有限公司','*汽油*92#汽油','373','','2024-3-8']]
        self.invoke_tree(data)


    def invoke_tree(self, data):
        if data is None:
            data = invoice.list_invoice()
        self.warehousing_tree.delete(*self.warehousing_tree.get_children())
        for item in data:
            self.warehousing_tree.insert("", "end", values=item)
            self.warehousing_tree.update()

    def modify_inbounds(self, event):
        select_value = self.warehousing_tree.item(self.warehousing_tree.selection()[0], 'values')
        # if select_value:
        ModifyInbounds(select_value,self)

    def reface_result(self):
        try:
            if self.work_id:
                mrpax = Mrapx()
                result = mrpax.check_workflow_result(self.work_id)
                if result:
                    result_data = result['obj_入库单信息']
                    if result_data != {}:
                        for i in range(0,len(result_data['str_入库单号'])):
                            inbounds.insert(result_data['str_入库单号'][i], result_data['str_入库日期'][i],
                                            result_data['str_入库详情'][i]
                                            , result_data['str_入库单金额'][i], result_data['购方企业名称'][i], '','')
                            result = invoice.list_invoice()
                            self.invoke_tree(result)

                    else:
                        messagebox.showerror("警告!", "流程机器人执行失败!请检查流程机器人状态!", icon="warning")
                else:
                    self.after(1000, self.reface_result)
        except queue.Empty:
            self.after(1000, self.reface_result)
        except Exception as e:
            print(e)


    def read_inbounds(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("表格文件", "*.xlsx;*.xls;*.cvs;*.et")]
        )
        if file_path == "":
            return
        mrpax = Mrapx()
        robot_status = mrpax.check_status()
        if robot_status == {}:
            messagebox.showerror(
                "警告!", "流程机器人状态不可用!请检查流程机器人状态!", icon="warning")
        else:
            rpa_dict = mrpax.list_mrpax()
            if "入库单入库" not in rpa_dict.keys():
                messagebox.showerror(
                    "警告!", "流程机器人中没有入库单入库流程!请导入入库单识别流程!", icon="warning")
            else:
                messagebox.showinfo("提示!", "点击确定以启动流程机器人执行入库单识别流程!\n机器人执行过程中非必要请勿触碰鼠标和键盘!", icon="info")
                self.work_id = mrpax.execute(
                    rpa_dict["入库单识别"], {"str_excel路径": file_path})
                self.reface_result()


    def list_inbounds(self):
        self.invoke_tree(inbounds.list_inbounds())