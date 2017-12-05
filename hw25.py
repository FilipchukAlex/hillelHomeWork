list_to_shuffle = [digit for digit in range(1, 100, 2)]


def shuffle_list(list_to_shuffle):
    import random
    for i in range(len(list_to_shuffle)):
        a = random.randint(0, len(list_to_shuffle) - 1)
        b = random.randint(0, len(list_to_shuffle) - 1)
        list_to_shuffle[a], list_to_shuffle[b] = list_to_shuffle[b], list_to_shuffle[a]
    return list_to_shuffle


print(shuffle_list(list_to_shuffle))

