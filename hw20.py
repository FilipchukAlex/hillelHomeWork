import random

num_limit = 100
lower_bound = 76
upper_bound = 280

def diff_even_odd(num_limit, lower_bound, upper_bound):
    even_total_sum = 0
    odd_total_sum = 0
    for i in range(num_limit):
        number = random.randint(lower_bound, upper_bound)
        if number % 2 == 0:
            even_total_sum += number
        else:
            odd_total_sum += number
    return even_total_sum - odd_total_sum


print(diff_even_odd(num_limit, lower_bound, upper_bound))


