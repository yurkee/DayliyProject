# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/21 19:25
"""

import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

sql = "create table user (id int(11) primary key, name varchar(18)) "
cursor.execute(sql)

cursor.close()
conn.close()