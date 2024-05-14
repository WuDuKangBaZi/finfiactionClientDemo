import queue
import threading
import time
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import ttkbootstrap as ttkbs

from Model import invoice
from Util.mrpax import Mrapx
from Util.sqlite_util import sqliteUtil


class OrderPrepare(tk.Frame):
    """
    发票预制
    """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.work_id = None
        self.master = master
        self.queue = queue.Queue()
        master.title("财务流程自动化 - 订单录入")
        style = ttkbs.Style(theme="minty")
        # 左侧功能框架
        left_frame = ttk.Frame(self, style="primary.TFrame", padding=10)
        left_frame.pack(fill="y", side="left")
        # 发票录入按钮
        button_invoice_entry = ttk.Button(left_frame, text="订单", style="primary.Outline.TButton",
                                          command=lambda: self.ocr_invoice())
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
        columns = ("项目", "金额", "数量", "订单号", "采购订单", "项目", "采购单文本", "税务代码")
        column_widths = [100, 100, 100, 100, 100, 100, 100, 100]  # 每列的宽度

        # 创建表格
        self.warehousing_tree = ttk.Treeview(
            table_frame, columns=columns, show="headings")

        # 设置表头和列宽度
        for col, width in zip(columns, column_widths):
            self.warehousing_tree.heading(col, text=col, anchor=tk.CENTER)
            self.warehousing_tree.column(col, anchor=tk.CENTER, minwidth=50, width=width)

        # 编造虚构的表格数据
        data = [
            ["金龙鱼纯玉米油4L", 628.8, 12, "01524116", "D23234", "米其林沈阳轮胎有限公司", "食品采购费用",
             "91110000710929148A"],
            ["*移动通信设备*适用小对讲机保护套1S硅胶保护壳米家户外对讲机3代Lite件", 1262, 50, "01524117", "D48390",
             "上海米其林轮胎有限公司", "产品采购费用", "913302006842554254"],
            ["*糖果类食品*列罗唯美斯双拼巧克力礼盒年货龙年情人节礼物新年跨年送女友女朋友", 37892.96, 368, "33316056",
             "D23712",
             "上海米其林轮胎有限公司", "食品采购费用", "91350100611332776W"],
            ["*金属制品*手用螺丝攻M16*2", 10.57, 1, "33316061", "D37482", "上海米其林轮胎有限公司", "新材料采购费用",
             "91350100611332776W"],
            ["*鉴证咨询服务*咨询服务费", 55837.6, 1, "33316064", "D12678", "上海米其林轮胎有限公司", "服务费用",
             "91440106691514632L"],
            ["电线电缆*网线", 110.74, 1, "33316069", "D78621", "驰加（上海）汽车用品贸易有限公司", "货运代理服务的费用",
             "91440106691514632L"],
            ["工业自动控制仪表系统安全光幕", 5498.35, 1, "59137347", "D23657", "上海米其林轮胎有限公司", "材料采购费用",
             "91440106691514632L"],
            ["工业自动控制仪表系统塑料座", 257.64, 100, "10972455", "D23798", "米其林（中国）投资有限公司",
             "材料采购费用",
             "91440106691514632L"],
            ["*工业自动控制仪表系统跨接剂", 169.5, 120, "10853488", "D22899", "米其林（中国）投资有限公司",
             "材料采购费用",
             "91330100063983876A"],
            ["工业自动控制仪表系统接触器", 604.96, 1, "00343057", "D16839", "米其林（中国）投资有限公司", "材料采购费用",
             "913100006073820251"]
        ]

        # 插入数据到表格中
        for item in data:
            self.warehousing_tree.insert("", "end", values=item)

        self.warehousing_tree.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)

    def invoke_tree(self, data):
        if data is None:
            data = invoice.list_invoice()
        self.warehousing_tree.delete(*self.warehousing_tree.get_children())
        for item in data:
            self.warehousing_tree.insert("", "end", values=item)
            self.warehousing_tree.update()

    def get_work_result(self):
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
                    result_data = result['obj_订单识别结果']
                    invoice.insert_invoice(result_data['购买方企业名称'], result_data['销方名称'],
                                           result_data['发票组号码'], result_data['价税合计'], result_data['金额'], result_data['税额'])
                    result = invoice.list_invoice()
                    self.invoke_tree(result)
                else:
                    raise Exception("未获取到结果")
        except Exception as e:
            self.after(1000, self.reface_result)

    def ocr_invoice(self):
        # 点击后弹出文件选择窗口
        file_path = filedialog.askopenfilename(
            filetypes=[("表格文件", "*.xlsx;*.xls;*.cvs;*.et")])
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
            if "订单录入" not in rpa_dict.keys():
                messagebox.showerror(
                    "警告!", "流程机器人中没有入库单入库流程!请导入订单录入流程!", icon="warning")
            else:
                messagebox.showinfo("提示!", "点击确定以启动流程机器人执行订单录入流程!\n机器人执行过程中非必要请勿触碰鼠标和键盘!", icon="info")
                self.work_id = mrpax.execute(
                    rpa_dict["订单入库"], {"str_发票图片路径": file_path})
                self.reface_result()
