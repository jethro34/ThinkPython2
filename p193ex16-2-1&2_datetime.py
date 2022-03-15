# 16-2.1: prints the current day of the week
# 16-2.2a: takes a birthdate and prints the user’s age
# 16-2.2b: takes a birthday and returns the number of days, hours, minutes, and seconds until the next birthday.

import datetime


def age_from_bd(y, m, d):
    """ Takes a birthdate and returns the corresponding age.
        Output: int """

    bd = datetime.date(y, m, d)
    td = datetime.date.today()
    adjust = (td < bd.replace(year=td.year)) * -1   # adjusting if this year's birthday hasn't passed
    age = td.year - bd.year + adjust                # a timedelta object

    return age


def till_bd(m, d):
    """ Takes a birthday and returns the days, hours, minutes, and seconds until the next.
        Output: Timedelta object """

    td = datetime.datetime.now()
    bd = datetime.datetime(td.year, m, d)
    if td >= bd:                                # adjusting if current year's birthday passed already
        bd = bd.replace(td.year + 1)

    till = bd - td                              # finding difference; Timedelta object
    return till - datetime.timedelta(microseconds=till.microseconds)    # removing microseconds attribute


print(datetime.datetime.now().strftime('%A'))
print(age_from_bd(1980, 3, 16))
print(till_bd(2, 17))
