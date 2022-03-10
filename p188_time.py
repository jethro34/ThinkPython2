
class Time:
    """ Represents a time with hours, minutes, and seconds. """

    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s


def print_time(time_obj):
    """ Prints a time object using the hh:mm:ss format. """

    print('%.2d:%.2d:%.2d' % (time_obj.h, time_obj.m, time_obj.s))


def is_after(t1, t2):
    """ Checks if the first of two time objects happens chronologically after the second.
        Output: Boolean """

    return (t1.h > t2.h) or (t1.h == t2.h and t1.m > t2.m) or (t1.h == t2.h and t1.m == t2.m and t1.s > t2.s)


time1 = Time(22, 5, 14)
time2 = Time(22, 5, 14)

print_time(time1)
print_time(time2)

print(is_after(time1, time2))
