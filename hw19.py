import random

num_limit = 100
lower_bound = -237
upper_bound = -4


def find_max(num_limit, lower_bound, upper_bound):
    max_number = random.randint(lower_bound, upper_bound)
    for i in range(num_limit):
        number = random.randint(lower_bound, upper_bound)
        if number >= max_number:
            max_number = number
    return max_number


print(find_max(num_limit, lower_bound, upper_bound))