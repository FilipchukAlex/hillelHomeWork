list_to_shuffle = [digit for digit in range(1, 100, 2)]


def shuffle_list(list_to_shuffle):
    import random
    k = 0
    for i in range(50):
        n = random.randint(k, 49)
        number = list_to_shuffle[n]
        list_to_shuffle.remove(number)
        list_to_shuffle.insert(0, number)
        k += 1
    return list_to_shuffle


print(shuffle_list(list_to_shuffle))