number = 56


def is_even(number):
    return number % 2 == 0


if is_even(number):
    print("The number %d is even" % number)
else:
    print("The number %d is not even" % number)