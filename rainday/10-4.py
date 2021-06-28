# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/21 17:15
"""

with open('data_write.txt', 'a') as file:
    # data = 'hello python'
    # file.write(data + '\n')
    # data = 'i am sniper'
    # file.write(data)

    datas = ['hello python', 'i am sniper', 'like']
    # for data in datas:
    #     file.write(data + '\n')

    file.writelines([data+'\n' for data in datas])

    # file.writelines('\n'.join(datas))
    # file.write('\n'.join(datas))