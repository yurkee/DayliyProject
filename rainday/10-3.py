# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/21 17:10
"""

from rainday.appConfig import configData

print('数据库地址：', configData['db_url'])
print('数据库端口：', configData['db_port'])
print('数据库用户：', configData['db_user'])
print('数据库密码：', configData['db_pass'])