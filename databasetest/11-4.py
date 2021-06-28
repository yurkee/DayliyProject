# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/22 15:54
"""
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

sql = "update user set name='nice' where id='2'"
cursor.execute(sql)

sql = "select * from user"
cursor.execute(sql)
result = cursor.fetchall()
for r in result:
    print("我是%d号，我叫%s" % r)

cursor.close()
conn.commit()
conn.close()