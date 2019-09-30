#!\usr\bin\env python3
#-*- encoding: utf-8 -*-
__author__ = 'QCF'

'''
OJ评测系统
V - 0.1

评测函数
支持python2、python3、C
（等我找到g++路径就能够支持C++了）
'''

import time
import subprocess
import psutil
import os, signal
import sys

import Config

import WeiBuCloudSandbox as yunsandbox

# 相对路径
dir_work = "./"


# Compile
#======================================================================================================================================
def Compile(language, filepath, filename):
    Q_Name = filename.split('.')[0]
    # 编译命令
    build_cmd = {
        "c": "gcc "+ filepath + filename + ' '+ "-o " + filepath + Q_Name + ' ' + "-Wall -lm -O2 -std=c99 --static -DONLINE_JUDGE",
        "g++": "g++ "+ filepath + filename + ' ' + "-O2 -Wall -lm --static -DONLINE_JUDGE -o " + Q_Name,
        "java": "javac " + filepath + filename,
        "ruby": "ruby -c " + filepath + filename,
        "perl": "perl -c " + filepath + filename,
        "pascal": 'fpc ' + filepath + filename + ' ' + '-O2 -Co -Ct -Ci',
        "go": '/opt/golang/bin/go build -ldflags "-s -w"  ' + filepath + filename,
        "lua": "luac -o " + filepath + Q_Name + ' ' + filename,
        "python2": "python2 -m py_compile " + filepath + filename,
        "python37": "python37 -m py_compile " + filepath + filename,
        "python3": "python3 -m py_compile " + filepath + filename,
        "haskell": "ghc -o " + filepath + Q_Name + ' ' + filename,
    }

    p = subprocess.Popen(build_cmd[language],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # 获取编译错误信息
    out,err = p.communicate()
    # 返回值为0,编译成功
    if p.returncode == 0:
        return True
    
    print("[*]Compile:{}".format(err,out))#
    
    return False

'''
#======================================================================================================================================
# cmd执行Python脚本，获取返回值
# 执行时间过长，舍弃。
def ExecCmd(commands):
    fin = open("./main.in", "r+")
    fout = open("./main.out", "w+")
    p = subprocess.Popen(commands,stdin=fin, stdout=fout, stderr=subprocess.PIPE, start_new_session=True)
    return p
'''


#======================================================================================================================================
# 检测时间
def Time(language, filepath, filename, testname):
    
    # 对应题目测试点文件夹名字
    Q_Name = filename.split('.')[0]
    # 测试点文件路径
    testpath = filepath + Q_Name + '/' + testname
    # 输出文件路径
    codepath = filepath + Q_Name + '/'
    
    # shell命令方式打开
    '''
    p_cmd = {  
    "c": filepath + Q_Name + ".exe",
    "g++": filepath + Q_Name + ".exe",
    "python2": "python2 " + filepath + filename,
    "python3": "python3 " + filepath + filename,
    "python37": "python37 " + filepath + filename
    }
    '''
    
    p_cmd = {  
    "c": [filepath + Q_Name + ".exe"],
    "g++": [filepath + Q_Name + ".exe"],
    "python2": ["python2", filepath + filename],
    "python3": ["python3", filepath + filename],
    "python37": ["python37", filepath + filename]
    }
    
    Problem_Info = {"time(ms)":None, "info":None}
    
    fin = open(testpath + ".in", "r+")
    fout = open(codepath + "main.out", "w+")
    
    print("[*]filepath + filename:{}{}".format(filepath, filename))###
    print("[*]fin:{},fout:{}".format(fin,fout))###
    
    start_time = time.perf_counter() * 1000
    p = subprocess.Popen(p_cmd[language],stdin=fin, stdout=fout, stderr=subprocess.PIPE, start_new_session=True)
    # p = subprocess.Popen(p_cmd[language],shell=True, stdin=fin, stdout=fout, stderr=subprocess.PIPE, start_new_session=True)
    print("[*]程序开始于{}".format(start_time))###
    while True:
        time_now = time.perf_counter() * 1000
        print("[!] {}".format(time_now))###
        if p.poll() is not None and p.poll() != 2:
            end_time = time.perf_counter() * 1000
            Problem_Info["time(ms)"] = end_time - start_time
            Problem_Info["info"] = "OK"
            break
        elif p.poll() is None:
            print("[!]time_now - start_time = {}".format(time_now - start_time))
            if time_now - start_time >= Config.time_limit:
                # 非shell方式结束进程
                p.kill()
                # Windows下结束shell创建的子进程
                # subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid = p.pid))
                Problem_Info["time(ms)"] = "Wrong"
                Problem_Info["info"] = "Time Limit Exceeded"
                print("[*]Time:{}".format(Problem_Info))###
                return Problem_Info
        else:
            print("[*]p.poll()={}".format(p.poll()))###
            Problem_Info["time(ms)"] = "Wrong(2)"
            Problem_Info["info"] = "Runtime Error"
            print("[*]Time:{}".format(Problem_Info))###
            return Problem_Info

    # 程序正常结束
    print("[*]Time:{}".format(Problem_Info))###
    return Problem_Info


#===================================================================================================================
# 检测最大内存使用
def Memory(language, filepath, filename, testname):
    # 对应题目测试点文件夹名字
    Q_Name = filename.split('.')[0]
    # 测试点文件路径
    testpath = filepath + Q_Name + '/' + testname
    # 输出文件路径
    codepath = filepath + Q_Name + '/'
    # shell命令
    '''
    p_cmd = {  
    "c": filepath + filename,
    "g++": filepath + filename,
    "python2": "python2 " + filepath + filename,
    "python3": "python3 " + filepath + filename,
    "python37": "python37 " + filepath + filename
    }
    '''
    p_cmd = {  
    "c": [filepath + Q_Name + ".exe"],
    "g++": [filepath + Q_Name + ".exe"],
    "python2": ["python2", filepath + filename],
    "python3": ["python3", filepath + filename],
    "python37": ["python37", filepath + filename]
    }
    
    
    # 记录最大内存
    max_rss = 0
    Problem_Info = {"memory(kb)":None, "info":None}
    fin = open(testpath + ".in", "r+")
    fout = open(codepath + "main.out", "w+")
    p = subprocess.Popen(p_cmd[language], stdin = fin, stdout = fout, stderr = subprocess.PIPE, start_new_session = True)
    # shell方式执行
    # p = subprocess.Popen(p_cmd[language],shell = True, stdin = fin, stdout = fout, stderr = subprocess.PIPE, start_new_session = True)
    pid = p.pid
    monitor = psutil.Process(pid) #监听控制进程
    
    while True:
        
        # 运行错误，RE
        if psutil.pid_exists(pid) is False:
            Problem_Info["memory(kb)"] = max_rss/1024.0
            #Problem_Info["info"] = "Accepted"
            Problem_Info["info"] = "Runtime Error"
            return Problem_Info
        
        m_infor = monitor.memory_info() 
        print("[*]monitor:{}".format(m_infor))###
        # 获取程序占用物理内存空间 rss
        rss = m_infor[0]

        # 运行正常，跳出循环.NJ
        if p.poll() == 0:
            p.kill()
            break
        if max_rss < rss:
            max_rss = rss
        
        # 内存超限，MLE
        if max_rss > Config.memo_limit*1024:
            Problem_Info["memory(kb)"] = max_rss/1024.0
            Problem_Info["info"] = "Memory Limit Exceeded"
            p.kill()
            return Problem_Info
 
    Problem_Info["memory(kb)"] = max_rss/1024.0
    Problem_Info["info"] = "Next Judge"
    print("[*]Problem_Info:{}".format(Problem_Info))###
    return Problem_Info


# Judge判断评测结果
#=================================================================================================
def JudgeResult(filepath, filename, testname):
    '''对输出数据进行评测'''
    # 对应题目测试点文件夹名字
    Q_Name = filename.split('.')[0]
    # 标准输出文件路径
    anspath = filepath + Q_Name + '/' + testname
    # 输出文件路径
    outpath = filepath + Q_Name + '/'
    
    currect_result = os.path.join(anspath + ".out")
    user_result = os.path.join(outpath + "main.out")
    try:
        curr = open(currect_result).read().replace('\r','').rstrip()#删除\r,删除行末的空格和换行  
        curr.rstrip('\n')
        print('[curr]',curr)###
        user = open(user_result).read().replace('\r','').rstrip()#python2中使用file函数
        user.rstrip('\n')
        print('[user]',user)###
    except:
        return False
    # 完全相同:AC
    if curr == user:
        return "Accepted"
    # 除去空格,tab,换行相同:PE
    if curr.split() == user.split():
        return "Presentation Error"
    # 超出输出限制:OLE
    if curr in user:
        return "Output Limit Exceeded"
    # 其他:WA
    return "Wrong Answer"


#=================================================================================================
# Judge()函数，检测安全后评测
# 传入Language、n，表示语言和测试点个数
def Judge(language, n, filepath, filename):
    # 全部测试点返回值
    Back_Info = dict(zip([i for i in range(1, n+1)], [{"Time(ms)":None, "Memory(kb)":None, "Info":None} for i in range(n)]))
    # 遍历测试点
    for dot in range(1, n+1):
        
        # [1] Compile
        C_temp = Compile(language, filepath, filename)
        if C_temp == False:
            Back_Info[dot]["Info"] = "Compile Error"
            continue
        else:
            
            # [2] Time
            T_temp = Time(language, filepath, filename, str(dot))
            if T_temp["info"] != "OK":
                Back_Info[dot]["Time(ms)"] = T_temp["time(ms)"]
                Back_Info[dot]["Info"] = "Time Limit Exceeded"
                continue
            else:
                Back_Info[dot]["Time(ms)"] = T_temp["time(ms)"]
                
                # [3] Memory
                M_temp = Memory(language, filepath, filename, str(dot))
                if M_temp["info"] != "Next Judge":
                    Back_Info[dot]["Memory(kb)"] = M_temp["memory(kb)"]
                    Back_Info[dot]["Info"] = M_temp["info"]
                    continue
                else:
                    Back_Info[dot]["Memory(kb)"] = M_temp["memory(kb)"]

                    # [3] JudgeResult
                    J_temp = JudgeResult(filepath, filename, str(dot))
                    Back_Info[dot]["Info"] = J_temp

    return Back_Info
    # 返回字典Back_Info：{ n 个测试点：{时间：—，内存：—，程序运行情况：—}}
    

#============================================================================================
# 检测文件是否安全
def Security(filepath, filename):

    Security_Info = {}

    # 测试用
    # filepath = './Answers/20190608/'
    # filename = 'A.py'

    # 上传main.py文件
    Up_backinfo = yunsandbox.Upload(filepath, filename)
    # 上传出错
    if Up_backinfo["response_code"] == -1:
        Security_Info["re_code"] = -1
        Security_Info["err_msg"] = Up_backinfo["msg"]
        Security_Info["threat_level"] = "Unknown"
        return Security_Info
    # 上传成功
    else:
        # 根据文件sha256编码获取Summay报告，检测threat_level项
        SHA_256 = Up_backinfo['sha256']
        # 循环查询报告，依次检查查询和报告返回码，根据网络情况约为20s
        while True:
            # 这里使用概要
            Sum_backinfo = yunsandbox.Summary(SHA_256)
            # 查询出错，即返回码为-1
            if Sum_backinfo["response_code"] == -1:
                # 报告未生成，静默3s继续查询
                if Sum_backinfo["msg"] == "NO_REPORT_FOUND" or Sum_backinfo["msg"] == "NO_MULTI_ENGINES_DATA" or Sum_backinfo["msg"] == "ESPROXY SEARCH ERROR":
                    time.sleep(3)
                    continue
                # 报告生成出错
                else:
                    Security_Info["re_code"] = -1
                    Security_Info["err_msg"] = Sum_backinfo["msg"]
                    Security_Info["threat_level"] = "Unknown"
                    return Security_Info
            # 查询成功，即返回码为1
            elif Sum_backinfo["response_code"] == 1:
                # 报告生成中，静默3s继续查询
                if Sum_backinfo["msg"] == "IN_PROGRESS":
                    time.sleep(3)
                    continue
                # 未知错误
                else:
                    Security_Info["re_code"] = -1
                    Security_Info["err_msg"] = Sum_backinfo["msg"]
                    Security_Info["threat_level"] = "Unknown"
                    return Security_Info
            # 获取威胁等级
            else:
                Security_Info["re_code"] = 0
                Security_Info["err_msg"] = "OK"
                Security_Info["threat_level"] =  Sum_backinfo["data"]["summary"]["threat_level"]
                if Security_Info["threat_level"] in ["malicious", "suspicious"]:
                    return Security_Info
                else:
                    return Security_Info
    # 返回字典Security_Info：{re_code: —，err_msg: —，threat_level: —}


#========================================================================================================
# OJ()函数
def OJ(language, n, filepath, filename):
    Out_Info = {"response":None, "msg":None, "threat_level":None,
                "result":None, "back_info":None}
    # 判断安全等级
    security_level = Security(filepath, filename)

    # [1] 返回错误
    if security_level["re_code"] == -1:
    #if security_level["re_code"] == 0:###
        Out_Info["response"] = -1
        Out_Info["msg"] = security_level["err_msg"]
        Out_Info["threat_level"] = security_level["threat_level"]
        Out_Info["result"] = "Runing Wrong"
        return Out_Info
    else:
        Out_Info["response"] = 0
        Out_Info["msg"] = security_level["err_msg"]
        Out_Info["threat_level"] = security_level["threat_level"]

        # [2] 威胁等级高于"clean"
        if Out_Info["threat_level"] == "malicious" or Out_Info["threat_level"] == "suspicious": 
        #if Out_Info["threat_level"] == "clean":###
            print(Out_Info["threat_level"], 11)
            Out_Info["result"] = "Runing Dangerous!"
            return Out_Info
        else:

            # [3] 威胁等级为"clean"
            Back_Info = Judge(language, n, filepath, filename)
            Out_Info["back_info"] = Back_Info

            # [4] 判断结果
            temp = True
            for i in range(1, n+1):
                if Out_Info["back_info"][i]["Info"] == "Accepted":
                    temp = temp & True
                    continue
                else:
                    temp = temp & False
                    Out_Info["result"] = Out_Info["back_info"][i]["Info"]
                    break
            if temp == True:
                Out_Info["result"] = "Accepted"
            return Out_Info


if __name__ == '__main__':
    # 测试用
    
    print(OJ("python37", 1, './Answers/20190614/', 'A.c'))

    
    a = Security('./Answers/20190614', 'E.py')
    print(a)
    
    language = input("输入要进行编译的language：")
    print('[1]',Compile(language, './Answers/20190614/', 'E.py'))
    
    text1 = Time(language, './Answers/20190614/', 'E.py', '1')
    print('[2]',text1)
    
    text2 = Memory(language, './Answers/20190614/', 'E.py', '1')
    print("[3]", text2)
    
    time.sleep(0.6)
    print('[3]',JudgeResult('./Answers/20190614/', 'E.py', '1'))

