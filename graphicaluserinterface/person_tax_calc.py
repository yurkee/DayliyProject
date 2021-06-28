# coding:utf-8

"""
 @Author : Cong
 @Time : 2021/6/28 11:35
"""

def person_tax_calc(money):
    if money <= 5000:
        tax = 0
    elif money > 5000 and money <= 8000:
        tax = (money - 5000) * 0.03
    elif money > 8000 and money <= 17000:
        tax = 3000 * 0.03 + (money - 8000) * 0.1
    elif money > 17000 and money <= 30000:
        tax = 3000 * 0.03 + 9000 * 0.1 + (money - 17000) * 0.2
    elif money > 30000 and money <= 40000:
        tax = 3000 * 0.03 + 9000 * 0.1 + 13000 * 0.2 + (money - 30000) * 0.25
    elif money > 40000 and money <= 60000:
        tax = 3000 * 0.03 + 9000 * 0.1 + 13000 * 0.2 + 10000 * 0.25 + (money - 40000) * 0.3
    elif money > 60000 and money <= 85000:
        tax = 3000 * 0.03 + 9000 * 0.1 + 13000 * 0.2 + 10000 * 0.25 + 20000 * 0.3 + (money - 60000) * 0.35
    else:
        tax = 3000 * 0.03 + 9000 * 0.1 + 13000 * 0.2 + 10000 * 0.25 + 20000 * 0.3 + 25000 * 0.35 + (money - 85000) * 0.45
    return tax
