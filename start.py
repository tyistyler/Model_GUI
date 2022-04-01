# coding: utf-8
# Name:     start
# Author:   dell
# Data:     2022/3/25

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        # for index in [0, 1]:
        #     # 调节窗体尺寸
        #     self.columnconfigure(index=index, weight=1)     # index表示第几列，weight表示缩放比例，这里设置为1
        #     self.rowconfigure(index=index, weight=1)        # index表示第几行，weight表示缩放比例，这里设置为1

        # 布尔类型变量
        self.var_0 = tk.BooleanVar(value=False)
        self.var_1 = tk.BooleanVar(value=False)
        self.var_2 = tk.BooleanVar(value=False)
        self.var_3 = tk.BooleanVar(value=False)

        self.var_ner = tk.BooleanVar(value=False)
        self.var_joint = tk.BooleanVar(value=False)

        self.setup_widgets()


    # def click_run_button(self):
    #     messagebox.showinfo(title="温馨提示", message="欢迎使用联合抽取模型")

    def setup_widgets(self):

        # =====================================================================================
        # Create a Frame for the Checkbuttons
        # padx-水平方向外边距
        # pady-垂直方向外边距
        # 控件在的起始位置-"e, w, s, n-东、西、南、北"
        # LabelFrame 会在其子组件的周围绘制一个边框以及一个标题
        self.check_frame_data = ttk.LabelFrame(self, text="数据预处理")
        self.check_frame_data.grid(row=0, column=0, padx=50, pady=10, sticky="nsew")        # padx, pady整体布局

        self.check_var_0 = ttk.Checkbutton(self.check_frame_data, text="分字", variable=self.var_0)
        self.check_var_0.grid(row=0, column=0, padx=5, pady=3, sticky="nsew")               # padx, pady控件之间的距离

        self.check_var_1 = ttk.Checkbutton(self.check_frame_data, text="分词", variable=self.var_1)
        self.check_var_1.grid(row=1, column=0, padx=5, pady=3, sticky="nsew")

        self.check_var_2 = ttk.Checkbutton(self.check_frame_data, text="大写", variable=self.var_2)
        self.check_var_2.grid(row=2, column=0, padx=5, pady=3, sticky="nsew")

        self.check_var_3 = ttk.Checkbutton(self.check_frame_data, text="小写", variable=self.var_3)
        self.check_var_3.grid(row=3, column=0, padx=5, pady=3, sticky="nsew")

        self.button_process = ttk.Button(self.check_frame_data, text="预处理")
        self.button_process.grid(row=4, column=0, padx=5, pady=3, sticky="nsew")

        # =====================================================================================
        self.check_frame_input = ttk.LabelFrame(self, text="文本输入")
        self.check_frame_input.grid(row=0, column=1, padx=10, pady=8, sticky="nsew")

        self.input_text = tk.Text(self.check_frame_input, width=50, height=7, autoseparators=False)
        self.input_text.grid(row=0, column=2, padx=10, pady=8, sticky="nsew")

        self.button_read = ttk.Button(self.check_frame_input, text="读入文件")
        self.button_read.grid(row=1, column=2, padx=10, pady=8, sticky="w")
        self.button_clear1 = ttk.Button(self.check_frame_input, text="清空文本")
        self.button_clear1.grid(row=1, column=2, padx=10, pady=8, sticky="e")

        self.check_frame_process = ttk.LabelFrame(self, text="数据预处理结果")
        self.check_frame_process.grid(row=0, column=2, padx=10, pady=8, sticky="nsew")

        self.processed_text = tk.Text(self.check_frame_process, width=50, height=7, autoseparators=False)
        self.processed_text.grid(row=0, column=1, padx=10, pady=8, sticky="nsew")

        self.button_clear2 = ttk.Button(self.check_frame_process, text="清空文本")
        self.button_clear2.grid(row=1, column=1, padx=10, pady=8, sticky="e")
        # =====================================================================================
        # 左下方-模型选择部分
        self.check_frame_model = ttk.LabelFrame(self, text="模型选择")
        self.check_frame_model.grid(row=1, column=0, padx=50, pady=10, sticky="nsew")

        self.check_var_ner = ttk.Checkbutton(self.check_frame_model, text="实体识别", variable=self.var_ner)
        self.check_var_ner.grid(row=0, column=0, padx=5, pady=3, sticky="nsew")

        # 下拉框
        self.model_ner = ttk.Combobox(self.check_frame_model)
        self.model_ner["value"] = ("Baseline", "NE-Transformer")
        self.model_ner.current(0)
        self.model_ner.grid(row=1, column=0, padx=5, pady=3, sticky="nsew")

        # 复选按钮
        self.check_var_joint = ttk.Checkbutton(self.check_frame_model, text="联合抽取", variable=self.var_joint)
        self.check_var_joint.grid(row=2, column=0, padx=5, pady=3, sticky="nsew")

        # 下拉框
        self.model_joint = ttk.Combobox(self.check_frame_model)
        self.model_joint["value"] = ("Baseline", "PaD-Casrel")
        self.model_joint.current(0)
        self.model_joint.grid(row=3, column=0, padx=5, pady=3, sticky="nsew")

        self.button_run = ttk.Button(self.check_frame_model, text="运行")
        self.button_run.grid(row=4, column=0, padx=5, pady=3, sticky="nsew")

        # =====================================================================================
        self.check_frame_pred = ttk.LabelFrame(self, text="模型预测")
        self.check_frame_pred.grid(row=1, column=1, padx=10, pady=8, sticky="nsew")
        #
        self.input_text = tk.Text(self.check_frame_pred, width=50, height=7, autoseparators=False)
        self.input_text.grid(row=0, column=0, padx=10, pady=8, sticky="nsew")

        self.button_dedup = ttk.Button(self.check_frame_pred, text="结果去重")
        self.button_dedup.grid(row=1, column=0, padx=10, pady=8, sticky="w")
        self.button_clear3 = ttk.Button(self.check_frame_pred, text="清空文本")
        self.button_clear3.grid(row=1, column=0, padx=10, pady=8, sticky="e")

        self.check_frame_result = ttk.LabelFrame(self, text="结果展示")
        self.check_frame_result.grid(row=1, column=2, padx=10, pady=8, sticky="nsew")

        self.processed_text = tk.Text(self.check_frame_result, width=50, height=7, autoseparators=False)
        self.processed_text.grid(row=0, column=0, padx=10, pady=8, sticky="nsew")
        self.button_save1 = ttk.Button(self.check_frame_result, text="保存结果")
        self.button_save1.grid(row=1, column=0, padx=10, pady=8, sticky="w")


        self.button_clear4 = ttk.Button(self.check_frame_result, text="清空文本")
        self.button_clear4.grid(row=1, column=0, padx=10, pady=8, sticky="e")

if __name__ == "__main__":
    # 1、设计图形界面
    root = tk.Tk()
    root.title("实体关系抽取模型")
    # 设置主窗口属性
    root.geometry("1100x500")
    # root.iconbitmap("favicon.ico")

    # simple set the theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "light")

    app = App(root)
    # 将各组件放置在主窗口内
    app.pack(fill="both", expand="True")

    # set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())

    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))
    root.mainloop()
