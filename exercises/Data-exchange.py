# -*-coding:utf-8 -*-
# @author  :cddysq
# @date    :2021/12/21 17:16
# @version :v1.0.0

# 临时变量交换数据
a = 10
b = 20
temp = a
a = b
b = temp
print(f"a={a},b={b}")
print("=" * 18)

# 算法交换
c = 10
d = 20
c = c + d
d = c - d
c = c - d
print(f"c={c},d={d}")
print("=" * 18)

# 元组拆包f,e => (f,e) => e f
e = 10
f = 20
e, f = f, e
print(f"e={e},f={f}")
