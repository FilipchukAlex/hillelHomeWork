number = 943

def sum_of_digits(number):
    digit1 = number % 10
    number_new1 = number // 10
    digit2 = number_new1 % 10
    number_new2 = number_new1 // 10
    digit3 = number_new2 % 10
    return digit1 + digit2 + digit3


print(sum_of_digits(number))