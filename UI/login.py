import tkinter as tk
from tkinter import ttk, messagebox

from Model.user_model import login_util
from UI.main_application import MainApplication


class Login(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        window_width=450
        window_height = 300
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_top = int(screen_height/2 - window_height/2)
        position_right = int(screen_width/2 - window_width/2)
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.resizable(False,False)
        self.title("登录")
        icon_image = tk.PhotoImage(file="icon2.png")
        self.iconphoto(True,icon_image)
        label_1 = ttk.Label(self,text="用户名",font=("微软雅黑",16))
        label_1.place(x=100,y=50,anchor="nw")
        self.entry_1 = ttk.Entry(self,style="success.TEntry", width=18, font=('微软雅黑', 10))
        self.entry_1.place(x=170,y=50,anchor="nw")
        label_2 = ttk.Label(self,text="密   码",font=("微软雅黑",16))
        label_2.place(x=100,y=100,anchor="nw")
        self.entry_2 = ttk.Entry(self,style="success.TEntry", width=18, font=('微软雅黑', 10),show="*")
        self.entry_2.place(x=170,y=100,anchor="nw")
        button_login = ttk.Button(self,text="登录",style="primary.TButton",command=lambda : self.login_user())
        button_login.place(x=170,y=170,anchor="nw")
        button_close = ttk.Button(self,text="关闭",style="danger.TButton")
        button_close.place(x=280,y=170,anchor="nw")

