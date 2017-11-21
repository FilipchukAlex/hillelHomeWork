#
print("Please enter coefficients of a quadratic equation ax**2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a != 0:
    def solve_quadratic_equation(a, b, c):
        import math
        discrim = b**2 - 4 * a * c
        if discrim > 0:
            x1 = (-b + math.sqrt(discrim)) / (2 * a)
            x2 = (-b - math.sqrt(discrim)) / (2 * a)
        elif discrim == 0:
            x1 = -b / (2 * a)
            x2 = None
        else:
            x1 = x2 = None
        return x1, x2
    print("x1 = %s \nx2 = %s" % (solve_quadratic_equation(a, b, c)))
else:
    print("It is not a quadratic equation, 'a' must not be a zero!!!")






