import math
x1 = 1; y1 = -2; r1 = 7
x2 = -8; y2 = 4; r2 = 5

circle1 = (x1, y1, r1)
circle2 = (x2, y2, r2)


def intersection_of_two_circles(circle1, circle2):
    centre_to_centre_distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    d = centre_to_centre_distance
    return d < r1 + r2 and d > abs(r1 - r2)


if intersection_of_two_circles(circle1, circle2):
    print("The circles intersect.")
else:
    print("The circles don't intersect.")