import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from UI.Invoice_prepare import InvoicePrepare
from UI.invoice_entry import InvoiceEntry
from UI.invoice_review import InvoiceReview
from UI.main_page import MainPage
from UI.order_match import OrderMatch
from UI.order_prepare import OrderPrepare
from UI.reimburse_management import ReimburseManagement
from UI.warehousing_prepare import WarehousingPrepare


class GlobalFrame(tk.Frame):
    def __init__(self, master,mainWindow):
        tk.Frame.__init__(self, master)
        self.master = master
        self.mainWindow = mainWindow
        self.user_name = self.mainWindow.user_name
        top_frame = ttk.Frame(master, style="primary.TFrame", padding=10)
        top_frame.pack(fill="x")
        self.build_user_frame(top_frame)
        self.build_search_area(top_frame)
        self.pack()


    def show_menu(self,event):
        self.menu.post(event.x_root, event.y_root)


    def build_user_frame(self, top_frame):
        # 创建用户信息框架
        user_frame = ttk.Frame(top_frame, padding=5)
        user_frame.pack(side="right")
        self.menu = tk.Menu(self, tearoff=0)
        self.menu.add_command(label="退出", command=self.mainWindow.close)
        self.menu.add_command(label="注销", command=self.mainWindow.login_page)
        user_frame.bind("<Button-1>", self.show_menu)
        # 加载用户头像图像并调整大小
        self.user_image = Image.open("face-image.jpg")
        self.user_image.thumbnail((50, 50))
        self.user_photo = ImageTk.PhotoImage(self.user_image)

        # 创建用户头像标签
        user_avatar = ttk.Label(user_frame, image=self.user_photo, style="primary.TLabel")
        user_avatar.pack(side="left")
        user_avatar.bind("<Button-1>", self.show_menu)
        user_name = ttk.Label(user_frame, text=self.user_name, font=('微软雅黑', 12, 'bold'))
        user_name.pack(side="left")
        user_name.bind("<Button-1>", self.show_menu)

    def build_search_area(self, top_frame):
        # 创建搜索图标
        self.search_icon = Image.open("search.png")
        self.search_icon = self.search_icon.resize((20, 20), Image.LANCZOS)
        self.search_icon = ImageTk.PhotoImage(self.search_icon)

        # 创建搜索框
        search_entry = ttk.Entry(top_frame, style="success.TEntry", width=18, font=('微软雅黑', 10))
        search_entry.pack(side="left", padx=(25, 5))

        button_home = ttk.Button(top_frame, text="首页", style="primary.Outline.TButton",
                                 command=lambda: self.mainWindow.switch_frame(MainPage))
        button_home.pack(side="left", padx=5)

        button_invoice_entry = ttk.Button(top_frame, text="报销管理",
                                          style="primary.Outline.TButton",
                                          command=lambda: self.mainWindow.switch_frame(ReimburseManagement))
        button_invoice_entry.pack(side="left", padx=5)



        if self.user_name == "财务管理员":
            button_invoice_audit = ttk.Button(top_frame, text="发票审核",
                                              style="primary.Outline.TButton",
                                              command=lambda: self.mainWindow.switch_frame(InvoiceReview))
            button_invoice_audit.pack(side="left", padx=5)
            button_invoice_entry = ttk.Button(top_frame, text="发票入账",
                                              style="primary.Outline.TButton",
                                              command=lambda: self.mainWindow.switch_frame(InvoiceEntry))
            button_invoice_entry.pack(side="left", padx=5)
            button_invoice_entry = ttk.Button(top_frame, text="订单管理",
                                              style="primary.Outline.TButton",
                                              command=lambda: self.mainWindow.switch_frame(OrderPrepare))
            button_invoice_entry.pack(side="left", padx=5)
            button_tri_match = ttk.Button(top_frame, text="三单匹配",
                                          style="primary.Outline.TButton",
                                          command=lambda: self.mainWindow.switch_frame(OrderMatch))
            button_tri_match.pack(side="left", padx=5)
        if self.user_name == "财务员工":
            button_invoice_prep = ttk.Button(top_frame, text="发票预制",
                                             style="primary.Outline.TButton",
                                             command=lambda: self.mainWindow.switch_frame(InvoicePrepare))
            button_invoice_prep.pack(side="left", padx=5)
        if self.user_name == "库房员工":
            button_invoice_prep = ttk.Button(top_frame, text="入库管理",
                                             style="primary.Outline.TButton",
                                             command=lambda: self.mainWindow.switch_frame(WarehousingPrepare))
            button_invoice_prep.pack(side="left", padx=5)
        search_icon_label = ttk.Label(top_frame, image=self.search_icon, style="primary.TLabel")
        search_icon_label.place(relx=0, rely=0.5, anchor="w")
        # 创建顶部按钮





