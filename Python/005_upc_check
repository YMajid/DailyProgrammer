"""
author = yousif majid
date = 2019-03-23
link = https://www.reddit.com/r/dailyprogrammer/comments/a72sdj/20181217_challenge_370_easy_upc_check_digits/
"""


def upc_checker(num):
    while len(num) < 11:
        num = '0'+num
    while len(num) > 11:
        num = num[:len(num)-1]
    sum = 0
    for i in num[0::2]:
        sum += int(i)
    sum *= 3
    for j in num[1::2]:
        sum += int(j)
    M = sum%10
    if M == 0:
        return 0
    else:
        return 10-M


print(upc_checker('1234567'))
