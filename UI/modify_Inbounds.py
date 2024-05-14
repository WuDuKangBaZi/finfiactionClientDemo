import tkinter as tk
from tkinter import ttk, messagebox

from Model import order, inbounds


class ModifyInbounds(tk.Tk):
    def __init__(self,select_value,master):
        tk.Tk.__init__(self)
        self.select_value = select_value
        self.master = master
        print(select_value)
        self.sap_order = None
        self.buyer_enterprise = None
        self.enterinbound_numb = None
        self.modify_frame = None
        self.convert_page()
        self.title("财务流程自动化 - 入库单修改")

    def convert_page(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.state("normal")
        window_width = 750
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.resizable(False, False)
        self.modify_frame = ttk.Frame(self)
        label_inbound_num = ttk.Label(self.modify_frame,text="入库单号",font=("微软雅黑",16))
        label_inbound_num.place(x=15,y=20,anchor="nw")
        self.enterinbound_numb = ttk.Entry(self.modify_frame, style="success.TEntry", width=18, font=('微软雅黑', 15)) # 输入框
        self.enterinbound_numb.insert(0, self.select_value[1])
        self.enterinbound_numb.place(x=120, y=20, anchor="nw")
        self.enterinbound_numb.config(state="readonly")

        label_inbound_buyer_enterprise = ttk.Label(self.modify_frame, text="采购企业", font=("微软雅黑", 16))
        label_inbound_buyer_enterprise.place(x=380, y=20, anchor="nw")
        self.buyer_enterprise = ttk.Entry(self.modify_frame, style="success.TEntry", width=18, font=('微软雅黑', 15))
        self.buyer_enterprise.insert(0, self.select_value[3])
        self.buyer_enterprise.place(x=480, y=20, anchor="nw")

        lael_total_amount = ttk.Label(self.modify_frame, text="总金额", font=("微软雅黑", 16))
        lael_total_amount.place(x=15, y=70, anchor="nw")
        self.total_amount = ttk.Entry(self.modify_frame, style="success.TEntry", width=18, font=('微软雅黑', 15))
        self.total_amount.place(x=120, y=70, anchor="nw")
        self.total_amount.insert(0,self.select_value[5])
        label_sap_order = ttk.Label(self.modify_frame,text="SAP单号", font=("微软雅黑", 16))
        label_sap_order.place(x=380,y=70, anchor="nw")
        self.sap_order = ttk.Entry(self.modify_frame, style="success.TEntry", width=18, font=('微软雅黑', 15))
        self.sap_order.place(x=480,y=70, anchor="nw")
        self.sap_order.insert(0,self.select_value[6])
        label_inbound_date = ttk.Label(self.modify_frame,text="入库时间",font=("微软雅黑", 16))
        label_inbound_date.place(x=15,y=120, anchor="nw")
        self.inbound_date = ttk.Entry(self.modify_frame, style="success.TEntry", width=18, font=('微软雅黑', 15))
        self.inbound_date.place(x=120, y=120, anchor="nw")
        self.inbound_date.insert(0,self.select_value[7])


        label_order_id  = ttk.Label(self.modify_frame,text="工单ID",font=("微软雅黑", 16))
        label_order_id.place(x=380,y=120, anchor="nw")
        options = ['10032','10042','10052','10053','10054']
        self.order_id = ttk.Combobox(self.modify_frame,font=("微软雅黑", 16),width=17,values=options)
        self.order_id.place(x=480,y=120, anchor="nw")
        self.order_id.set(self.select_value[2])

        label_details = ttk.Label(self.modify_frame,text="入库详情",font=("微软雅黑", 16))
        label_details.place(x=15,y=170, anchor="nw")
        self.details = tk.Text(self.modify_frame,height=8,width=58,font=('微软雅黑', 15))
        self.details.place(x=15,y=220,anchor="nw")
        self.details.insert("1.0",self.select_value[4])
        button_modify = ttk.Button(self.modify_frame,text="保存",style="primary.TButton",command=lambda :self.change_data())
        button_modify.place(x=500,y=460,anchor="nw")

        button_close = ttk.Button(self.modify_frame,text="取消",style="danger.TButton",command=lambda :self.close_page())
        button_close.place(x=600,y=460,anchor="nw")
        self.modify_frame.pack(fill="both",expand=True)

    def close_page(self):
        self.destroy()

    def change_data(self):
        # 保存
        update_ret = inbounds.update(self.select_value[0],self.enterinbound_numb.get(),self.inbound_date.get(),
                        self.details.get("1.0","end"),self.total_amount.get(),
                        self.buyer_enterprise.get(),self.order_id.get(),
                        self.sap_order.get())
        if update_ret:
            self.master.list_inbounds()
            self.destroy()
        else:
            messagebox.showerror("更新失败!")