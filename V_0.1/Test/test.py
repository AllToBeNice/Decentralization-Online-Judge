#!\usr\bin\env python3
#-*- encoding: utf-8 -*-
__author__ = 'QCF'

from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.simpledialog import askstring, askinteger, askfloat

global teacher_acccounts
teacher_acccounts = {'admin1':{'Name':'admin1','Pwd':'123456'},
                     'admin2':{'Name':'admin2','Pwd':'654321'}}

global students_scores
students_scores = {'BZB':100,
                   'bzb':95,
                   'Bzb':80}

def add_name():
  temp_Name = askstring("提示", "请输入学生姓名")
  return temp_Name

def add_score():
  temp_Score = askinteger("提示", "请输入学生成绩", minvalue=0, maxvalue=100)
  return temp_Score

def AddScore():
    temp_Name = add_name()
    if temp_Name not in students_scores:
        temp_Score = add_score()
        students_scores[temp_Name] = temp_Score
    else:
        messagebox.showerror("提示","该学生已存在！")

def OutputScore():
    for scores in students_scores.items():
        print("姓名：{:<10s}成绩：{:<5d}".format(scores[0], scores[1]))


def MainMenu():
    branch = Tk()
    branch.title("学生管理系统登入界面")
    branch.geometry('300x500') # 设置窗口大小                     
    branch.resizable(0, 0) # 窗体在x,y方向上的可变性（True or False/1 or 0）

    button_AddScore = Button(branch, text = "添加成绩",
                             command = AddScore)
    
    button_OutputScore = Button(branch, text = "查看成绩",
                                command = OutputScore)
    
    button_Quit = Button(branch, text = "退出系统",
                         command = quit)

    button_AddScore.place(x = 94, y = 80)
    button_OutputScore.place(x = 94, y = 230) # 138x40
    button_Quit.place(x = 94, y = 380)


    

def Login():
    NameIn = entry_Name.get()
    PwdIn = entry_Pwd.get()
    if teacher_acccounts.get(NameIn) == None or PwdIn != teacher_acccounts[NameIn]['Pwd']:
        messagebox.showerror("登入失败", "用户名或密码错误！")
    else:
        messagebox.showinfo("登入成功", "欢迎您！教师" + NameIn)
        root.destroy()
        MainMenu()
    
def main():
    global root
    root = Tk()
    '''
    canvas = Canvas(root,  
        width = 300,      # 指定Canvas组件的宽度  
        height = 200,      # 指定Canvas组件的高度  
        bg = 'white')      # 指定Canvas组件的背景色  
    #im = Tkinter.PhotoImage(file='img.gif')     # 使用PhotoImage打开图片  
    image = Image.open("background.jpg")  
    im = ImageTk.PhotoImage(image)  
       
    canvas.create_image(300,50,image = im)
    canvas.pack()
    '''
    root.title("学生管理系统登入界面")
    root.geometry('300x200') # 设置窗口大小                     
    root.resizable(0, 0) # 窗体在x,y方向上的可变性（True or False/1 or 0）
    
    # Login
    label_Name = Label(root, text = "用户名：",
                       width = 6, justify=CENTER)
    label_Pwd = Label(root, text = "密码：",
                      width = 6, justify=CENTER)

    global entry_Name, entry_Pwd
    
    var_Name=StringVar()
    entry_Name=Entry(root, textvariable = var_Name)

    var_Pwd=StringVar()
    entry_Pwd=Entry(root, textvariable=var_Pwd, show = '*')

    button_Login = Button(root, text = "Login",
                          width = 6,
                          command = Login) # function Login
    button_Cancel = Button(root, text = "Cancel",
                           width = 6,
                           command = quit) # function quit
    
    label_Name.place(x = 50, y = 25)
    entry_Name.place(x = 100, y = 25)
    label_Pwd.place(x = 50, y = 75)
    entry_Pwd.place(x = 100, y = 75)
    button_Login.place(x = 75, y = 125)
    button_Cancel.place(x = 175, y = 125)
    root.mainloop()

if __name__ == "__main__":
    main()
