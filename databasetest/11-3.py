# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/22 15:12
"""
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

sql = 'select * from user'
cursor.execute(sql)

result = cursor.fetchall()
for r in result:
    print("我是%d号，我叫%s" % r)

cursor.close()
conn.close()
