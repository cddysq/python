# -*-coding:utf-8 -*-
# @author  :cddysq
# @date    :2021/12/15 10:25
# @version :v1.0.0

# 输出5x5的正方形
i = 0
while i < 5:
    j = 0
    while j < 5:
        print("*  ", end='')
        j += 1
    print("")
    i += 1

print("=" * 60)

# 打印指定行高的等腰三角形
height = input("打印等腰三角形高度：")
while height.strip() == '':
    input("打印等腰三角形高度：")
print("")
height = int(height) + 1
# 遍历高度次数从1开始
for i in range(1, height):
    # 空格规律：高度-n
    print(" " * (height - i), end="")
    j = 1
    # 等腰三角形公式：2n-1
    while j <= (2 * i - 1):
        print("*", end="")
        j += 1
    print("")
