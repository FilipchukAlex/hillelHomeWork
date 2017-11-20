import random

num_limit = 100
lower_bound = -150
upper_bound = 280


def find_max(num_limit, lower_bound, upper_bound):
    max_number = 0
    for i in range(num_limit):
        number = random.randint(lower_bound, upper_bound)
        if number >= max_number:
            max_number = number
    return max_number


print(find_max(num_limit, lower_bound, upper_bound))