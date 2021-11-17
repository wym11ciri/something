import requests

response = requests.get(url='https://www.baidu.com/')
response.encoding = 'utf-8'
print(response)  # <Response [200]>
# 返回响应状态码
print(response.status_code)  # 200
# 返回响应文本
# print(response.text)
print(type(response.text))  # <class 'str'>
#将爬取的内容写入xxx.html文件
with open('baidu.html', 'w', encoding='utf-8') as f:
    f.write(response.text)