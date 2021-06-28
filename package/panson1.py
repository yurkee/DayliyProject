# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/17 18:26
"""

# __all__ = ['a', 'Add']  #导入控制权限



a = 1
b = 2

def Add(x, y):
    return x+y


class Kid:
    def __init__(self, age):
        self.age = age

    def laugh(self):
        print('i am %d years old' % self.age)