import random

lower_bound = 100000000000
upper_bound = 999999999999
number = random.randint(lower_bound, upper_bound)
print(number)


def get_max_digit(number):
    list_of_digits = [int(digit) for digit in (str(number))]
    max_digit = max(list_of_digits)
    return max_digit


print(get_max_digit(number))




