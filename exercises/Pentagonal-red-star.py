# -*-coding:utf-8 -*-
# @author  :cddysq
# @date    :2021/12/16 10:58
# @version :v1.0.0

import turtle
import time

# 绘制五角红心
turtle.color("red")
# 画五条线
for i in range(5):
    turtle.forward(100)
    # 向右旋转144度
    turtle.right(144)

time.sleep(6)
