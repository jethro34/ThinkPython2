# Change the attributes of Time to be a single integer representing seconds since mid‐ night.
# Then modify the methods (and the function int_to_time) to work with the new implementation.
# You should not have to modify the test code in main. When you are done, the output should be the same as before.

class Time:
    """Represents the time of day.
    attributes: seconds since midnight
    """

    def __init__(self, seconds=0):
        """Initializes a time object.
        seconds: int or float
        """
        self.seconds = seconds

    def __str__(self):
        """Returns a string representation of the time."""
        return '%.6d' % self.seconds

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.seconds > other.seconds

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.
        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.seconds + other.seconds
        return int_to_time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.seconds
        return int_to_time(seconds)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        if self.seconds < 0:
            return False
        return True


def int_to_time(seconds):
    """Makes a new Time object.
    seconds: int seconds since midnight.
    """
    time = Time(seconds)
    return time


def main():
    start = Time(0)
    print(start)

    end = start.increment(1337)
    # end = start.increment(1337, 460)
    print(end)

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(0)
    duration = Time(95)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(463)
    t2 = Time(461)
    t3 = Time(457)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()