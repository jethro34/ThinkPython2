
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


def ave_time(t0, dist):
    """ Takes a Time object (representing a finishing time in a race) and a number (representing distance),
        and returns a Time object which represents the average pace (time per mile).
        Output: a Time object """

    return secs2time(time2secs(t0) / dist)


t1 = Time(20, 30, 15)
print_time(ave_time(t1, 5))
