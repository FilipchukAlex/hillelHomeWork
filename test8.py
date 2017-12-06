lst = [2, 5, 78, 45, 1]


def replace_max_min(lst):
    idx_min, idx_max = lst.index(min(lst)), lst.index(max(lst))
    lst[idx_min], lst[idx_max] = lst[idx_max], lst[idx_min]
    return lst

print(replace_max_min(lst))
