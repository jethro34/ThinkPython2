
import copy


class Point:
    """ Represents a point with its x-y coordinates. """

    def __init__(self, xc, yc):
        self.xc = xc                # x coordinate
        self.yc = yc                # y coordinate


class Rect:
    """ Represents a rectangle with two opposite corners."""

    def __init__(self, blc, urc):
        self.blc = blc              # bottom-left corner
        self.urc = urc              # upper-right corner


def move_rect(rekt, dx, dy):
    """ Moves a rectangle object by updating its two corners."""

    rekt.blc.xc += dx
    rekt.urc.xc += dx
    rekt.blc.yc += dy
    rekt.urc.yc += dy


def copy_rect(rekt, dx, dy):
    """ Creates a new rectangle object at the updated corners."""

    deep_c = copy.deepcopy(rekt)    # making a deep copy
    move_rect(deep_c, dx, dy)       # moving the new deep-copied rectangle
    return deep_c


corner1, corner2 = Point(0, 0), Point(8, 2)

rect1 = Rect(corner1, corner2)
print(rect1.blc.xc, rect1.blc.yc, rect1.urc.xc, rect1.urc.yc)

move_rect(rect1, 1, 1)

print(rect1.blc.xc, rect1.blc.yc, rect1.urc.xc, rect1.urc.yc)

rect2 = copy_rect(rect1, 3, 3)
print(rect2.blc.xc, rect2.blc.yc, rect2.urc.xc, rect2.urc.yc)
