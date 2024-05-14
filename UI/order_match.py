import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkbs
from PIL import Image, ImageTk


class OrderMatch(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.master = master
        master.title("财务流程自动化 - 三单匹配")
        style = ttkbs.Style(theme="minty")
        # 创建左侧功能框架
        left_frame = ttk.Frame(self, style="primary.TFrame", padding=10)
        left_frame.pack(fill="y", side="left")

        style.configure("Right.TFrame", background="#F0F0F0")
        # 创建右侧功能框架
        right_frame = ttk.Frame(self, style="Right.TFrame", padding=10)
        right_frame.pack(fill="y", side="right")
        right_label = ttk.Label(right_frame, text="匹配结果", style="primary.TLabel")
        right_label.pack()
        # 创建输出框
        output_text = tk.Text(right_frame, wrap="word", width=40, height=20)
        output_text.pack(fill="both", expand=True, padx=10, pady=10)

        # 将输出框置于可滚动区域
        scrollbar = ttk.Scrollbar(right_frame, command=output_text.yview)
        scrollbar.pack(side="right", fill="y")
        output_text.config(yscrollcommand=scrollbar.set)

        # 示例文本
        example_text = "匹配结果为：大PO单行，PO与发票单价、数量均不一致，部分匹配"
        output_text.insert("end", example_text)

        # 禁止用户编辑输出框内容
        output_text.config(state="disabled")
        # 在左侧框架添加按钮
        button_order_import = ttk.Button(left_frame, text="订单管理", 
                                         style="primary.Outline.TButton")
        button_order_import.pack(fill="x", padx=5, pady=5)

        button_delivery_import = ttk.Button(left_frame, text="收货单管理", 
                                            style="primary.Outline.TButton")
        button_delivery_import.pack(fill="x", padx=5, pady=5)

        button_auto_match = ttk.Button(left_frame, text="自动匹配", 
                                       style="primary.Outline.TButton")
        button_auto_match.pack(fill="x", padx=5, pady=5)

        button_auto_history = ttk.Button(left_frame, text="匹配记录", 
                                         style="primary.Outline.TButton")
        button_auto_history.pack(fill="x", padx=5, pady=5)

        button_exception_handling = ttk.Button(left_frame, text="异常处理", 
                                               style="primary.Outline.TButton")
        button_exception_handling.pack(fill="x", padx=5, pady=5)

        # 创建新的框架1
        # new_frame1 = ttk.Frame(self, style="New.TFrame", padding=5)
        # new_frame1.pack(fill="x", pady=5)  # 填充X方向并添加垂直间距
        #
        # # 设置新框架1的背景色
        # style.configure("New.TFrame", background="#4287f5")
        #
        # # 在新框架1中添加功能按钮1
        # button_new1 = ttk.Button(new_frame1, text="选择匹配流程",
        #                          style="primary.Outline.TButton")
        # button_new1.pack(side="left", padx=5)
        #
        # button_new1 = ttk.Button(new_frame1, text="单据转换原则",
        #                          style="primary.Outline.TButton")
        # button_new1.pack(side="left", padx=5)
        # 创建新的框架3
        style.configure("Third.TFrame", background="#FFB6C1")
        new_frame3 = ttk.Frame(self, style="Third.TFrame", padding=10)
        new_frame3.pack(fill="x", pady=10)  # 填充X方向并添加垂直间距
        # 在新框架3中添加一个标签作为表格名称
        table_name_label = ttk.Label(new_frame3, text="增值税发票", font=('微软雅黑', 14, 'bold'), background="#FFB6C1")
        table_name_label.pack(pady=(0, 5))  # 设置标签的上方间距为 0，下方间距为 5

        # 在新框架3中添加功能按钮3
        # button_new3 = ttk.Button(new_frame3, text="新功能按钮3",  style="primary.Outline.TButton")
        # button_new3.pack(side="left", padx=5)
        # 创建表格
        table = ttk.Treeview(new_frame3, columns=(
        "Product Name", "Quantity", "Unit Price (incl. tax)", "Amount", "Tax", "Total Amount", "Matching Quantity",
        "Matching Amount"), show="headings")
        table.pack(fill="both", expand=True)

        # 设置表头
        table.heading("Product Name", text="商品名称")
        table.heading("Quantity", text="数量")
        table.heading("Unit Price (incl. tax)", text="含税单价")
        table.heading("Amount", text="金额")
        table.heading("Tax", text="税额")
        table.heading("Total Amount", text="价税合计")
        table.heading("Matching Quantity", text="匹配数量")
        table.heading("Matching Amount", text="匹配金额")

        # 编造虚构的表格数据
        data = [
            ["金龙鱼纯玉米油4L", 12, 48.0733333, 576.88, 51.92, 628.8, 12, 48.07],
            ["*移动通信设备*适用小对讲机保护套1S硅胶保护壳米家户外对讲机3代Lite件", 50, 22.3362, 1116.81, 145.19, 1262,
             50,
             22.33],
            ["*糖果类食品*列罗唯美斯双拼巧克力礼盒年货龙年情人节礼物新年跨年送女友女朋友", 368, 91.12388587, 33533.59,
             4359.37,
             37892.96, 368, 91.12],
            ["*金属制品*手用螺丝攻M16*2", 1, 9.35, 9.35, 1.22, 10.57, 1, 9.35],
            ["*鉴证咨询服务*咨询服务费", 1, 55837.60377, 55837.60, 3350.26, 55837.6, 25, 3190.72],
            ["电线电缆*网线", 1, 98, 98.00, 12.74, 110.74, 1, 98.00],
            ["工业自动控制仪表系统安全光幕", 1, 4865.8, 4865.80, 632.55, 5498.35, 1, 4865.80],
            ["工业自动控制仪表系统塑料座", 100, 2.28, 228, 29.64, 257.64, 100, 2.28],
            ["*工业自动控制仪表系统跨接剂", 120, 1.25, 150, 19.50, 169.5, 120, 1.25],
            ["工业自动控制仪表系统接触器", 1, 533.06, 533.06, 71.90, 604.96, 1, 533.06]
        ]

        # 插入数据到表格中
        for row in data:
            table.insert("", "end", values=row)

        # 缩短表格列宽度
        for col in (
        "Product Name", "Quantity", "Unit Price (incl. tax)", "Amount", "Tax", "Total Amount", "Matching Quantity",
        "Matching Amount"):
            table.column(col, width=100)  # 设置每一列的宽度为 100 像素

        # 创建新的框架2
        new_frame2 = ttk.Frame(self, style="Third.TFrame", padding=10)
        new_frame2.pack(fill="x", pady=10)  # 填充X方向并添加垂直间距

        # 设置新框架2的背景色
        # style.configure("New.TFrame", background="#ff7f0e")

        # 在新框架2中添加功能按钮2
        # button_new2 = ttk.Button(new_frame2, text="新功能按钮2",  style="primary.Outline.TButton")
        # button_new2.pack(side="left", padx=5)
        table_name_label = ttk.Label(new_frame2, text="采购入库单", font=('微软雅黑', 14, 'bold'), background="#FFB6C1")
        table_name_label.pack(pady=(0, 5))  # 设置标签的上方间距为 0，下方间距为 5
        # 创建表格
        table = ttk.Treeview(new_frame2, columns=(
        "Company", "Supplier", "Invoice Number", "Transaction Date", "Item", "Quantity", "Total Amount",
        "Matching Quantity"), show="headings")
        table.pack(fill="both", expand=True)

        # 设置表头
        table.heading("Company", text="公司名称")
        table.heading("Supplier", text="供应商名称")
        table.heading("Invoice Number", text="单据编号")
        table.heading("Transaction Date", text="业务日期")
        table.heading("Item", text="物料名称")
        table.heading("Quantity", text="数量")
        table.heading("Total Amount", text="价税合计")
        table.heading("Matching Quantity", text="本次发票匹配数量")

        # 设置表格列的宽度
        table.column("Company", width=100)
        table.column("Supplier", width=100)
        table.column("Invoice Number", width=100)
        table.column("Transaction Date", width=100)
        table.column("Item", width=100)
        table.column("Quantity", width=100)
        table.column("Total Amount", width=100)
        table.column("Matching Quantity", width=100)

        # 添加虚构的表格数据
        data = [
            ["米其林沈阳轮胎有限公司", "嘉世坚国际货运代理(上海)有限公司", 5400111631, "2024-02-02 08:53:32",
             "金龙鱼纯玉米油4L", 12, 628.8, 12],
            ["上海米其林轮胎有限公司", "中信泰富钢铁贸易有限公司", 5400107902, "2024-02-02 08:43:15",
             "*移动通信设备*适用小对讲机保护套1S硅胶保护壳米家户外对讲机3代Lite件", 50, 1262, 50],
            ["上海米其林轮胎有限公司", "中信泰富钢铁贸易有限公司", 5400108169, "2024-02-02 08:44:07",
             "*糖果类食品*列罗唯美斯双拼巧克力礼盒年货龙年情人节礼物新年跨年送女友女朋友", 368, 37892.96, 368],
            ["上海米其林轮胎有限公司", "中信泰富钢铁贸易有限公司", 5400110249, "2024-02-02 08:44:50",
             "*金属制品*手用螺丝攻M16*2", 1, 10.57, 1],
            ["上海米其林轮胎有限公司", "柯尼卡美能达办公系统(中国)有限公司", 5400111611, "2024-02-02 08:45:17",
             "*鉴证咨询服务*咨询服务费", 1, 55837.6, 25],
            ["驰加（上海）汽车用品贸易有限公司", "上海华记洗衣有限公司", 5400111625, "2024-02-02 08:53:38",
             "电线电缆*网线", 1,
             110.74, 1],
            ["上海米其林轮胎有限公司", "上海腾浦起重设备有限公司", 5400111379, "2024-02-02 08:53:49",
             "工业自动控制仪表系统安全光幕", 1, 5498.35, 1],
            ["米其林（中国）投资有限公司", "山东京博中聚新材料有限公司", 5400109303, "2024-02-02 08:53:38",
             "工业自动控制仪表系统塑料座", 100, 257.64, 100],
            ["米其林（中国）投资有限公司", "中信泰富钢铁贸易有限公司", 5400107900, "2024-02-02 08:53:51",
             "*工业自动控制仪表系统跨接剂", 120, 169.5, 120],
            ["米其林（中国）投资有限公司", "中化岩土集团股份有限公司", 5400098220, "2024-02-02 08:53:47",
             "工业自动控制仪表系统接触器", 1, 604.96, 1]
        ]

        # 插入数据到表格中
        for row in data:
            table.insert("", "end", values=row)

        # 创建底部功能框架
        bottom_frame = ttk.Frame(self, style="Right.TFrame", padding=10)
        bottom_frame.pack(fill="y", side="bottom")
        bottom_label = ttk.Label(bottom_frame, text="差额智能化分析", style="primary.TLabel")
        bottom_label.pack()
        # 创建输出框
        output_text = tk.Text(bottom_frame, wrap="word", width=1000, height=20)
        output_text.pack(fill="both", expand=True, padx=10, pady=10)

        # 将输出框置于可滚动区域
        scrollbar = ttk.Scrollbar(right_frame, command=output_text.yview)
        scrollbar.pack(side="right", fill="y")
        output_text.config(yscrollcommand=scrollbar.set)

        # 示例文本
        example_text = "建议核实订单、发票和收货单中的税率和税额是否匹配，确保数据的一致性。修正税额:税额差异可能是由于税率调整、计算精度问题。系统计算的小数点精度问题导致的税额差异，可以调整计算精度以减少误差。特别关注订单中的税率和税额信息，与发票和收货单进行比对，确保一致性。\n"
        output_text.insert("end", example_text)

        # 禁止用户编辑输出框内容
        output_text.config(state="disabled")

        # 创建底部框架
        bottom_frame = ttk.Frame(self, padding=10)
        bottom_frame.pack(fill="x", side="bottom")

        # 添加按钮：取消
        button_cancel = ttk.Button(bottom_frame, text="取消",  style="danger.TButton")
        button_cancel.pack(side="right", padx=5, pady=5)

        # 添加按钮：保存设置
        button_save_settings = ttk.Button(bottom_frame, text="保存",  style="primary.TButton")
        button_save_settings.pack(side="right", padx=5, pady=5)
        self.pack(fill="both")