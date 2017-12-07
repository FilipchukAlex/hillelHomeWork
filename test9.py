import random
lst_random = [random.randint(-10, 10) for i in range(6)]
#print(lst_random, id(lst_random))


def normalize_lst(lst):
    max_abs_lst = max([abs(number) for number in lst])
    for i, element in enumerate(lst):
        lst[i] = round((element / max_abs_lst), 1)
    #print(lst, id(lst))
    return lst


print(normalize_lst(lst_random))
