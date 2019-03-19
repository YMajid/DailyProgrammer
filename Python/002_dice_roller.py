"""
author = yousif majid
date = 2019-03-18
link = https://www.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/
"""


from re import split
from random import randint


def dice_roller():
    rolls = input('What would you like to roll? ')
    rolls_list = split('d', rolls)
    result = 0
    for i in range(int(rolls_list[0])):
        result += randint(1, int(rolls_list[1]))
    return result


print(dice_roller())
