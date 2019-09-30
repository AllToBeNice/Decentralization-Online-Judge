#!/usr/bin/env python3
#-*- encoding: utf-8 -*-
__author__ = 'QCF'

'''
OJ评测系统
V - 0.1
'''

'''
注意：
1、语句后标明#或###的为调试语句
'''

import os
import sys
import time
from tkinter import *
from tkinter import Toplevel
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
from tkinter.simpledialog import askstring, askinteger, askfloat
from tkinter import messagebox

from PIL import Image, ImageTk
from chardet import detect

from Config import *
import Core

global administrator_accounts, student_accounts

# 测试账号（Future Functions）
administrator_accounts = {'QCF':{'Name':'QCF','Pwd':'123456'}}
student_accounts = {'test':{'Name':'test','Pwd':'123456'}}


#=======================================================================================
#评测开始函数，使用语言名、题目名、测试点字典、代码目录、测试点目录
def OJBegin():
    ymd = time.strftime("%Y%m%d")
    # 评测文件所在目录
    A_Path = "./Answers/" + ymd + "/"
    # 语言名、题目名、文件名
    Q_Lan, Q_Name, F_Name = OJPrepare()

    # 本机含多个版本python3，因此测试环境使用“python37”shell命令。
    if Q_Lan == "Python3":
        Q_Lan  = Q_Lan.lower() + '7'
    else:
        Q_Lan  = Q_Lan.lower()

    # 默认python的shell命令为“python2”、“python3”、“gcc”    
    # Q_Lan  = Q_Lan.lower()

    # 程序文件目录
    A_Dir = A_Path + F_Name
    # 测试点存放目录
    T_Dir = A_Path + Q_Name
    
    print(Q_Name, A_Dir, T_Dir)#
    print(testpoint)#
    
    n = testpoint[Q_Name]
    
    # OJ()函数依次执行的函数
    '''
    Core.Security(A_Path, F_Name)#
    Core.Compile(Q_Lan, A_Path, F_Name)#
    Core.Time(Q_Lan, A_Path, F_Name, '1')#
    Core.Memory(Q_Lan, A_Path, F_Name, '1')#
    Core.JudgeResult(A_Path, F_Name, '1')#
    '''
    
    Result = Core.OJ(Q_Lan, n, A_Path, F_Name)
    
    print(Result)#
    
    ResultShow(Result)


#=======================================================================================
# 评测准备函数，保存并重命名代码文件到指定目录
def OJPrepare():
    global text_Code
    # 语言对应文件扩展名
    LanToName = {"C":".c", "C++":".cpp", "Python2":".py", "Python3":".py"}
    
    # 评测程序相对路径
    direction = "./Answers/"
    ymd = time.strftime("%Y%m%d")
    # Answers Path
    A_Path = direction + ymd + "/"
    
    # 检测文件夹是否存在
    if os.path.exists(A_Path) == False:
        os.mkdir(A_Path)
    # 获取题目名和语言名
    Q_Lan = combobox_language.get()
    Q_Name = combobox_question.get()
    F_Name = Q_Name + LanToName[Q_Lan]
    # 储存为文件
    text = text_Code.get(1.0, END)

    print(text)#
    # 更换Tab键为4个空格
    text.expandtabs(4)
    
    with open(A_Path + F_Name, "w") as fw:
        fw.write(text)
        fw.close()
    submitmenu.destroy()
    return (Q_Lan, Q_Name, F_Name)


#=======================================================================================
# 管理员修改时空限制函数
def TimeChange():
    # 获取输入的时间限制（ms）
    new_TimeLimit = entry_Time.get()
    # 逐行读入Config.py文件，更改后再逐行写入
    with open("./Config.py", "r", encoding = "utf-8") as fr:
        lines = fr.readlines()
        fr.close()
    for i in range(len(lines)):
        print(i)
        if "time_limit = " in lines[i]:
            lines[i] = "time_limit = " + new_TimeLimit
    with open("./Config.py", "w", encoding = "utf-8") as fw:
        fw.writelines(lines)
        fw.close()


def MemoChange():
    new_MemoLimit = entry_Memo.get()
    with open("./Config.py", "r", encoding = "utf-8") as fr:
        lines = fr.readlines()
    for i in range(len(lines)):
        if "memo_limit = " in lines[i]:
            lines[i] = "memo_limit = " + new_MemoLimit
    with open("./Config.py", "w", encoding = "utf-8") as fw:
        fw.writelines(lines)
        fw.close()


#=======================================================================================
# 信息显示界面函数，传入Out_Info字典
# Out_Info = {"response":None, "msg":None, "threat_level":None,"result":None, "back_info":None}
def ResultShow(InfoDict):
    resultshow = Toplevel()
    # 设置GUI图标、标题、显示位置
    resultshow.iconbitmap("./items/ICO.ico")
    resultshow.title("Submit: ")
    center_window(resultshow, resultshow_width, resultshow_height)
    resultshow.resizable(0, 0)
    # 评测结果与颜色对应
    resultTocolor = {"Accepted":"green", "Wrong Answer":"red", "Compile Error":"red",
                     "Time Limit Exceeded":"red", "Memory Limit Exceeded":"red", "Runtime Error":"red",
                     "Runing Wrong":"red", "Presentation Error":"red", "Output Limit Exceeded":"red",
                     "Runing Dangerous!":"red",
                     }

    # Frame，背景和Text
    frame_bkg = Frame(resultshow)
    frame_buttom = Frame(resultshow)
    # Background
    canvas_Background = Canvas(frame_bkg, highlightthickness = 0)
    image = Image.open("./items/3.jpg")
    im = ImageTk.PhotoImage(image)
    canvas_Background.create_image(355, 250, image = im)
    canvas_Background.pack(fill = BOTH, expand = YES)

    # Label
    label_Result = Label(resultshow, text = InfoDict["result"], bg = 'white',
                         font = ('Arial 14 bold'), fg = resultTocolor[InfoDict["result"]],
                         width = 50, height = 2, justify = CENTER)
    # Text
    text_Result = Text(frame_buttom, font = ('Arial 14 normal'))

    # 创建Scrollbar组件，该组件与text_Result的纵、横向滚动关联
    y_scrollbar_Result = Scrollbar(frame_buttom, orient = VERTICAL,
                                 command = text_Result.yview)

    # 组件管理
    frame_bkg.pack(fill = BOTH, expand = YES)
    label_Result.pack()
    canvas_Background.create_window(400, 70, width=200, height=40, window = label_Result)

    # 评测点显示框
    frame_buttom.pack(side = 'top', fill = BOTH, expand = YES)
    y_scrollbar_Result.pack(side = 'right', fill = BOTH, expand = NO)
    text_Result.pack(side = 'left', fill = BOTH, expand = YES)
    # 滚动条设置
    text_Result.configure(yscrollcommand = y_scrollbar_Result.set)
    # 设置Text显示
    canvas_Background.create_window(400, 280, width=400, height=280, window = frame_buttom)

    # Text插入格式化字符串
    for i in range(1, len(InfoDict["back_info"])+1):
        text_Result.insert(INSERT, "Test "+ str(i) +":\n")
        text_Result.insert(INSERT, "Time(ms): " + str(InfoDict["back_info"][i]["Time(ms)"]) + "\n")
        text_Result.insert(INSERT, "Memory(kb): " + str(InfoDict["back_info"][i]["Memory(kb)"]) + "\n")
        text_Result.insert(INSERT, "Info: " + str(InfoDict["back_info"][i]["Info"]) + "\n")
    # 设置Text不可编辑
    text_Result.config(state = DISABLED)
    resultshow.mainloop()

    

#=======================================================================================
# Submit界面生成函数，选择题目、语言
def Submit(number, dic):
    global submitmenu
    submitmenu = Toplevel()
    submitmenu.title("Submit: ")
    center_window(submitmenu, submitmenu_width, submitmenu_height)
    submitmenu.resizable(0, 0)

    # Frame1
    frame_top = Frame(submitmenu)
    frame_buttom = Frame(submitmenu, bg = 'white')

    # Canvas
    canvas_select = Canvas(frame_buttom, highlightthickness = 0, bg = 'white')

    # 按钮
    button_OK = Button(canvas_select,text = 'OK', bg = 'white',
                          font = ('Arial 13 bold'), fg = '#011640',
                          width = 6, height = 1, relief = 'flat',
                          justify=CENTER, command = lambda:OJBegin())
    
    button_Concel = Button(canvas_select, text = 'Concel', bg = 'white',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 6, height = 1, relief = 'flat',
                          justify=CENTER, command = submitmenu.destroy)

    # 标签
    label_Title = Label(frame_top, text = "Select Question and Labguage: ", bg = 'white',
                        font =("Arial", 16, "bold"),
                        width = 20, height = 3, justify = CENTER)

    label_question = Label(canvas_select, text = "Question: ", bg = 'white',
                        font =("Arial", 14, "normal"),
                        width = 20, height = 3, justify = CENTER)

    label_language = Label(canvas_select, text = "Language: ", bg = 'white',
                        font =("Arial", 14, "normal"),
                        width = 20, height = 3, justify = CENTER)
    
    # 下拉菜单
    global combobox_question
    global combobox_language
    
    select_question = StringVar()
    combobox_question = ttk.Combobox(canvas_select, width = 40, textvariable = select_question)
    combobox_question["value"] = tuple([i for i in dic.keys()])
    combobox_question.current(0)

    select_language = StringVar()
    combobox_language = ttk.Combobox(canvas_select, width = 40, textvariable = select_language)
    combobox_language["value"] = ("C", "C++", "Python2", "Python3", "Java", "R")
    combobox_language.current(0)

    # 组件管理
    frame_top.pack(side = "top", fill = BOTH, expand = YES)
    frame_buttom.pack(side = "top", fill = BOTH, expand = YES)

    canvas_select.pack()
    
    label_Title.pack(side = "top", fill = BOTH, expand = YES)
    
    label_question.grid(row = 0, column = 0)
    combobox_question.grid(row = 0, column = 1)
    label_language.grid(row = 1, column = 0)
    combobox_language.grid(row = 1, column = 1)
    button_OK.grid(row = 2, column = 0)
    button_Concel.grid(row = 2, column = 1, columnspan = 3)

    
    submitmenu.mainloop()



#=======================================================================================
# 字符串搜索函数
def StringSearch(string, target):
    n = len(target)
    des_list = []
    for i in range(len(string) - n + 1):
        if string[i:i+n] == target:
            des_list.append((i, i+n))
    return des_list


#=======================================================================================
# 帮助函数，输出帮助信息
def App_Help():
    apphelp = Toplevel()
    apphelp.title("Attention!")
    center_window(apphelp, apphelp_width, apphelp_height)
    apphelp.resizable(1, 1)

    # Text显示
    text_Help = Text(apphelp, width = apphelp_width, height = apphelp_height,
                     undo = True, maxundo = 20,
                     font=('Arial', 14, 'normal'), state = NORMAL)
    
    # 创建Scrollbar组件，该组件与Text的纵向滚动关联
    y_scrollbar_help = Scrollbar(apphelp, orient = VERTICAL,
                                 command = text_Help.yview)
    text_Help.grid(row = 0, column = 0)
    y_scrollbar_help.grid(row = 0, column = 1, sticky = N + S + E)
    text_Help.insert(INSERT, help_content)
    text_Help.focus_force()
    # 设置Text不可编辑
    text_Help.config(state = DISABLED)
    apphelp.mainloop()


#==========================================================================================
# Menu函数
def menu11(TEXT):
    'open'
    try:
        global fname
        fname = filedialog.askopenfilename(title='Select your code file: ', filetypes=[('All Files', '*'), ('All Files', '*')],initialdir='./')
        # print(fname, type(fname))
        with open(fname, 'rb') as fo:
            text = fo.read()
            # 获取文件编码格式，便于打开写入Text
            encode_method = detect(text)["encoding"]
            fo.close()
        # print(detect(text))
    except:
        pass
        # TEXT.config(state = NORMAL)
        # TEXT.insert(INSERT, '\nWrong!\n')
    else:
        TEXT.config(state = NORMAL)
        TEXT.insert(INSERT, text.decode(encode_method))


def menu12(TEXT):
    'save'
    global fname
    try:
        msg = TEXT.get(1.0,END)
        with open(filename,'w', encoding = 'utf-8') as fw:
            fw.write(msg)
            fw.close()
    except NameError:
        messagebox.showinfo("Attention!","Document not open yet.")
    # 即点击save后又关闭抛出的异常
    except FileNotFoundError:
        saveas(TEXT)


def menu13(TEXT):
    'saveas'
    try:
        fsname = filedialog.asksaveasfilename(initialfile= 'untitled', filetypes=[('All Files', '*'), ('All Files', '*')])
        TEXT.config(state = NORMAL)
        msg = TEXT.get(1.0,END)
        with open(fsname, 'w', encoding = 'utf-8') as fw:
            fw.write(msg)
            fw.close()
    except FileNotFoundError:
        pass


def menu21(TEXT):
    'clear'
    TEXT.config(state = NORMAL)
    TEXT.delete('1.0', END)


def menu22(TEXT):
    'search'
    # 删除原有tag
    try:
        TEXT.tag_delete("tag1")
    except:
        pass
    temp_string = askstring("Attention","Please input the string:")
    TEXT.config(state = NORMAL)
    # 设定光标在末尾，并获取行数（1开始）
    TEXT.mark_set(INSERT, END)
    rows = (TEXT.index(INSERT).split('.'))[0]
    # print(rows)
    
    try:
        for i in range(1, int(rows)+1):
            # print(str(i)+'.0', str(i)+'.end')
            s = 0
            line_text = TEXT.get(str(i)+'.0', str(i)+'.end')
            # 调用StringSearch()函数搜索指定字符串
            des_list = StringSearch(line_text, temp_string)
            if len(des_list) != 0:
                for item in des_list:
                    TEXT.tag_add("tag1", str(i)+'.'+str(item[0]), str(i)+'.'+str(item[1]))
                    TEXT.tag_config("tag1", background = "yellow", foreground = "red")
    except:
        pass

def menu23(TEXT):
    'substitution'
    target_string = askstring("Attention!","Search:")
    sub_string = askstring("Attention!","Substitution:")
    TEXT.config(state = NORMAL)
    # 设定光标在末尾，并获取行数（1开始）
    TEXT.mark_set(INSERT, END)
    rows = (TEXT.index(INSERT).split('.'))[0]
    
    try:
        for i in range(1, int(rows)+1):
            s = 0
            line_text = TEXT.get(str(i)+'.0', str(i)+'.end')
            # 调用StringSearch()函数搜索指定字符串
            des_list = StringSearch(line_text, target_string)
            if len(des_list) != 0:
                # （每行）插入后偏移量
                delta = 0
                for item in des_list:
                    print("des", i, item)
                    TEXT.mark_set("mark1", str(i)+'.'+str(item[0] + delta))
                    print("mark", str(i)+'.'+str(item[0] + delta))
                    TEXT.insert("mark1", sub_string)
                    delta += len(sub_string) 
                    print(str(i)+'.'+str(item[0] + delta), str(i)+'.'+str(item[1] + delta))
                    TEXT.delete(str(i)+'.'+str(item[0] + delta), str(i)+'.'+str(item[1] + delta))
                    delta -= len(target_string)
    except:
        pass
# 以下内容未完成，包括切换语言、切换主题
def menu31():
    'Chinese'
    pass
def menu32():
    'English'
    pass
def menu41():
    'Theme'
    pass


#=======================================================================================
# 菜单栏生成函数
def Menu_Generate(MainWindow, TEXT):
    callback_tuple = (menu11, menu12, menu13, menu21, menu22, menu23, menu31, menu32, menu41)

    Menubar = Menu(MainWindow)
    
    # 菜单栏列表  
    '''
    Menubar.add_command(label = "File", )
    Menubar.add_command(label = "Edit", )
    Menubar.add_command(label = "Language", )
    Menubar.add_command(label = "Option", )
    Menubar.add_command(label = "Help", command = App_Help)
    Menubar.add_command(label = "Quit", command = QuitMainWindow)
    '''

    i = 0
    filemenu1 = Menu(Menubar, tearoff = 0)
    filemenu1.add_command(label = "Open", accelerator = "Ctrl+Shift+O", command = lambda: menu11(TEXT))
    filemenu1.add_separator()
    filemenu1.add_command(label = "Save", accelerator = "Ctrl+Shift+S", command = lambda: menu12(TEXT))
    filemenu1.add_separator()
    filemenu1.add_command(label = "Save As", accelerator = "Ctrl+Alt+S", command = lambda: menu13(TEXT))
    filemenu1.add_separator()
    i += 3
    Menubar.add_cascade(label = "File", menu = filemenu1)

    filemenu2 = Menu(Menubar, tearoff = 0)
    filemenu2.add_command(label = "Clear", accelerator = "Ctrl+Shift+L", command = lambda: menu21(TEXT))
    filemenu2.add_separator()
    filemenu2.add_command(label = "Search", accelerator = "Ctrl+Shift+F", command = lambda: menu22(TEXT))
    filemenu2.add_separator()
    filemenu2.add_command(label = "Substitution", accelerator = "Ctrl+Shift+H", command = lambda: menu23(TEXT))
    filemenu2.add_separator()
    i += 3
    Menubar.add_cascade(label = "Edit", menu = filemenu2)

    filemenu3 = Menu(Menubar, tearoff = 0)
    for item3 in ("Chinese", "English"):
        # print(item3, i)
        filemenu3.add_command(label = item3, command = callback_tuple[i])
        filemenu3.add_separator()
        i += 1
    Menubar.add_cascade(label = "Language", menu = filemenu3)

    filemenu4 = Menu(Menubar, tearoff = 0)
    for item4 in ("Theme",):
        # print(item4, i)
        filemenu4.add_command(label = item4, command = callback_tuple[i])
        filemenu4.add_separator()
        i += 1
    Menubar.add_cascade(label = "Option", menu = filemenu4)

    MainWindow['menu'] = Menubar

    Menubar.add_command(label = "Help", command = App_Help)
    Menubar.add_command(label = "Quit", command = lambda:QuitMainWindow(MainWindow))

    # 快捷键绑定
    MainWindow.bind("<Control-O>", lambda event:menu11(TEXT))
    MainWindow.bind("<Control-S>", lambda event:menu12(TEXT))
    MainWindow.bind("<Control-Alt-S>", lambda event:menu13(TEXT))
    MainWindow.bind("<Control-L>", lambda event:menu21(TEXT))
    MainWindow.bind("<Control-F>", lambda event:menu22(TEXT))
    MainWindow.bind("<Control-H>", lambda event:menu23(TEXT))


#==================================================================================
# 读入题目
# 读入当天题目，返回题目个数及测试点字典
def Questions_In(text_Question, QOrder = "A.qst"):

    menu21(text_Question)

    ymd = time.strftime("%Y%m%d")
    
    # 默认初始打开A题，若无题目，打印"No Test Today."
    try:
        Q_path = "./Questions/" + ymd + "/" + QOrder
        with open(Q_path, "rb") as fr:
            questions = fr.read()
            encode_method = detect(questions)["encoding"]
            fr.close()
    except FileNotFoundError:
        questions = "No Test Today."
    
    
    # 写入text组件，并设置为不可读写（disabled）
    text_Question.config(state = NORMAL)
    try:
        text_Question.insert(INSERT, questions.decode(encode_method))
    except:
        text_Question.insert(INSERT, questions)
    text_Question.config(state = DISABLED)

    # 读取config文件，获取题目个数及各题测试点个数字典
    try:
        C_path = "./Questions/" + ymd + "/" + "config"
        with open(C_path, "r") as fr:
            Q_info = fr.read().replace("\r", '').split("\n")
            fr.close()
        
        # 处理信息
        try:
            n = int(Q_info[0])
        except ValueError:
            return (-1, {})

        testpoint = {}
        try:
            for i in range(0, int(len(Q_info[1])), 2):
                testpoint[Q_info[1][i]] = int(Q_info[1][i+1])
            print((n, testpoint))
            return (n, testpoint)
        except:
            return (-1, {})
        
    except FileNotFoundError:
        return (-1, {})


#====================================================================================
# 登入函数
def Login():
    NameIn = entry_Name.get().strip()
    PwdIn = entry_Pwd.get()
    A_temp = administrator_accounts.get(NameIn)
    S_temp = student_accounts.get(NameIn)
    if  A_temp == None and S_temp == None:
        LoginFailed()
    elif A_temp != None and PwdIn != A_temp['Pwd']:
        LoginFailed()
    elif S_temp != None and PwdIn != S_temp['Pwd']:
        LoginFailed()
    elif A_temp != None and PwdIn == A_temp['Pwd']:
        LoginSuccessfully()
        AdministratorMenu()
    elif S_temp != None and PwdIn == S_temp['Pwd']:
        LoginSuccessfully()
        StudentMenu()


#============================================================================================
# 登入失败窗口
def LoginFailed():
    quit_login_fail = Toplevel()
    quit_login_fail.title("Attention!")
    center_window(quit_login_fail, quit_login_fail_width, quit_login_fail_height)
    quit_login_fail.resizable(0, 0)

    
    # Canvas
    l_canvas1 = Canvas(quit_login_fail, highlightthickness = 0, bg = 'white')
    l_canvas1.pack(fill = 'both', expand = 'yes')

    # 图标
    image = Image.open("./items/Attention1.gif")
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
    button_Ok.focus_set()
    quit_login_fail.bind("<Return>", lambda x:quit_login_fail.destroy())

    # 组件管理
    label_Title.pack(side = 'top', fill = 'both')
    label_content.pack()
    button_Ok.pack()
    
    quit_login_fail.mainloop()


# 登入成功窗口
def LoginSuccessfully():
    quit_login_success = Toplevel()
    quit_login_success.title("Attention!")
    center_window(quit_login_success, quit_login_success_width, quit_login_success_height)
    quit_login_success.resizable(0, 0)

    # Canvas
    s_canvas1 = Canvas(quit_login_success, highlightthickness = 0, bg = 'white')
    s_canvas1.pack(fill = 'both', expand = 'yes')

    # 图标
    image = Image.open("./items/Attention2.png")
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
                       justify=CENTER, command = root.destroy)
    button_Ok.focus_set()
    quit_login_success.bind("<Return>", lambda x:root.destroy())
    ### 注意：这里使用的是root.destroy()而不是quit_login_success.destroy()。
    ### 注意：这里使用lambda需要定义事件变量，然后不传入。

    # 组件管理
    label_Title.pack(side = 'top', fill = 'both')
    label_content.pack()
    button_Ok.pack()
    quit_login_success.mainloop()


# 离开主界面（程序）函数
def QuitMainWindow(quit_mainwindow):
    quit_mainwindow = Toplevel()
    quit_mainwindow.title("Attention!")
    center_window(quit_mainwindow, quit_mainwindow_width, quit_mainwindow_height)
    quit_mainwindow.resizable(0, 0)

    # Canvas
    q_canvas = Canvas(quit_mainwindow, highlightthickness = 0, bg = 'white')
    q_canvas.pack(fill = 'both', expand = 'yes')

    # 图标
    image = Image.open("./items/Attention1.gif")
    im = ImageTk.PhotoImage(image)
    Pic = Label(q_canvas, highlightthickness = 0, image = im, bg = 'white')
    Pic.pack(side = 'top', fill = 'both')

    # Canvas1
    canvas_Button = Canvas(q_canvas, highlightthickness = 0, bg = 'white')

    # 标签及按钮
    label_Title = Label(q_canvas, text = "Do you want to quit?", bg = 'white',
                        font =("Arial", 14, "bold"),
                        width = 20, height = 3, justify = CENTER)
    
    button_Yes = Button(canvas_Button,text = 'Yes', bg = 'white',
                        font = ('Arial 13 normal'), fg = '#011640',
                        width = 6, height = 1,
                        justify=CENTER, command = quit)
    
    button_No = Button(canvas_Button, text = 'No', bg = 'white',
                       font = ('Arial 13 normal'), fg = '#011640',
                       width = 6, height = 1,
                       justify=CENTER, command = quit_mainwindow.destroy)
    button_Yes.focus_set()
    
    quit_mainwindow.bind("<Return>", lambda x:quit())
    quit_mainwindow.bind("<Escape>", lambda x:quit_mainwindow.destroy())
    
    # 组件管理
    label_Title.pack(side = 'top', fill = 'both')
    canvas_Button.pack()
    button_Yes.grid(row = 0, column = 0, padx = 20)
    button_No.grid(row = 0, column = 1, padx = 20)
    
    quit_mainwindow.mainloop()


#===============================================================================
# 管理员页面设置
def AdministratorMenu():
    administrator = Tk()
    administrator.iconbitmap("./items/ICO.ico")
    administrator.title("Online Judge(version-0.1) Administrator")
    center_window(administrator, administrator_width, administrator_height)
    administrator.resizable(1, 1)

    # Frame
    frame_Left = Frame(administrator,bg='red')
    frame_Middle = Frame(administrator,bg='white')
    frame_Right = Frame(administrator,bg='white')

    # 代码展示框
    text_Show = Text(frame_Left, width = code_width, height = code_height,
                     undo = True, maxundo = 20,
                     font = ('Arial 14 normal'))
    # Label
    lable_Timelimit = Label(frame_Right, text = "Time Limit(ms):", bg = 'white',
                            font = ('Arial 14 bold'),fg = '#256D69',
                            width = 15, height =1, justify = CENTER)
    lable_Memolimit = Label(frame_Right, text = "Memory Limit(Kb):", bg = 'white',
                            font = ('Arial 14 bold'),fg = '#256D69',
                            width = 15, height = 1, justify = CENTER)
    # Entry
    global entry_Time
    global entry_Memo
    var_Time = StringVar()
    entry_Time = Entry(frame_Right, width = 20, textvariable = var_Time)
    var_Memo = StringVar()
    entry_Memo = Entry(frame_Right, width = 20, textvariable = var_Memo)
    entry_Time.insert(END, "1000")
    entry_Memo.insert(END, "16*1024")

    # 生成菜单栏
    Menu_Generate(administrator, text_Show)
    
    # 创建Scrollbar组件，该组件与Text的纵、横向滚动关联
    y_scrollbar_Show = Scrollbar(frame_Left, orient = VERTICAL,
                                 command = text_Show.yview)
    x_scrollbar_Show = Scrollbar(frame_Left, orient = HORIZONTAL,
                                 command = text_Show.xview)

    # 组件管理
    frame_Left.pack(side = 'left', fill = BOTH, expand = YES)
    y_scrollbar_Show.pack(side = 'right', fill = Y, expand = NO)
    x_scrollbar_Show.pack(side = 'bottom', fill = X, expand = NO)
    text_Show.pack(side = 'left', fill = BOTH, expand = YES)
    
    frame_Middle.pack(side = 'left',fill = BOTH, expand = YES)

    frame_Right.pack(side = 'left', fill = BOTH, expand = YES)
    lable_Timelimit.grid(row = 0, column = 0, sticky = N + E + S + W)
    entry_Time.grid(row = 0, column = 1, sticky = N + E + S + W)
    lable_Memolimit.grid(row = 1, column = 0, sticky = N + E + S + W)
    entry_Memo.grid(row = 1, column = 1, sticky = N + E + S + W)

    # 事件绑定
    entry_Time.bind("<Return>", lambda event:TimeChange())
    entry_Memo.bind("<Return>", lambda event:MemoChange())

    

    # 滚动条设置
    text_Show.configure(yscrollcommand = y_scrollbar_Show.set)
    text_Show.configure(xscrollcommand = x_scrollbar_Show.set)

    # 获得输入焦点
    text_Show.focus_set()

    
    administrator.mainloop()
    # 设置题目、答案、时间限制、空间限制、查看提交的代码


#====================================================================================
# 生成用户界面
def StudentMenu():
    
    studentmenu = Tk()
    studentmenu.iconbitmap("./items/ICO.ico")
    studentmenu.title("Online Judge(version-0.1) User")
    center_window(studentmenu, studentmenu_width, studentmenu_height)
    studentmenu.resizable(1, 1)

    # Frame
    frame_Left = Frame(studentmenu,bg = '#FAEDD2')
    frame_Middle = Frame(studentmenu,bg = 'white')
    frame_Right = Frame(studentmenu,bg = '#FAEDD2')


    global text_Code
    # 代码输入框
    text_Code = Text(frame_Left, width = code_width, height = code_height,
                     undo = True, maxundo = 20, bg = '#FAEDD2',
                     font = ('Arial 14 normal'))
    
    # global text_Question
    # 题目显示框
    text_Question = Text(frame_Right, width = code_width, height = code_height,
                     undo = True, maxundo = 20, bg = '#FAEDD2',
                     font = ('Arial 14 normal'))

    #题号选择按钮（小窗口max = 15，大窗口max = 20）
    button_QA = Button(frame_Right, text = 'A', bg = 'white',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 2, height = 2, relief = 'flat',
                          justify = CENTER, command = lambda:Questions_In(text_Question, "A.qst"))
    button_QB = Button(frame_Right, text = 'B', bg = 'white',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 2, height = 2, relief = 'flat',
                          justify = CENTER, command = lambda:Questions_In(text_Question, "B.qst"))
    button_QC = Button(frame_Right, text = 'C', bg = 'white',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 2, height = 2, relief = 'flat',
                          justify = CENTER, command = lambda:Questions_In(text_Question, "C.qst"))
    button_QD = Button(frame_Right, text = 'D', bg = 'white',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 2, height = 2, relief = 'flat',
                          justify = CENTER, command = lambda:Questions_In(text_Question, "D.qst"))
    button_QE = Button(frame_Right, text = 'E', bg = 'white',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 2, height = 2, relief = 'flat',
                          justify = CENTER, command = lambda:Questions_In(text_Question, "E.qst"))
    button_QF = Button(frame_Right, text = 'F', bg = 'white',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 2, height = 2, relief = 'flat',
                          justify = CENTER, command = lambda:Questions_In(text_Question, "F.qst"))
    button_QG = Button(frame_Right, text = 'G', bg = 'white',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 2, height = 2, relief = 'flat',
                          justify = CENTER, command = lambda:Questions_In(text_Question, "F.qst"))
    button_QH = Button(frame_Right, text = 'H', bg = 'white',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 2, height = 2, relief = 'flat',
                          justify = CENTER, command = lambda:Questions_In(text_Question, "F.qst"))
    button_QI = Button(frame_Right, text = 'I', bg = 'white',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 2, height = 2, relief = 'flat',
                          justify = CENTER, command = lambda:Questions_In(text_Question, "F.qst"))
    button_QJ = Button(frame_Right, text = 'J', bg = 'white',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 2, height = 2, relief = 'flat',
                          justify = CENTER, command = lambda:Questions_In(text_Question, "F.qst"))
    button_QK = Button(frame_Right, text = 'K', bg = 'white',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 2, height = 2, relief = 'flat',
                          justify = CENTER, command = lambda:Questions_In(text_Question, "F.qst"))
    button_QL = Button(frame_Right, text = 'L', bg = 'white',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 2, height = 2, relief = 'flat',
                          justify = CENTER, command = lambda:Questions_In(text_Question, "F.qst"))
    button_QM = Button(frame_Right, text = 'M', bg = 'white',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 2, height = 2, relief = 'flat',
                          justify = CENTER, command = lambda:Questions_In(text_Question, "F.qst"))
    button_QN = Button(frame_Right, text = 'N', bg = 'white',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 2, height = 2, relief = 'flat',
                          justify = CENTER, command = lambda:Questions_In(text_Question, "F.qst"))
    button_QO = Button(frame_Right, text = 'O', bg = 'white',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 2, height = 2, relief = 'flat',
                          justify = CENTER, command = lambda:Questions_In(text_Question, "F.qst"))
    # 组件元组
    button_Q_tuple = (button_QA, button_QB, button_QC, button_QD, button_QE,
                      button_QF, button_QG, button_QH, button_QI, button_QJ,
                      button_QK, button_QL, button_QM, button_QN, button_QO)

    # 读入当天题目
    # text_Question.bind("<Button-1>", lambda x:Questions_In(text_Question))
    global testpoint
    global question_n
    question_n, testpoint = Questions_In(text_Question)


    # 生成菜单栏
    Menu_Generate(studentmenu, text_Code)

    # 提交按钮
    button_Submit = Button(frame_Middle, text = 'Submit', bg = '#60A0B3',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 8, height = 2, relief = 'flat',
                          justify = CENTER, command = lambda:Submit(question_n, testpoint))
    
    # 创建Scrollbar组件，该组件与text_Code的纵、横向滚动关联
    y_scrollbar_Code = Scrollbar(frame_Left, orient = VERTICAL,
                                 command = text_Code.yview)
    x_scrollbar_Code = Scrollbar(frame_Left,  orient = HORIZONTAL,
                                 command = text_Code.xview)
    # 创建Scrollbar组件，该组件与text_Question的纵、横向滚动关联
    y_scrollbar_Question = Scrollbar(frame_Right, orient = VERTICAL,
                                 command = text_Question.yview)
    x_scrollbar_Question = Scrollbar(frame_Right, orient = HORIZONTAL,
                                 command = text_Question.xview)

    

    # 组件管理
    frame_Left.pack(side = 'left', fill = BOTH, expand = YES)
    y_scrollbar_Code.pack(side = 'right', fill = Y, expand = NO)
    x_scrollbar_Code.pack(side = 'bottom', fill = X, expand = NO)
    text_Code.pack(side = 'left', fill = BOTH, expand = YES)
    
    frame_Middle.pack(side = 'left',fill = BOTH, expand = YES)
    button_Submit.pack(side = 'bottom', pady = 50)
    

    frame_Right.pack(side = 'left', fill = BOTH, expand = YES)
    y_scrollbar_Question.pack(side = 'left', fill = Y, expand = NO)
    x_scrollbar_Question.pack(side = 'bottom', fill = X, expand = NO)
    text_Question.pack(side = 'right', fill = BOTH, expand = YES)
    
    # 滚动条设置
    text_Code.configure(yscrollcommand = y_scrollbar_Code.set)
    text_Code.configure(xscrollcommand = x_scrollbar_Code.set)

    text_Question.configure(yscrollcommand = y_scrollbar_Question.set)
    text_Question.configure(xscrollcommand = x_scrollbar_Question.set)

    # 选题按钮布局
    for i in range(question_n):
        button_Q_tuple[i].pack(side = 'top')

    text_Code.focus_set()

    studentmenu.mainloop()
    # 代码框，清空按钮，选择语言下拉栏，评测区，显示评测记录


#=================================================================================
# 登入窗口
def Main():
    # root为登入界面，也是程序的起点。
    # root界面窗口大小为1120x630，也就是16：9，窗口大小可变，显示在屏幕正中央
    # root界面拥有图片背景，ID & Pwd 输入框，登入及退出按钮
    # 下一界面为admin界面或student界面
    global root
    root = Tk()
    root.iconbitmap("./items/ICO.ico")
    root.title("Online Judge(version-0.1)")
    center_window(root, root_width, root_height)
    root.resizable(1, 1)

    # 账户与密码
    global entry_Name
    global entry_Pwd

    # canvas_Background --> bkg_Frame===================================
    bkg_Frame = Frame(root)
    bkg_Frame.pack(fill = BOTH, expand = YES)
    
    canvas_Background = Canvas(bkg_Frame, highlightthickness = 0)
    image = Image.open("./items/background.png")
    im = ImageTk.PhotoImage(image)
    canvas_Background.create_image(900,540,image = im)
    canvas_Background.pack(fill = BOTH, expand = YES)
    #===================================================================

    # canvas1 --> canvas_Background======================================
    canvas1 = Canvas(canvas_Background, highlightthickness = 0, bg = 'white')
    canvas11 = Canvas(canvas1, highlightthickness = 0, bg = 'white')
    canvas12 = Canvas(canvas1, highlightthickness = 0, bg = 'white')
    canvas1.pack(side = 'top', expand = 'yes')
    canvas11.pack()
    canvas12.pack()

    # 标题和标签
    label_Title = Label(canvas11, text = "Decentralization Online Judge\nVersion-0.1", bg = 'white',
                       font = ('Arial 14 bold'),fg = '#256D69',
                       width = 50, height = 2, justify = CENTER)
    
    label_Name = Label(canvas12, text = "ID：", bg = 'white',
                       font = ('Arial 13 bold'),
                       width = 10, height = 2, justify = CENTER)
    
    label_Pwd = Label(canvas12, text = "Password：", bg = 'white',
                      font = ('Arial 13 bold'),
                      width = 10, height = 2, justify = CENTER)

    
    # 单行输入框
    var_Name=StringVar()
    entry_Name=Entry(canvas12, width = 20, textvariable = var_Name)
    var_Pwd=StringVar()
    entry_Pwd=Entry(canvas12, width = 20, textvariable=var_Pwd, show = '*')

    # 登入与退出按钮
    button_Login = Button(canvas12,text = 'Login', bg = 'white',
                          font = ('Arial 13 bold'), fg = '#011640',
                          width = 6, height = 1, relief = 'flat',
                          justify=CENTER, command = Login)
    
    button_Concel = Button(canvas12, text = 'Concel', bg = 'white',
                           font = ('Arial 13 bold'), fg = '#011640',
                           width = 6, height = 1, relief = 'flat',
                          justify=CENTER, command = lambda:QuitMainWindow(root))

    root.bind("<Return>", lambda x:Login())
    root.bind("<Escape>", lambda x:QuitMainWindow(root))
    
    
    # 规划组件
    label_Title.pack()
    label_Name.grid(row = 0, column = 0)
    label_Pwd.grid(row = 1, column = 0)
    entry_Name.grid(row = 0, column = 1)
    entry_Pwd.grid(row = 1, column = 1)
    button_Login.grid(row = 2, column = 0)
    button_Concel.grid(row = 2, column = 1, columnspan = 3)

    entry_Name.focus_set()
    
    root.mainloop()
    

if __name__ == "__main__":
    Main()
