#!\usr\bin\env python3
#-*- encoding: utf-8 -*-
__author__ = 'QCF'

'''
OJ评测系统
V - 0.1

退出函数
'''
from tkinter.ttk import *
from tkinter import Canvas
# from tkinter import Tk
from tkinter import Toplevel
from tkinter import Label
from tkinter import Button
from tkinter import mainloop
from tkinter import Pack
from tkinter import CENTER
from Config import *
from time import sleep
from PIL import Image, ImageTk

# 退出root窗口
def QuitRoot():
    quit_root = root.Toplevel()
    quit_root.title("Attention!")
    center_window(quit_root, quit_root_width, quit_root_height)
    quit_root.resizable(0, 0)

    # Canvas
    q_canvas1 = Canvas(quit_root, highlightthickness = 0, bg = 'white')
    q_canvas1.pack(fill = 'both', expand = 'yes')

    # 图标
    image = Image.open("Attention.gif")
    im = ImageTk.PhotoImage(image)
    Pic1 = Label(q_canvas1, highlightthickness = 0, image = im, bg = 'white')
    Pic1.pack(side = 'top', fill = 'both')

    # Canvas1
    canvas_Button = Canvas(q_canvas1, highlightthickness = 0, bg = 'white')

    # 标签及按钮
    label_Title = Label(q_canvas1, text = "Do you want to quit?", bg = 'white',
                        font =("Arial", 14, "bold"),
                        width = 20, height = 3, justify = CENTER)
    
    button_Yes = Button(canvas_Button,text = 'Yes', bg = 'white',
                        font = ('Arial 13 normal'), fg = '#011640',
                        width = 6, height = 1,
                        justify=CENTER, command = quit)
    
    button_No = Button(canvas_Button, text = 'No', bg = 'white',
                       font = ('Arial 13 normal'), fg = '#011640',
                       width = 6, height = 1,
                       justify=CENTER, command = quit_root.destroy)
    
    # 组件管理
    label_Title.pack(side = 'top', fill = 'both')
    canvas_Button.pack()
    button_Yes.grid(row = 0, column = 0, padx = 20)
    button_No.grid(row = 0, column = 1, padx = 20)
    
    quit_root.mainloop()

# 登入失败窗口
def LoginFailed():
    quit_login_fail = root.Toplevel()
    quit_login_fail.title("Attention!")
    center_window(quit_login_fail, quit_login_fail_width, quit_login_fail_height)
    quit_login_fail.resizable(0, 0)

    
    # Canvas
    l_canvas1 = Canvas(quit_login_fail, highlightthickness = 0, bg = 'white')
    l_canvas1.pack(fill = 'both', expand = 'yes')

    # 图标
    image = Image.open("Attention.gif")
    im = ImageTk.PhotoImage(image)
    Pic2 = Label(l_canvas1, highlightthickness = 0, image = im, bg = 'white')
    Pic2.pack(side = 'top', fill = 'both')

    # 标签及按钮
    label_Title = Label(l_canvas1, text = "Login Failed！", bg = 'white',
                        font =("Arial", 14, "bold"),
                        width = 20, height = 1, justify = CENTER)
    
    label_content = Label(l_canvas1, text = "Incorrect ID or password.\nPlease re-enter.",
                          font =("Arial", 12, "normal"), bg = 'white',
                          width = 50, height = 3, justify=CENTER)
    
    button_Ok = Button(l_canvas1,text = 'Ok', bg = 'white',
                       font = ('Arial 13 normal'), fg = '#011640',
                       width = 6, height = 1, justify=CENTER,
                       command = quit_login_fail.destroy)

    # 组件管理
    label_Title.pack(side = 'top', fill = 'both')
    label_content.pack()
    button_Ok.pack()
    
    quit_login_fail.mainloop()

# 登入成功窗口
def LoginSuccessfully():
    quit_login_success = root.Toplevel()
    quit_login_success.title("Attention!")
    center_window(quit_login_success, quit_login_success_width, quit_login_success_height)
    quit_login_success.resizable(0, 0)

    # Canvas
    s_canvas1 = Canvas(quit_login_success, highlightthickness = 0, bg = 'white')
    s_canvas1.pack(fill = 'both', expand = 'yes')

    # 图标
    image = Image.open("Attention.gif")
    im = ImageTk.PhotoImage(image)
    Pic3 = Label(s_canvas1, highlightthickness = 0, image = im, bg = 'white')
    Pic3.pack(side = 'top', fill = 'both')

    # 标签及按钮
    label_Title = Label(s_canvas1, text = "Login Successfully！", bg = 'white',
                        font =("Arial", 14, "bold"), 
                        width = 20, height = 1, justify = CENTER)
    
    label_content = Label(s_canvas1, text = "Welcome! Administrator: ",
                          font =("Arial", 12, "normal"), bg = 'white',
                          width = 50, height = 3, justify=CENTER)
    
    button_Ok = Button(s_canvas1,text = 'Ok', bg = 'white',
                       font =("Arial", 13, "normal"),
                       width = 6, height = 1, fg = '#011640',
                       justify=CENTER, command = quit_login_success.destroy)

    # 组件管理
    label_Title.pack(side = 'top', fill = 'both')
    label_content.pack()
    button_Ok.pack()
    
    quit_login_success.mainloop()

if __name__ == "__main__":
    QuitRoot()
    LoginFailed()
    LoginSuccessfully()
