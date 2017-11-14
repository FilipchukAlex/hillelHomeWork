import math
angles = (60, 45, 40)


def degrees_to_radians(degrees):
    return math.radians(degrees)


for n in angles:
    print(math.cos(degrees_to_radians(n)))

# Question!
#for n in angles:
#   print("The cosine of the angle of %d degrees =", math.cos(degrees_to_radians(n)) % n)