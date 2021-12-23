# -*-coding:utf-8 -*-
# @author  :cddysq
# @date    :2021/12/22 17:30
# @version :v1.0.0

# 斐波那契数列：F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)（n ≥ 2，n ∈ N*）

def formula(n):
    """ 返回斐波那契数列某一位f(n)的值 """
    if n == 0 or n == 1:
        return 1
    data = {0: 1, 1: 1}
    for i in range(2, n + 1):
        data[i] = data[i - 1] + data[i - 2]
    return data[n]


def recursion(n):
    """ 递归方式返回斐波那契数列某一位f(n)的值 """
    if n == 0 or n == 1:
        return 1
    return recursion(n - 1) + recursion(n - 2)


n = input("请输入待计算的斐波那契数列n值:")
while n.strip() == '':
    n = input("请输入待计算的斐波那契数列n值:")
n = int(n)
print(f"斐波那契数列：f({n})={formula(n)}")
print(f"斐波那契数列：f({n})={recursion(n)}")
