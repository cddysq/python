# -*-coding:utf-8 -*-
# @author  :cddysq
# @date    :2021/12/15 17:41
# @version :v1.0.0

# 打印9x9乘法口诀表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i}", end="\t")
        j += 1
    print("")
    i += 1
