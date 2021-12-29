# -*-coding:utf-8 -*-
# @author  :cddysq
# @date    :2021/12/23 16:54
# @version :v1.0.0

"""
设置控制台字体颜色
代码格式：\033[显示方式;前景色;背景色m+文字+\033[0m
"""


class Colors(object):
    # 颜色枚举
    white = "white"  # default
    black = "black"  # 黑色
    red = "red"  # 红色
    green = "green"  # 绿色
    yellow = "yellow"  # 黄色
    blue = "blue"  # 蓝色
    Violet = "Viole"  # 紫色
    cyan = "cyan"  # 青色
    gray = "gray"  # 灰色


class FontColor(object):
    # 开始标志位
    __start = "\033["

    # 颜色码
    white = "99"  # default
    black = "30"
    red = "31"
    green = "32"
    yellow = "33"
    blue = "34"
    Violet = "35"
    cyan = "36"
    gray = "37"

    # 背景色
    white_background = ";99"  # default
    black_background = ";40"
    red_background = ";41"
    green_background = ";42"
    yellow_background = ";43"
    blue_background = ";44"
    Violet_background = ";45"
    cyan_background = ";46"
    gray_background = ";47"

    # 下划线标志
    __default = "0;"  # 默认
    __highlight = "1;"  # 高亮 default
    __underline = "4;"  # 下划线

    # 字母
    __m = "m"

    # 结束标志位
    __end = "\033[0m"

    @classmethod
    def set_color(cls, text, color=Colors.white, underline=False):
        """
        设置文字颜色
        调用方式：文字 + 文字颜色 + 下划线标志
        """
        if hasattr(cls, color):
            end = cls.__m + text + cls.__end
            if underline:
                return cls.__start + cls.__underline + getattr(cls, color) + end
            else:
                return cls.__start + cls.__highlight + getattr(cls, color) + end
        else:
            return text

    @classmethod
    def set_backcolor(cls, text, backcolor=Colors.white, underline=False):
        """
        设置文字背景色
        调用方式：文字 + 背景色 + 下划线标志
        """
        backcolor = backcolor + "_background"
        if hasattr(cls, backcolor):
            end = cls.__m + text + cls.__end
            if underline:
                return cls.__start + cls.__underline + cls.white + getattr(cls, backcolor) + end
            else:
                return cls.__start + cls.__highlight + cls.white + getattr(cls, backcolor) + end
        else:
            return text

    @classmethod
    def set_color_and_backcolor(cls, text, color=Colors.white, backcolor=Colors.white, underline=False):
        """
        设置文字颜色和背景色
        调用方式：文字 + 文字颜色 + 背景色 + 下划线标志
        """
        backcolor = backcolor + "_background"
        if hasattr(cls, color) or hasattr(cls, backcolor):
            end = cls.__m + text + cls.__end
            if underline:
                return cls.__start + cls.__underline + getattr(cls, color) + getattr(cls, backcolor) + end
            else:
                return cls.__start + cls.__highlight + getattr(cls, color) + getattr(cls, backcolor) + end
        else:
            return text
