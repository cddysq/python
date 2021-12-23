# -*-coding:utf-8 -*-
# @author  :cddysq
# @date    :2021/12/23 16:54
# @version :v1.0.0

# 设置控制台字体颜色
# 代码格式：\033[颜色;显示方式m code \033[0m

class Colors:
    # 颜色枚举
    white = "white"  # default
    red = "red"
    green = "green"
    brown = "brown"  # 棕色
    Pink = "Pink"
    Violet = "Viole"  # 紫色
    blue = "blue"
    black = "black"


class FontColor:
    """不同的版本可能颜色不一样
    调用方式：颜色/背景色/+下划线标志 + 需要加颜色的文字 + 结束标志
    """
    # 颜色码
    white = "\033[30;"  # default
    red = "\033[31;"
    green = "\033[32;"
    brown = "\033[33;"
    Pink = "\033[34;"
    Violet = "\033[35;"  # 紫色
    blue = "\033[36;"
    black = "\033[37;"

    # 背景色
    white_background = "\033[40;"  # default
    red_background = "\033[41;"
    green_background = "\033[42;"
    brown_background = "\033[43;"
    Pink_background = "\033[44;"
    Violet_background = "\033[45;"  # 紫色
    blue_background = "\033[46;"
    black_background = "\033[47;"

    # 下划线标志
    default = "1m"  # default
    underline = "4m"

    # 结束标志位
    end = "\033[0m"

    # 设置字体色方法
    @classmethod
    def set_color(cls, text, color="white", underline=False):
        if hasattr(cls, color):
            if underline:
                return getattr(cls, color) + cls.underline + text + cls.end
            else:
                return getattr(cls, color) + cls.default + text + cls.end
        else:
            return text

    # 设置背景色
    @classmethod
    def set_backcolor(cls, text, backcolor="white", underline=False):
        color = backcolor + "_background"
        if hasattr(cls, color):
            if underline:
                return getattr(cls, color) + cls.underline + text + cls.end
            else:
                return getattr(cls, color) + cls.default + text + cls.end
        else:
            return text
