#I WILL REVIEW HOW TO USE PYTHON AGAIN
a=1

"""
输入年份，闰年输出True，平年输出False

Version: 1.0
Author: 骆昊
"""
year = int(input('请输入年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f'{is_leap = }')


