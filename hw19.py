import random

num_limit = 100
lower_bound = -150
upper_bound = 280


def find_max(num_limit, lower_bound, upper_bound):
    list_of_numbers = []
    for i in range(num_limit):
        number = random.randint(lower_bound, upper_bound)
        list_of_numbers.append(number)
    return max(list_of_numbers)


print(find_max(num_limit, lower_bound, upper_bound))