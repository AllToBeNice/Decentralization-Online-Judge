from tkinter import *
from tkinter import Toplevel
import tkinter.ttk as ttk
from PIL import Image, ImageTk

resultshow_width = '800'
resultshow_height = '450'
resultshow_geo = resultshow_width + 'x' + resultshow_height

#================================================================================================================
# 设置窗口居中显示
def get_screen_size(window):
    return window.winfo_screenwidth(),window.winfo_screenheight()

def get_window_size(window):
    return window.winfo_reqwidth(),window.winfo_reqheight()

def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '{}x{}+{}+{}'.format(width, height, (screenwidth - int(width))//2, (screenheight - int(height))//2)
    # print(size)
    root.geometry(size)

#================================================================================================================
# 信息显示界面函数，传入评测结果Out_Info
def ResultShow():

    resultTocolor = {"Accepted":"green", "Wrong Answer":"red"}
    
    resultshow = Tk()
    resultshow.iconbitmap("F:/Python/Project/Homework/Online_Judge_v_0.1/V_0.1/items/ICO.ico")
    resultshow.title("Submit: ")
    center_window(resultshow, resultshow_width, resultshow_height)
    resultshow.resizable(0, 0)

    # Frame
    frame_bkg = Frame(resultshow)
    frame_top = Frame(resultshow)###
    frame_buttom = Frame(resultshow)
    
    # Canvas背景图片
    canvas_Background = Canvas(frame_bkg, highlightthickness = 0)
    image = Image.open("F:/Python/Project/Homework/Online_Judge_v_0.1/V_0.1/items/3.jpg")
    im = ImageTk.PhotoImage(image)
    canvas_Background.create_image(355, 250, image = im)
    canvas_Background.pack(fill = BOTH, expand = YES)

    # Label
    label_Result = Label(resultshow, text = "Accepted", bg = 'white',
                         font = ('Arial 14 bold'), fg = resultTocolor["Accepted"],
                         width = 50, height = 2, justify = CENTER)
    # Text
    text_Result = Text(frame_buttom)

    # 创建Scrollbar组件，该组件与text_Result的纵、横向滚动关联
    y_scrollbar_Result = Scrollbar(frame_buttom, orient = VERTICAL,
                                 command = text_Result.yview)

    # 组件管理
    label_Result.pack()

    frame_bkg.pack(fill = BOTH, expand = YES)

    canvas_Background.create_window(400, 70, width=180, height=40, window=label_Result)

    # 评测点显示框
    frame_buttom.pack(side = 'top', fill = BOTH, expand = YES)
    y_scrollbar_Result.pack(side = 'right', fill = BOTH, expand = NO)
    text_Result.pack(side = 'left', fill = BOTH, expand = YES)
    # 滚动条设置
    text_Result.configure(yscrollcommand = y_scrollbar_Result.set)

    canvas_Background.create_window(400, 280, width=400, height=280, window=frame_buttom)
    
    resultshow.mainloop()

ResultShow()
