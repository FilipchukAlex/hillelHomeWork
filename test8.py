lst = [2, 5, 78, 45,1]


def replace_max_min(lst):
    if lst.index(min(lst)) < lst.index(max(lst)):
        lst[lst.index(max(lst))], lst[lst.index(min(lst))]  =  min(lst), max(lst)
    else:
        lst[lst.index(min(lst))], lst[lst.index(max(lst))] = max(lst), min(lst)
    return lst


print(replace_max_min(lst))
