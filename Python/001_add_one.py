# https://www.reddit.com/r/dailyprogrammer/comments/aphavc/20190211_challenge_375_easy_print_a_new_number_by/


def add_one_simple():
    number = input('Enter a number: ')
    new_number = []
    for n in number:
        nn = int(n)+1
        new_number.append(nn)
    return int(''.join(map(str, new_number)))

def add_one_complex():
    number = int(input('Enter a number: '))
    new_number = 0
    factor = 1

    while number:
        new_number += ((number % 10)+1)*factor
        if (number % 10)+1 != 10:
            factor *= 10
        else:
            factor = 100
        number //= 10

    return new_number
