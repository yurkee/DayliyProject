# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/22 15:10
"""
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

sql = "insert into user(id,name) values ('1','tom')"
cursor.execute(sql)
sql = "insert into user(id,name) values ('2','kim')"
cursor.execute(sql)

cursor.close()
conn.commit()
conn.close()