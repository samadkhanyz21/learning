import math

class Point:
    """Represents a point in two-dimensional geometric coordinates"""

    def __init__(self, x=0, y=0):

        """Initialize the position of a new point. The x and y
        coordinates can be specified. If they are not, the
        point defaults to the origin."""

        def move(self, x, y):

            """Move the point to a new location in 2D space."""
            self.x = x
            self.y = y

        def reset(self):

            """Reset the point back to the geometric origin: 0, 0"""
            self.move(0,0)

        def cal_dist(self, other_point):

            """Calculate the distance from this point
            to a second point passed as a parameter.
            This function uses the Pythagorean Theorem
            to calculate the distance between the
            two points. The distance is returned as
            a float."""
            return math.sqrt(
                ((self.x - other_point.x) ** 2) +
                ((self.y - other_point.y) ** 2)
            )


# How to use it
p1 = Point()
p2 = Point()

p1.reset()
p2.move(5,0)

print(p2.cal_dist(p1))

assert p2.cal_dist(p1) == p1.cal_dist(p2)
p1.move(3,4)

print(p1.cal_dist(p2))
print(p1.cal_dist(p1))