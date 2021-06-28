# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/22 16:00
"""

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

sql = "insert into user (id,name) values ('3','kim')"
cursor.execute(sql)
conn.commit()

sql = 'select * from user'
cursor.execute(sql)
result = cursor.fetchall()
for r in result:
    print("我是%d号，我叫%s" % r)

sql = "delete from user where id='3'"
cursor.execute(sql)
conn.commit()

sql = 'select * from user'
cursor.execute(sql)
result = cursor.fetchall()
for r in result:
    print("我是%d号，我叫%s" % r)

cursor.close()
conn.close()