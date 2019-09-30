import psutil
import subprocess
import os
L = []
commands = 'python37 -m memoTest1.py'

p = subprocess.Popen(commands,shell=True,cwd='./', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
pid = p.pid
glan = psutil.Process(pid)
while True:
  m_infor = glan.memory_info()
  '''
  with open('log.txt','w') as fw:
    fw.write(str(m_infor[0]))
    fw.write('\n')
    fw.close()
  '''
  print(m_infor[0]/1024)
  # print("内存占用：{}".format(b-a))
