import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import ttkbootstrap as ttkbs


class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # 搜索图标
        # 创建顶部框架
        self.search_icon = None
        self.master = master
        master.title("财务流程自动化")
        self.user_image = None
        self.build_image_frame()
        self.pack()


    def build_image_frame(self):
        # 创建图片框架
        image_frame = ttk.Frame(self)
        image_frame.pack(expand=True)

        # 加载大图片
        self.big_image = Image.open("1aa06e2f20de49f33583fc28d0f5ce1.jpg")

        # 调整大小并保持长宽比
        width, height = 1300, 500
        aspect_ratio = self.big_image.width / self.big_image.height
        if aspect_ratio > (width / height):
            self.big_image = self.big_image.resize((int(height * aspect_ratio), height), Image.LANCZOS)
        else:
            self.big_image = self.big_image.resize((width, int(width / aspect_ratio)), Image.LANCZOS)

        self.big_photo = ImageTk.PhotoImage(self.big_image)

        big_image_label = ttk.Label(image_frame, image=self.big_photo)
        big_image_label.pack()

        # 创建小图片框架
        small_images_frame = ttk.Frame(self)
        small_images_frame.pack(pady=5)  # 将整个小图片框架向上移动20像素
        # 加载小图片1
        small_image1 = Image.open("64631e1b75ae8349bda334ca26e2c5f.jpg")
        small_image1.thumbnail((450, 250), Image.LANCZOS)  # 调整大小并保持比例
        self.small_photo1 = ImageTk.PhotoImage(small_image1)
        # 调整大小并保持比例

        small_image_label1 = ttk.Label(small_images_frame, image=self.small_photo1)
        small_image_label1.pack(side="left", padx=5)

        # 加载小图片2
        small_image2 = Image.open("b1935a52540eaacc8224142dad19085.jpg")
        small_image2.thumbnail((450, 250), Image.LANCZOS)  # 调整大小并保持比例
        self.small_photo2 = ImageTk.PhotoImage(small_image2)

        small_image_label2 = ttk.Label(small_images_frame, image=self.small_photo2)
        small_image_label2.pack(side="left", padx=5)

        # 加载小图片3
        small_image3 = Image.open("1e0c406d9625094b70c57c72b2524b5.jpg")
        small_image3.thumbnail((450, 250), Image.LANCZOS)  # 调整大小并保持比例
        self.small_photo3 = ImageTk.PhotoImage(small_image3)

        small_image_label3 = ttk.Label(small_images_frame, image=self.small_photo3)
        small_image_label3.pack(side="left", padx=5)
