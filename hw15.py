import math
x1 = 3; y1 = -2; r1 = 7
x2 = -8; y2 = 4; r2 = 5


def intersection_of_two_circles(x1, y1, r1, x2, y2, r2):
    centre_to_centre_distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    d = centre_to_centre_distance
    return d < r1 + r2 and d > abs(r1 - r2)


if intersection_of_two_circles(x1, y1, r1, x2, y2, r2):
    print("The circles intersect.")
else:
    print("The circles don't intersect.")