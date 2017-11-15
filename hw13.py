import math

leg1 = 12
leg2 = 35

print("Legs of the right-angled triangle are %d and %d" % (leg1, leg2))

def square_and_perimeter_right_triangle(leg1, leg2):
    square =  (leg1 * leg2) / 2
    perimiter = leg1 + leg2 + math.hypot(leg1, leg2)
    return square, perimiter


square, perimiter = (square_and_perimeter_right_triangle(leg1, leg2))
print("Square = %d" % square)
print("Perimiter = %d" % perimiter)
