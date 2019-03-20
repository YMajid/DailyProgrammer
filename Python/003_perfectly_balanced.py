"""
author = yousif majid
date = 2019-03-20
link = https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/
"""

def balanced(str):
    str_split = list(str.lower())
    if str_split.count('y') == str_split.count('x'):
        return True
    else:
        return False

def balanced_bonus(str):
    count = []
    for i in set(str):
        count.append(list(str.lower()).count(i))
    if all(x == count[0] for x in count):
        return True
    else:
        return False
