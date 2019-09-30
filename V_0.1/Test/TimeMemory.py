#!\usr\bin\env python3
#-*- encoding: utf-8 -*-
__author__ = 'QCF'

'''
OJ评测系统
V - 0.1

Time & Memory函数
'''


import time
import subprocess
import psutil
 
 
dir_work = "./"
fin = open("./main.in", "r+")
fout = open("./main.out", "w+")
 
p_cmd = {  # 运行程序的命令,这里以C++、C语言为例
    "gcc": "./main",
    "g++": "./main",
    "python37": 'python37 -m main.py'
}
 
 
 
def time_mem(language):
    """
    执行程序获取执行时间与内存
    """
    time_limit = 1  #second 时间限制
    mem_limit = 128 * 1024 #kb 内存限制
    max_rss = 0   #记录最大内存
    problem_info = {} #时间单位ms 内存单位kb
    p = subprocess.Popen(p_cmd[language],shell=True,cwd=dir_work, stdin=fin, stdout=fout, stderr=subprocess.PIPE)  # cwd设置工作目录
    start = time.perf_counter()  #开始时间
    print("程序开始运行的时间是%s" % start)
    pid = p.pid
    glan = psutil.Process(pid) #监听控制进程
 
    while True:
        time_now = time.perf_counter() - start  # ??
        if psutil.pid_exists(pid) is False:   #运行错误
            problem_info['time'] = time_now*1000
            problem_info['memory'] = max_rss/1024.0
            problem_info['result'] = "Runtime Error"
            return problem_info
        m_infor = glan.memory_info() 
        print(m_infor)
        rss = m_infor[0] #获取程序占用内存空间 rss
        if p.poll() == 0:  #运行正常结束，跳出循环，继续判断
            end = time.perf_counter()
            break
        if max_rss < rss:
            max_rss = rss
            #print("max_rss=%s" % max_rss)  #debug
        if time_now > time_limit:  #时间超限
            problem_info['time'] = time_now*1000
            problem_info['memory'] = max_rss/1024.0
            problem_info['result'] = "Time Limit Exceeded"
            glan.terminate()
            return problem_info
        if max_rss > mem_limit: #内存超限
            problem_info['time'] = time_now*1000
            problem_info['memory'] = max_rss/1024.0
            problem_info['result'] = "Memery Limit Exceeded"
 
    problem_info['time'] = time_now*1000
    problem_info['memory'] = max_rss/1024.0
    problem_info['result'] = "next judge"
    return problem_info
 
 
if __name__ == "__main__":
    language = input("选择语言")  
    result = time_mem(language)
    print(result)
