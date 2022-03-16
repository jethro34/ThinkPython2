# there is a day when one person is twice as old as another.
# 16-2.4: takes two birthdays and computes their Double Day

import datetime


def double_day(bd1, bd2):
    """ Takes two DOB Date objects and returns their Double Day.
        Output: Date object """

    if bd2 < bd1:                       # ordering & swapping the DOBs if not chronological
        bd1, bd2 = bd2, bd1

    td = bd2 - bd1                      # finding timedelta

    return bd2 + td                     # finding the double day


dob1, dob2 = datetime.date(2001, 10, 31), datetime.date(2009, 4, 21)
print(double_day(dob1, dob2))
