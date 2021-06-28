# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/21 16:32
"""

configData = {}

with open('app.config', 'r') as file:
    datas = file.readlines()
    for line in datas:
        if line.startswith('#'):
            continue
        key = line.split("=")[0]
        value = line.split("=")[1].replace("\n", '')
        configData[key] = value

if __name__ == '__main__':
    print(configData)