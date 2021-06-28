# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/19 16:11
"""

try:
    # print(10 / 0)
    # a = b + 1
    a = 1 + 1
except (NameError,ZeroDivisionError) as e:
    print(e)
except Exception as e:
    print(e)
else:
    print('else')
finally:
    print('finally')

print('2')