# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 21:15:59 2022

@author: charles
"""
import time
import keyboard
import win32clipboard            # clip board
import pyautogui
import requests

import os
import os.path
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 使用Chrome costomize config =>
options = Options()
options.add_argument(r"user-data-dir=C:\\Users\\charles\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 6")
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.google.co.in")
# <=使用Chrome costomize config 
from selenium.webdriver.common.keys import Keys
#driver = webdriver.Chrome()

actionchains = ActionChains(driver)

#element = driver.find_element_by_id("displayModal") 
# print complete element 
#print(element)

driver.get('https://www.javlibrary.com/tw/vl_newrelease.php?list&mode=&page=7')
#driver.get('http://ben.baiwanwan.com/2048/thread.php?fid-5-page-1.html')
#click agree button
#button = driver.find_element_by_link_text("我同意")
#button.click()

#driver.find_elements_by_css_selector('[class="largebutton btnAdultAgree"]')[0].click() 
#keyboard.write('c:\')
#讀取抓取的討論區標題
#file_object = open('c:/tmp/title.txt','r',encoding='utf-8')

#lines = file_object.read()
#lines = file_object.readline()
#lines = file_object.readlines()
#for line in lines:
#  print("line=",lines)
#print("line=",lines)

folder = "c:\\tmp\\8888"
os.chdir("c:\\tmp")
print("current dir is: %s" % (os.getcwd()))

if os.path.isdir(folder):
   print("Exists")
else:
   print("Doesn't exists")
   os.mkdir(folder)    
   
with open('c:/tmp/title.txt','r',encoding='utf-8') as infile:
    while True:
        line = infile.readline()     # 一次讀一行資料
        line = line.split('\n', 1)[0]  #清掉換行符號
        if not line:                 # 所有資料讀取完畢
            break
#        print(line) 
#        print(line, end='')          # end='': 不要自動加斷行
        
        l_text = line
        o_name = l_text
        n_name = '['+ o_name + ']'
#        element = driver.find_element_by_link_text(l_text) 
        element = driver.find_element_by_partial_link_text(l_text) 
          # 按滑鼠右鍵,取得連結
        actionchains = ActionChains(driver)
        actionchains.context_click(element).perform()
        time.sleep(1)
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.typewrite(['enter'])
        # copy from clipboard
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()        
        print (data)
        driver.get(data)     #開網頁
        driver.maximize_window()
#        l_text = '.torrent'
        path1 = 'c:\\tmp\\8888\\'
        #擷取網頁內容 =>
        response = requests.get(data)
        response.encoding = 'utf8'
        soup = BeautifulSoup(response.text,"html.parser")
        print(soup.prettify())    #輸出排版後的HTML內容
#標題擷取        
        #result = soup.find_all("h3", class = "post-title text")
        result = soup.find_all("a", rel="bookmark")
#        result = soup.find_all("a", href="/tw/?v=javmefze7y")
#        print(result)
        new_result = str(result)
#        new_result1 = new_result.split("bookmark",1)   
        new_result1 = new_result.split(o_name,1)        
        new_result1 = str(new_result1[1])
        new_result2 = new_result1.split("<",1)
#        print(new_result2)   ####
        new_result2 = str(new_result2[0]) 
        print(new_result2)
#        new_result3 = new_result2.split(">",1)   
#        new_result2 = str(new_result3[1]) 
        print(result)
        print(new_result2)               #擷取網頁內容<=
        for char in new_result2:
            if char in "?!/;:*":
              new_result2 = new_result2.replace(char,'')  
#        print(new_result2)
#        new_result2 = new_result2.replace(o_name , n_name)
        new_result2 = n_name + new_result2        
        print(new_result2)       #<=title
#發行商處理        
        supplier = soup.find_all("span", class_="label")        
        supplier = str(supplier)
        print(supplier)
        supplier1 = supplier.split("tag",1)
        supplier = str(supplier1[1])
        supplier1 = supplier.split(">",1)
        supplier = str(supplier1[1])
        supplier1 = supplier.split("<",1)
        supplier = str(supplier1[0])
        supplier = "(" + supplier + ")"
        for char in supplier:
            if char in "?!/;:*":
              supplier = supplier.replace(char,'') 
#        print(supplier)
#演員處理   
#        cast = soup.find_all("a", rel="tag")
#        cast = str(cast)
#        cast1 = cast[-10:]  
#        print(cast)
#        print(cast1)
                      # DOS command
        new_result2 = supplier + new_result2  
        new_result2 = new_result2.lstrip()   
        new_result2 = new_result2.strip()
        print(new_result2)    
        folder = new_result2
        folder.encode('utf8')
        command = '\\tmp\\8888\\' + folder
        print(command)
#command = str(command.decoding('utf-8')
        os.mkdir(command)              #<= DOS command
#        output = stream.read()
        #output
#        path = path1  + new_result2 + '\\'     #儲存路徑 #
#        print(path)
#        element = driver.find_element_by_partial_link_text(l_text) 
#        actionchains = ActionChains(driver)
#        actionchains.context_click(element).perform()
#        time.sleep(1)
#        pyautogui.press('down')
#        pyautogui.press('down')
#        pyautogui.press('down')
#        pyautogui.press('down')
#        pyautogui.typewrite(['enter']) 
#        time.sleep(9)
#        keyboard.press_and_release('home')
#        keyboard.write(path,delay = 0.1)       #存檔到指定路徑
#        keyboard.press_and_release('enter')   
#        print(line)          
        driver.back()              #回上一個page"
#l_text = line
infile.close()
