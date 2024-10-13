# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 17:43:16 2022

@author: charles
"""
# -*- coding: utf-8 -*-
import time
import keyboard
#import win32clipboard            # clip board
#import pyautogui

#import requests
import os
import os.path
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#import pyodbc
import pandas as pd
#from bs4 import BeautifulSoup
#from selenium.webdriver.common.keys import Keys

# 使用Chrome costomize config =>

options = Options()
options.add_argument(
    r"user-data-dir=C:\\Users\\charles\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 6")
#options.add_argument('--headless')
#driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.co.in")
# <=使用Chrome costomize config

#driver = webdriver.Chrome()

actionchains = ActionChains(driver)

#element = driver.find_element_by_id("displayModal") 
# print complete element 
#print(element)

#driver.get('https://sukebei.nyaa.si/user/ofkkyu?p=1')
driver.get('https://sukebei.nyaa.si/user/offkab')
#driver.get('http://cdn5.7n7c.xyz/2048/read.php?tid-1632792.html')
time.sleep(5)
#search_input = driver.find_element_by_xpath("//input[@class='form-control search-bar']") 
#attr = search_input.get_attribute("class")
#print("class attr:" , attr)
#search_input.send_keys("JUQ-266")
#search_button = driver.find_element_by_xpath("//div[@class='input-group-btn search-btn']") 
#search_button.click()

folder = "c:\\tmp\\9997"
os.chdir("c:\\tmp")
print("current dir is: %s" % (os.getcwd()))

if os.path.isdir(folder):
   print("Exists")
else:
   print("Doesn't exists")
   os.mkdir(folder) 
   
def find_prefix(spliter,long_str):    
    if spliter in long_str:
       new_long_str = long_str.split(spliter,1)
       new_long_str = str(new_long_str[1])   
    else:  
       new_long_str = ''        
    print('post arg1:',spliter)
    print('post arg2:',new_long_str) 
    long_str = new_long_str
    return long_str

with open('c:/tmp/title.txt','r',encoding='utf-8') as infile:   
    if __name__ == "__main__":    #要怎麼讓檔案在被引用時，不該執行的程式碼不被執行
      print("started....")
#      mssql_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
#      + 'sql.bsite.net\MSSQL2016' + ';DATABASE=' 
#      + 'princel_new' + '; UID=' + 'princel_new' +';PWD=' + '1qaz2wsx')  
#      print("connections established!")
#      SQL_QUERY = """
#SELECT * FROM  [princel_new].[dbo].[SUPPLIER_MAP];
#"""
#    cursor = mssql_conn.cursor()
#    cursor.execute(SQL_QUERY)
#    supp_records = cursor.fetchall()
    dataframe1 = pd.read_excel('c:/suppliers/SUPPLIER_MAP.xlsx',sheet_name='NAME')
    supp_records = dataframe1
    print(type(supp_records))
    print (supp_records)  
        
    while True:
        line = infile.readline()     # 一次讀一行資料
        line = line.split('\n', 1)[0]  #清調換行符號
        if not line:                 # 所有資料讀取完畢
            break
#        print(line) 
#        print(line, end='')          # end='': 不要自動加斷行
        l_sterm = line
        l_text =  line    #'+++[FHD]'
        l_name = str(line)        
        n_name = '['+ l_name + ']'
        print(n_name, l_text )
#關閉廣告
#         close_button = driver.find_element(By.XPATH , "//div[@class='exo_close']")
#         close_button = driver.find_element(By.id , ' ' )
#         close_button.click() 
#輸入字串      
#        search_input = driver.find_element_by_xpath("//input[@class='form-control search-bar']") 
        search_input = driver.find_element(By.XPATH , "//input[@class='form-control search-bar']") 
#        driver.find_element_by_xpath("//input[@class='form-control search-bar']").clear()
        driver.find_element(By.XPATH, "//input[@class='form-control search-bar']").clear()
        search_input.send_keys(l_sterm)
#        search_button = driver.find_element_by_xpath("//div[@class='input-group-btn search-btn']") 
        search_button = driver.find_element(By.XPATH , "//div[@class='input-group-btn search-btn']") 
        search_button.click()        
        response_text = driver.find_element(By.XPATH , "//div[@class='pagination-page-info']").text
        print('aa', response_text)
        if 'Displaying results 0-0 out of 0 results' in response_text:
         continue    
         
#輸入字串查詢<=
#CLICK 日期排序=>
#        sort_by_seeder = driver.find_element(By.XPATH , "//th[@class='hdr-seeders sorting text-center']")
#        #driver.find_element(By.LINK_TEXT , 'Date')
#        sort_by_seeder.click()
        
        sort_by_date = driver.find_element(By.XPATH , "//th[@class='hdr-date sorting_desc text-center']")
        #driver.find_element(By.LINK_TEXT , 'Date')
        sort_by_date.click()
#CLICK 日期排序<=

#        element = driver.find_element_by_link_text(l_text) 
        time.sleep(5)
        element = driver.find_element(By.PARTIAL_LINK_TEXT, l_text) 
        element.click() 
          # 按滑鼠右鍵,取得連結        
#        actionchains = ActionChains(driver)
#        actionchains.context_click(element).perform()
#        time.sleep(10)
#        pyautogui.press('down')
#        pyautogui.press('down')
#        pyautogui.press('down')
#        pyautogui.press('down')
#        pyautogui.press('down')
#        pyautogui.typewrite(['enter'])
        # copy from clipboard
#        win32clipboard.OpenClipboard()
#        data = win32clipboard.GetClipboardData()
#        win32clipboard.CloseClipboard()
#        print (data) 
#        try:
#            driver.get(data)     #開網頁
#        except:
#            print('retry')
#            time.sleep(1)
#            try:
#               driver.get(data)
#            except:
#               print('retry')
#               time.sleep(1)
#            continue
        driver.maximize_window()        
        l_text = 'Download Torrent'
        path1 = 'c:\\tmp\\9997\\'
        #擷取網頁內容 =>
#        response = requests.get(data)
#        response.encoding = 'utf8'
#        soup = BeautifulSoup(response.text,"html.parser")
#print(soup.prettify())    #輸出排版後的HTML內容
#        result = soup.find_all("h3", id ="panel-title")        
        detail = driver.find_element(By.ID , 'torrent-description').get_attribute("textContent")        
        result = driver.find_element(By.CLASS_NAME , 'panel-title').get_attribute("textContent")
#        print(result)
#        print(detail)
#=> torrent title        
        new_result = str(result)        
        print('new_result:', new_result)
        if '[FHD]' not in new_result:
           continue  
            
        new_result1 = new_result.split("]",1)
        print('new_result1:', new_result1)
        new_result1 = str(new_result1[1])
#        new_result2 = new_result1.split("<",1)
#        new_result2 = str(new_result2[0])        
        print(result)
        print(new_result1)               #擷取網頁內容<=
#        for char in new_result1:
#            if char in "?!/;:":
#              new_result1 = new_result1.replace(char,'')  
        new_result1 = new_result1.replace(l_name , n_name)
        new_result1 = new_result1.lstrip()   
        new_result1 = new_result1.strip() 
        
        print(new_result1)    #<= torrent title
#=> torrent cast / supplier        
        new_detail = str(detail).replace(r"\n", " ")   
#        new_detail = new_detail.rstrip('\n')
        print('L0-',new_detail)
        spliter = "出演"
        new_detail1 = find_prefix(spliter,new_detail)           
#        if "出演" in new_detail:
#          new_detail1 = new_detail.split("出演",1)
#          new_detail1 = str(new_detail1[1])   
#        else:  
#          new_detail1 = ''          
        print('L1-',new_detail1)
        spliter = "："
        new_detail1 = find_prefix(spliter,new_detail1[0:13]) 
#        if "：" in new_detail1[0:13]:
#          print('L11-',new_detail1[0:13])  
#          new_detail1 = new_detail1.split("：",1)
#          new_detail1 = str(new_detail1[1])
#        else:
#          new_detail1 = ''         
##        new_detail1 = str(new_detail1[1])
        print('L2-',new_detail1)
        new_detail1 = new_detail1.split("\n",1)
        new_detail1 = str(new_detail1[0])
        print(new_detail1)
#        try:
#            new_detail1 = new_detail1.split("監督",1)
#        except:
#            new_detail1 = new_detail1
#            print('retry')
#            continue
#        new_detail1 = new_detail1.split("監督",1)
        cast = '-' + str(new_detail1).strip() 
        
        new_detail = str(detail).replace(r"\n", " ")        
        print("without enter:",new_detail)
        spliter = "レーベル"
        new_detail1 = find_prefix(spliter,new_detail)  
#        if "レーベル" in new_detail:
#          new_detail1 = new_detail.split("レーベル",1)
#          new_detail1 = str(new_detail1[1])        
#        else:
#          new_detail1 = ''  
        print('L3-',new_detail1)
        spliter = "："
#        new_detail1 = find_prefix(spliter,new_detail1[0:13]) 
        new_detail1 = find_prefix(spliter,new_detail1[0:14]) 
#        if "：" in new_detail1[0:13]:  
#          new_detail1 = new_detail1.split("：",1)
#          new_detail1 = str(new_detail1[1])
#        else:  
#          new_detail1 = ''
        print('L4-',new_detail1)
        new_detail1 = new_detail1.split("\n",1)
        new_detail1 = str(new_detail1[0])
        print(new_detail1)
#        new_detail1 = new_detail1.split("ジャンル",1)
#find the abbreviation of supplier ---------------
        value = new_detail1
# query database         
#        for r in supp_records:  
##          print(f"{r.ALL_NAME}\t{r.ABBREV}")   
#          if value in {r.ALL_NAME}:
#            print(f"{r.ALL_NAME}\t{r.ABBREV}") 
#            new_detail1 = r.ABBREV
#            break        <=query database 
        
# query dataframe =>
        print(supp_records)
        outcome1 = supp_records.query('ALL_NAME==@value', engine='python') 
        print(outcome1)
        if not outcome1.empty:
          index_item  = outcome1.index.item()
          print(index_item)
          new_detail1 = outcome1.at[index_item, "ABBREV"]
# <=query dataframe        
        
        supplier = '(' + str(new_detail1).strip() + ')'
            
        print('supplier:' , supplier)
#----find the abbreviation of supplier  ------   
        #<=torrent caste / supplier   
                      # DOS command                     
        folder = supplier + new_result1 + cast
        for char in folder:
            if char in "?!/;:*":
              folder = folder.replace(char,'')  
        folder.encode('utf8')
        command = '\\tmp\\9997\\' + folder       
        print('Dos command:',command)
#command = str(command.decoding('utf-8')
        os.mkdir(command)              #<= DOS command
#        output = stream.read()
        #output
        path = path1  + folder + '\\'     #儲存路徑 #
        print(path)
        driver.back()              #回上一個page"
#        element = driver.find_element_by_partial_link_text(l_text) 
        element = driver.find_element(By.XPATH , "//i[@class='fa fa-fw fa-download']")
        element.click()
#        actionchains = ActionChains(driver)
#        actionchains.context_click(element).perform()
#        time.sleep(3)
#        pyautogui.press('down')
#        pyautogui.press('down')
#        pyautogui.press('down')
#        pyautogui.press('down')
#        pyautogui.typewrite(['enter']) 
        time.sleep(8)
        keyboard.press_and_release('home')
        keyboard.write(path,delay = 0.1)       #存檔到指定路徑
        keyboard.press_and_release('enter')   
        print(line)          
#        driver.back()              #回上一個page"
        
        
#l_text = line
infile.close()
