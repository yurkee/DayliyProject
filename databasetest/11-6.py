# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/22 15:54
"""
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

try:
    sql = "update user set name='nice' where id='2'"
    cursor.execute(sql)

    sql = "select * from user"
    cursor.execute(sql)
    result = cursor.fetchall()
    for r in result:
        print("我是%d号，我叫%s" % r)

    conn.commit()
except Exception as e:
    conn.rollback()
finally:
    cursor.close()
    conn.close()


