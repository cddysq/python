# -*-coding:utf-8 -*-
# @author  :cddysq
# @date    :2021/12/23 16:04
# @version :v1.0.0

# 文件操作
import os

# 引入控制台颜色修改方法
from library.console_color import *


def create_a_file():
    file_name = input("请输入待创建文件名,默认(like.txt):")
    if file_name.strip() == '':
        file_name = "like.txt"
    content = input("请输入文件内容:")
    if content.strip() == '':
        content = "I love three things in this world. Sun, moon and you. Sun for morning, moon for night , and you forever ."
    file_url = get_file_url(file_name)
    file = open(file_url, "w+", encoding='utf-8')
    file.write(content)
    file.close()
    print(FontColor.set_color(f"创建 {file_name} Success! 文件内容为：{content}", Colors.green))


def get_file_url(file_name):
    """ 返回文件完整路径 """
    # 获取父路径
    pardir = os.path.pardir
    # 获取系统分割符
    sep = os.sep
    # 组装文件路径
    file_url = f"{pardir}{sep}resources{sep}{file_name}"
    return file_url


def delete_the_file():
    file_name = input("请输入需要删除的文件名:")
    if file_name.strip() == '':
        return
    file_url = get_file_url(file_name)
    if not os.path.exists(file_url):
        print(FontColor.set_color(f"文件 {file_name} 不存在", Colors.yellow))
        return
    os.remove(file_url)
    print(FontColor.set_color(f"文件 {file_name} 删除成功!", Colors.green))


while True:
    print(f"{'==' * 3}欢迎使用文件操作系统v1.0{'==' * 3}")
    print("1.创建文件")
    print("2.删除文件")
    print("0.退出系统")
    instruct = input("请输入对应编号进行操作:")
    if instruct == '1':
        create_a_file()
    elif instruct == '2':
        delete_the_file()
    elif instruct == '0':
        print("bye~")
        break
    else:
        print(FontColor.set_color("指令错误,请重试!", Colors.red))
