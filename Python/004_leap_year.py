"""
author = yousif majid
date = 2019-03-20
link = https://www.reddit.com/r/dailyprogrammer/comments/b0nuoh/20190313_challenge_376_intermediate_the_revised/
"""


def leap_year(year_1, year_2):
    leap_years = []
    years = range(year_1, year_2)
    for year in years:
        if year%4 == 0:
            if year%100 == 0:
                if year/900 == 200 or year/900 == 600:
                    leap_years.append(year)
                else:
                    continue
            else:
                leap_years.append(year)
        else:
            continue
    return len(leap_years)
    
