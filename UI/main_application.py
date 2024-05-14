import tkinter as tk
from tkinter import ttk, messagebox

import ttkbootstrap as ttkbs

from Model import order, invoice, inbounds
from Model.user_model import login_util
from UI.globalFrame import GlobalFrame
from UI.main_page import MainPage


class MainApplication(tk.Tk):
    def load_main(self):
        print("load_main")
        self.pageName = ""
        self.state("zoomed")
        self._frame = None
        icon_image = tk.PhotoImage(file="icon.png")
        self.iconphoto(True, icon_image)
        self.title(f"财务流程自动化")
        style = ttkbs.Style(theme="minty")
        self.geometry(None)
        self.resizable(True, True)
        top_frame = ttk.Frame(self, style="primary.TFrame", padding=10)
        top_frame.pack(fill="x")
        GlobalFrame(top_frame, self)
        self.switch_frame(MainPage)


    def login_page(self):
        print("login_page")
        for widget in self.winfo_children():
            widget.destroy()
        self.user_name = None
        self.state("normal")
        self.login_frame = ttk.Frame(self)
        window_width = 450
        window_height = 300
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.resizable(False, False)
        self.title("登录")
        icon_image = tk.PhotoImage(file="icon2.png")
        self.iconphoto(True, icon_image)
        label_1 = ttk.Label(self.login_frame, text="用户名", font=("微软雅黑", 16))
        label_1.place(x=100, y=50, anchor="nw")
        self.entry_1 = ttk.Entry(self.login_frame, style="success.TEntry", width=18, font=('微软雅黑', 10))
        self.entry_1.place(x=170, y=50, anchor="nw")
        label_2 = ttk.Label(self.login_frame, text="密   码", font=("微软雅黑", 16))
        label_2.place(x=100, y=100, anchor="nw")
        self.entry_2 = ttk.Entry(self.login_frame, style="success.TEntry", width=18, font=('微软雅黑', 10), show="*")
        self.entry_2.place(x=170, y=100, anchor="nw")
        self.entry_2.bind("<Return>", lambda event: self.login_user())
        button_login = ttk.Button(self.login_frame, text="登录", style="primary.TButton",
                                  command=lambda: self.login_user())
        button_login.place(x=170, y=170, anchor="nw")
        button_close = ttk.Button(self.login_frame, text="关闭", style="danger.TButton", command=lambda: self.close())
        button_close.place(x=280, y=170, anchor="nw")
        self.login_frame.pack(expand=True, fill="both")

    def __init__(self):
        tk.Tk.__init__(self)
        self.entry_1 = None
        self._frame = None
        self.login_frame = None
        self.pageName = None
        self.login_page()


    def close(self):
        self.destroy()

    def login_user(self):
        # 获取输入的用户名和密码
        account = self.entry_1.get()
        password = self.entry_2.get()
        if account == "" or password == "":
            messagebox.showerror("提示", "用户名或密码不能为空")
            return
        # 查询数据库
        result = login_util(account, password)
        if len(result) > 0:
            print("登录成功")
            self.user_name = result[0][0]
            self.login_frame.destroy()
            self.load_main()
        else:
            messagebox.showerror("登录失败!","账号或密码输入错误!")

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
            self.update()
        self._frame = new_frame
        self._frame.pack(expand=True)
