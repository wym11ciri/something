# coding:utf-8
import requests
from lxml import etree
import urllib3
urllib3.disable_warnings()
url="http://jtzi7680ouhinbwk.mikecrm.com/r.php?t=4iyHrGY&s=2"
r=requests.get(url,verify=False)
print(r.text)
content=etree.HTML(r.content)
print(content)
print(content.xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/ul/li[1]/ul/li[1]/div[1]/p//text()"))
print(content.xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/ul/li[2]/ul/li[1]/div[1]/p//text()"))
