from selenium import webdriver
import time
import json

driver = webdriver.Chrome() #获取驱动对象
driver.get("http://jtzi7680ouhinbwk.mikecrm.com/r.php?t=4iyHrGY&s=2")
#time.sleep(10)
driver.implicitly_wait(1)
div = driver.find_element_by_tag_name('div')
#print(div.tag_name)
#a = driver.find_element_by_xpath('//div[@class="rm_dliItemInfo"]')

#a = driver.find_elements_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/ul/li')
#a.click() #
#aa = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/ul/li[1]/ul/li[1]/div[1]/p')
#print(aa.text)
#print(a)

#time.sleep(20)

#b = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/ul/li[2]/div[2]')
#b.click()
#bb = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/ul/li[2]/ul/li[1]/div[1]/p')
#print(bb.text)

i=1
#/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/ul/li[5]/div[2]
#/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/ul/li[6]/div[2]
#/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/ul/li[1]/div[2]
#/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/ul/li[1]/ul/li[1]/div[1]/p
#/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/ul/li[4]/ul/li[1]/div[1]/p

#/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/ul/li[1]/div[2]/span[2]
#/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/ul/li[2]/div[2]/span[2]
result = []
while i < 10:
    time.sleep(10)
    print(i)
    ii = str(i)
    c = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/ul/li[' + ii + ']/div[2]')
    c.click()
    one = {}
    print(c.text)
    one['time'] = c.text
    #
    time.sleep(10)
    bb = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/ul/li[' + ii + ']/ul/li[1]/div[1]/p')
    print(bb.text)
    one['content'] = bb.text
    result.append(one)
    i+=1

print(result)
with open('/Users/wym/Desktop/data.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(result, indent=2, ensure_ascii=False))

time.sleep(10)
driver.close