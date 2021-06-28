# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/21 16:24
"""

with open('data.txt', 'r') as file:
    datas = file.readlines()
    for line in datas:
        print(line, end='')