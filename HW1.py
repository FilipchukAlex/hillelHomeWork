# Find the results of an expression for arbitrary values
import math
# Set arbitrary values and print them to the user
a = -9
b = 31
c = 4
print("Our values: \na =",a,"\nb =",b,"\nc =",c)
# Let's find and print the results
print("Expressions and results:")
print("a+b*(c/2) =",a + b * (c / 2))
print("(a**2+b**2) % 2 =",(a**2 + b**2) % 2)
print("(a+b)/12*c%4+b =",(a + b) / 12 * c % 4 + b)
print("(a-b*c)/(a+b)%c =",(a - b * c) / (a + b) % c)
print("|a-b|/(a+b)**3-cos(c) =",math.fabs(a - b) / (a + b)**3 - math.cos(c))
print("(ln(1+c)/(-b))**4+|a| =",(math.log1p(c) / (-b))**4 + math.fabs(a))