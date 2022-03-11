
class Time:
    """ Represents a time with hours, minutes, and seconds. """

    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s


def print_time(time_obj):
    """ Prints a time object using the hh:mm:ss format. """

    print('%.2d:%.2d:%.2d' % (time_obj.h, time_obj.m, time_obj.s))


def time2secs(t0):
    """ Converts a Time object to seconds.
        Output: integer """

    return t0.h * 3600 + t0.m * 60 + t0.s


def secs2time(secs):
    """ Converts seconds into a Time object.
        Output: Time object """

    return Time((secs // 3600) % 24, (secs % 3600) // 60, secs % 60)


def is_after(t1, t2):
    """ Checks if the first of two time objects happens chronologically after the second.
        Output: Boolean """

    return time2secs(t1) > time2secs(t2)


def add_time(t1, t2):
    """ Adds two time objects.
        Output: a Time object """

    return secs2time(time2secs(t1) + time2secs(t2))


time1 = Time(2, 29, 50)
print_time(time1)

time2 = Time(1, 30, 10)
print_time(time2)

print(is_after(time1, time2))
print_time(add_time(time1, time2))
