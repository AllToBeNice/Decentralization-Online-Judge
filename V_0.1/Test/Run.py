#!\usr\bin\env python3
#-*- encoding: utf-8 -*-
__author__ = 'QCF'

'''
OJ评测系统
V - 0.1

运行函数
'''


import time
import subprocess
dir_work = "./"
def compile(language):
    build_cmd = {
        "gcc": "gcc main.c -o main -Wall -lm -O2 -std=c99 --static -DONLINE_JUDGE",
        "g++": "g++ main.cpp -O2 -Wall -lm --static -DONLINE_JUDGE -o main",
        "java": "javac Main.java",
        "ruby": "ruby -c main.rb",
        "perl": "perl -c main.pl",
        "pascal": 'fpc main.pas -O2 -Co -Ct -Ci',
        "go": '/opt/golang/bin/go build -ldflags "-s -w"  main.go',
        "lua": 'luac -o main main.lua',
        "python2": 'python2 -m py_compile main.py',
        "python37": 'python37 -m py_compile main.py',
        "python3": 'python3 -m py_compile main.py',
        "haskell": "ghc -o main main.hs",
    }
    p = subprocess.Popen(build_cmd[language],shell=True,cwd=dir_work,stdout=subprocess.PIPE,stderr=subprocess.PIPE) #cwd设置工作目录
    out,err = p.communicate()#获取编译错误信息
    if p.returncode == 0: #返回值为0,编译成功
        return True
    # update_compile_info(solution_id,err+out) #编译失败，更新题目编译错误信息
    print(err,out)
    return False


if __name__ == '__main__':
    language = input("输入要进行编译的language：")
    print(compile(language))
