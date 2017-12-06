def make_lst_fibonachi(quantity_of_numbers):
    fib_lst = [0, 1]
    for i in range(2, quantity_of_numbers):
        fib_lst.append((fib_lst[i - 1] + fib_lst[i - 2]))
    return fib_lst


print(sum(make_lst_fibonachi(10)))
