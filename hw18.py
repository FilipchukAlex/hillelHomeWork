
first = 'x'
last = 's'


def sum_symbol_codes(first, last):
    first_ord = ord(first)
    last_ord = ord(last)
    if first_ord <= last_ord:
        lower_bound = first_ord
        upper_bound = last_ord
    else:
        lower_bound = last_ord
        upper_bound = first_ord
    sum_symbol = 0
    for i in range(lower_bound, upper_bound + 1):
        sum_symbol += i
    return sum_symbol


print(sum_symbol_codes(first, last))