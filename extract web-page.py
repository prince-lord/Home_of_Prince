# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 08:57:14 2022

@author: charles
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
driver = webdriver.PhantomJS(executable_path= '/phantomjs-2.1.1-windows/bin/phantomjs')
driver.get("https://tw.stock.yahoo.com/quote/2330/revenue")
page = driver.page_source
#print(page)
response = requests.get('https://tw.stock.yahoo.com/quote/2330/revenue').text
#print (response.status_code)
#print (response.content)

page = urlopen('https://tw.stock.yahoo.com/quote/2330/revenue')
html_bytes = page.read()
html = html_bytes.decode("utf-8")
#print(html)
data = 'https://tw.stock.yahoo.com/quote/2330/revenue'
response = requests.get(data)
response.encoding = 'utf8'
soup = BeautifulSoup(response.text,"html.parser")
#print(soup.prettify())    #輸出排版後的HTML內容
title_YYMM = soup.find_all("span", class_="Pos(a) W(100%) B(10px)") 
title_YYMM = str(title_YYMM)
title_YYMM = title_YYMM.split(">",1)
title_YYMM = str(title_YYMM[1])
title_YYMM = title_YYMM.split("<",1)
title_YYMM = str(title_YYMM[0])
#print(title_YYMM)
title_Rev_thisM = soup.find_all("li", class_="Jc(c) D(ib) Miw(100px) Fxg(1) Fxs(0) Fxb(100px) Ta(end) Mend(0)") 
title_Rev_thisM = str(title_Rev_thisM)
title_Rev_thisM = title_Rev_thisM.split("</li>")
#print(title_Rev_thisM)
print(len(title_Rev_thisM))
for num in range(len(title_Rev_thisM)):  
    if "Mend(0)" in title_Rev_thisM[num]:
      correct_str = title_Rev_thisM[num].split("Mend(0)",1)
      title_Rev_thisM[num] = str(correct_str[1])
#    else:
#      correct_str = title_Rev_thisM[num]    
#    print(correct_str)
#   title_Rev_thisM[num] = str(correct_str[1])
    print(num,"- ",title_Rev_thisM[num])

num = 1
while num < 3:
    num = num + 1
    title_Rev_thisM = title_YYMM.split(">",1)
    pass

title_Rev_thisM = title_YYMM.split(">",1)
title_Rev_thisM = str(title_Rev_thisM[1])
title_Rev_thisM = title_Rev_thisM.split("<",1)
title_Rev_thisM = str(title_Rev_thisM[0])
print(title_Rev_thisM)


# 使用Chrome costomize config =>
options = Options()
options.add_argument(r"user-data-dir=C:\\Users\\charles\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 6")
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.google.co.in")
# <=使用Chrome costomize config 
from selenium.webdriver.common.keys import Keys
#driver = webdriver.Chrome()

actionchains = ActionChains(driver)

driver.get('https://sukebei.nyaa.si/user/ofkkyu')