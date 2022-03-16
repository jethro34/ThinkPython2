# computes the day when one person is n times older than the other

import datetime


def nx_older(dob1, dob2, n):
    """ Finds the day in which person with DOB1 is n times older than person with DOB2.
        Output: Date object """

    if dob2 < dob1:
        dob1, dob2 = dob2, dob1

    td = dob2 - dob1
    tt = td * n / (n - 1)

    return dob1 + tt


bd1, bd2 = datetime.date(1972, 8, 31), datetime.date(1980, 9, 23)
print(nx_older(bd1, bd2, 4))
