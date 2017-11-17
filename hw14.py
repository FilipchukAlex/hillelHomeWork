number = 58


def is_even(number):
    if number % 2 == 0:
        result = 'even'
    else:
        result = 'not even'
    return result


print("The number %s is %s" % (number, is_even(number)))