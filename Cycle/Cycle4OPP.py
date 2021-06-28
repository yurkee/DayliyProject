# coding:utf-8

"""
面向过程方式解决小孩和圈的题目
 @Author : Cong
 @Time : 2021/6/15 17:47
"""

cycle = [i for i in range(1, 501)]
step = 1

while len(cycle) > 1:
    dels = []
    for kid in cycle:
        if step % 3 == 0:
            dels.append(kid)
        step += 1

    for kid in dels:
        cycle.remove(kid)

print(cycle)