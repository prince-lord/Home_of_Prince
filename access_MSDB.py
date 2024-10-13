# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 10:00:04 2024

@author: charles
"""
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import os
import re
import pyodbc
import pyhdb
import datetime
import time
#import pydat
import pandas.io.sql as psql
from pandasql import *
import pandasql as pdsql
import warnings
from hdbcli import dbapi
warnings.filterwarnings('ignore')
from datetime import *
from datetime import datetime
from dateutil.tz import gettz
import smtplib
from email.message import EmailMessage
from smtplib import SMTP
import sys
import sqlite3

if __name__ == "__main__":    #要怎麼讓檔案在被引用時，不該執行的程式碼不被執行
  print("started....")
  mssql_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
  + 'sql.bsite.net\MSSQL2016' + ';DATABASE=' 
  + 'princel_new' + '; UID=' + 'princel_new' +';PWD=' + '1qaz2wsx')  
  print("connections established!")
  
  SQL_QUERY = """
SELECT  top 10 * FROM  [princel_new].[dbo].[MATERIALS];
"""
  df_check = psql.read_sql(SQL_QUERY, mssql_conn) #first option
  print(df_check.head(5))
  
#  SQL_QUERY = """
#SELECT @@SERVERNAME
#"""

cursor = mssql_conn.cursor()
cursor.execute(SQL_QUERY)             #second option
records = cursor.fetchall()
print(type(records))
print (records)
value = 'quisque'
for r in records:     
#    print(f"{r.MAR_NO}\t{r.MAR_TYPE}\t{r.MAR_COST}\t{r.MAR_DESC}")
   if value in {r.MAR_TYPE}:
     print(f"{r.MAR_NO}\t{r.MAR_TYPE}\t{r.MAR_COST}\t{r.MAR_DESC}") 
     break
   else:
     print('none!!')  


#df = pd.read_sql_query('SELECT * FROM products', conn)
df = pd.read_sql_query(SQL_QUERY, mssql_conn)
print(df)
print(type(df))

#conn = sqlite3.connect('princel_new.db')

c = mssql_conn.cursor()
c.execute("INSERT INTO [princel_new].[dbo].[Supplier] (VEN_ID , VEN_NAME , VEN_ADD) VALUES (?, ?, ?)" , ('002', 'test value1', '314'))
#c.execute("INSERT INTO [princel_new].[dbo].[Supplier] VALUES (?, ?, ?)" , ( 1, 'test value1', '314'))
#c.execute("""
#          INSERT INTO princel_new.dbo.Supplier (VEN_ID , VEN_NAME , VEN_ADD) VALUES ('001', 'test value1', '3.14')
#          """)
mssql_conn.commit()
mssql_conn.close()


records = cursor.fetchall()
print(records)
for r in records:
    print(f"{r.MAR_NO}\t{r.MAR_TYPE}\t{r.MAR_COST}")