a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def common_elements(a, b):
    common_lst = []
    for element in a:
        if element in b and element not in common_lst:
            common_lst.append(element)
    return common_lst


print(common_elements(a,b))