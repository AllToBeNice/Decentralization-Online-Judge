import urllib 
import urllib2 
import requests
print "downloading with urllib" 
url = 'https://bt.byr.cn/download.php?id=285482'
print "downloading with urllib"
urllib.urlretrieve(url, "demo.zip")
