#!/usr/bin/env python3
#-*- encoding: utf-8 -*-
__author__ = 'QCF'

'''
OJ评测系统
V - 0.1

Config.py配置文件，储存设置窗口居中显示函数、GUI界面大小、评测时空参数等。
'''

#================================================================================================================
# 设置窗口居中显示
##def get_screen_size(window):
##    return window.winfo_screenwidth(),window.winfo_screenheight()
##
##
##def get_window_size(window):
##    return window.winfo_reqwidth(),window.winfo_reqheight()


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '{}x{}+{}+{}'.format(width, height, (screenwidth - int(width))//2, (screenheight - int(height))//2)
    # print(size)
    root.geometry(size)


#================================================================================================================
global root

# 登入窗口(16:9)
root_width = '1120'
root_height = '630'
root_geo = root_width + 'x' + root_height

# QuitRoot窗口
quit_root_width = '400'
quit_root_height = '260'
quit_root_geo = quit_root_width + 'x' + quit_root_height

# QuitMainWindow窗口
quit_mainwindow_width = '400'
quit_mainwindow_height = '260'
quit_mainwindow_geo = quit_mainwindow_width + 'x' + quit_mainwindow_height

# 登入失败窗口
quit_login_fail_width = '400'
quit_login_fail_height = '260'
quit_login_fail_geo = quit_login_fail_width + 'x' + quit_login_fail_height

# 登入成功窗口
quit_login_success_width = '400'
quit_login_success_height = '260'
quit_login_success_geo = quit_login_success_width + 'x' + quit_login_success_height

# 用户界面
studentmenu_width = '1120'
studentmenu_height = '630'
studentmenu_geo = studentmenu_width + 'x' + studentmenu_height

# 菜单栏
menu_width = '1'
menu_height = '1'

# 帮助窗口
apphelp_width = '500'
apphelp_height = '300'
help_content = 'This is the Decentralization Online Judge Version-0.1.\nThe TAB at the beginning of each line is eight spaces.\nPlease use fore spaces to instead.'

# 单词搜索窗口
varin_search_width = '200'
varin_search_height = '100'
varin_search_geo = varin_search_width + 'x' + varin_search_height

# 管理员界面
administrator_width = '1120'
administrator_height = '630'
administrator_geo = administrator_width + 'x' + administrator_height

# 代码输入框
code_width = 50
code_height = 27

# 提交框
submitmenu_width = '800'
submitmenu_height = '450'
submitmenu_geo = submitmenu_width + 'x' + submitmenu_height

# 评测显示框
resultshow_width = '800'
resultshow_height = '450'
resultshow_geo = resultshow_width + 'x' + resultshow_height

# 评测数据
# 单位：ms
time_limit = 1000
# 单位：kb
memo_limit = 16*1024
