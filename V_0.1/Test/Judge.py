#-*- encoding: utf-8 -*-
__author__ = 'QCF'

'''
OJ评测系统
V - 0.1

评测函数
'''



import os
def judge_result():
    '''对输出数据进行评测'''
    currect_result = os.path.join("./ans.out")
    user_result = os.path.join("./main.out")
    try:
        curr = open(currect_result).read().replace('\r','').rstrip()#删除\r,删除行末的空格和换行  
        print(curr)
        user = open(user_result).read().replace('\r','').rstrip()  #python2中使用file函数
        print(user)
    except:
        return False
    if curr == user:  #完全相同:AC
        return "Accepted"
    if curr.split() == user.split():  #除去空格,tab,换行相同:PE
        return "Presentation Error"
    if curr in user:  #输出多了
        return "Output Limit Exceed"  #超出输出限制:OLE
    return "Wrong Answer"  #其他:WA
 
if __name__ == '__main__':
    print(judge_result())
