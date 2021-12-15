# -*-coding:utf-8 -*-
# @author  :cddysq
# @date    :2021/12/7 14:29
# @version :v1.0.0

upper_base = input('请输入梯形上底长度：')
# 空校验
while upper_base.strip() == '':
    upper_base = input('请输入梯形上底长度：')
upper_base = float(upper_base)

the_bottom = input('请输入梯形下底长度：')
while the_bottom.strip() == '':
    the_bottom = input('请输入梯形下底长度：')
the_bottom = float(the_bottom)

height = input('请输入梯形高度：')
while height.strip() == '':
    height = input('请输入梯形高度：')
height = float(height)

# 梯形面积计算公式：（上底+下底)*高/2
result = (upper_base + the_bottom) * height / 2

if __name__ == '__main__':
    print(f'梯形的面积为：{result}')
