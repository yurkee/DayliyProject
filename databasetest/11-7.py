# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/22 16:35
"""

import pymysql

conn = pymysql.connect(host='192.168.7.27', user='tester', password='Btclass$123', db='cong_test', port=3306)

cursor = conn.cursor()

sql ='create table user (id int(11) primary key ,name varchar(50))'
cursor.execute(sql)

cursor.close()
conn.close()