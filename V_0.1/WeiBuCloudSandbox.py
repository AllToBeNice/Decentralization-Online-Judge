import os
import time
import requests

global key

# API密钥，需申请
key = ''


# 提交文件
def Upload(filedir, filename):
    url = 'https://s.threatbook.cn/api/v2/file/upload';
    fields = {
        'apikey': key,
        'sandbox_type': 'win7_sp1_enx64_office2013',
        'run_time': 2
        }

    filepath = filedir + "/" + filename
    
    files = {
        'file' : (filename, open(filepath, 'rb'))
        }
    response = requests.post(url, data = fields, files = files)
    print(response.json())#
    return response.json()


# 获取静态分析&动态分析报告
def Report(SHA_256):
    url = 'https://s.threatbook.cn/api/v2/file/report'
    params = {
        'apikey': key,
        'sandbox_type': 'win7_sp1_enx86_office2013',
        'sha256': SHA_256
        }
    response = requests.get(url, params = params)
    print(response.json())#
    return response.json()


# 获取文件概要
def Summary(SHA_256):
    url = 'https://s.threatbook.cn/api/v2/file/report/summary'
    params = {
        'apikey': key,
        'sandbox_type': 'win7_sp1_enx86_office2013',
        'sha256': SHA_256
        }

    response = requests.get(url, params = params)
    print(response.json())#
    return response.json()


# 获取文件网络行为
def NetWork(SHA_256):
    url = 'https://s.threatbook.cn/api/v2/file/report/network'
    params = {
        'apikey': key,
        'sandbox_type': 'win7_sp1_enx86_office2013',
        'sha256': SHA_256
        }
    response = requests.get(url, params = params)
    print(response.json())#
    return response.json()


# 获取文件签名
def Signature(SHA_256):
    url = 'https://s.threatbook.cn/api/v2/file/report/signature'
    params = {
        'apikey': key,
        'sandbox_type': 'win7_sp1_enx86_office2013',
        'sha256': SHA_256
        }
    response = requests.get(url, params = params)
    print(response.json())#
    return response.json()


# 获取静态信息
def Static(SHA_256):
    url = 'https://s.threatbook.cn/api/v2/file/report/static'
    params = {
        'apikey': key,
        'sandbox_type': 'win7_sp1_enx86_office2013',
        'sha256': SHA_256
        }
    response = requests.get(url, params = params)
    print(response.json())#
    return response.json()


# 文件释放行为信息
def Dropped(SHA_256):
    url = 'https://s.threatbook.cn/api/v2/file/report/dropped'
    params = {
        'apikey': key,
        'sandbox_type': 'win7_sp1_enx86_office2013',
        'sha256': SHA_256
        }
    response = requests.get(url, params = params)
    print(response.json())#
    return response.json()


# 获取文件进程行为报告
def Pstree(SHA_256):
    url = 'https://s.threatbook.cn/api/v2/file/report/pstree'
    params = {
        'apikey': key,
        'sandbox_type': 'win7_sp1_enx86_office2013',
        'sha256': SHA_256
        }
    response = requests.get(url, params = params)
    print(response.json())#
    return response.json()


# 获取文件反病毒扫描引擎检测报告
def Multiengines(SHA_256):
    url = 'https://s.threatbook.cn/api/v3/file/report/multiengines'
    params = {
        'apikey': key,
        'sandbox_type': 'win7_sp1_enx86_office2013',
        'sha256': SHA_256
        }
    response = requests.get(url, params = params)
    print(response.json())#
    return response.json()


# 提交扫描网址
def UrlScan(Url):
    url = "https://s.threatbook.cn/api/v2/url/scan"
    data = {
        "apikey": key,
        "url": Url
        }
    response = requests.post(url, data = data)
    print(response.json())#
    return response.json()


def UrlReport(Url):
    url = "https://s.threatbook.cn/api/v2/url/report"
    params = {
        "apikey": key,
        "url": Url
        }
    response = requests.get(url, params = params)
    print(response.json())#
    return response.json()


if __name__ == '__main__':
    
    filepath = 'F:\\Python\\Project\\Homework\\Online_Judge_v_0.1\\V_0.1\\Test'
    filename = 'EraPrimeCalc.py'
    
    back = Upload(filepath, filename)

    Signature(back['sha256'])
    Pstree(back['sha256'])
    Static(back['sha256'])
    Summary(back['sha256'])
