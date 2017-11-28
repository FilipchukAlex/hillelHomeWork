list_to_shuffle = [digit for digit in range(1, 100, 2)]


def shuffle_list(list_to_shuffle):
    import random
    while list_to_shuffle:
        print(list_to_shuffle.pop(random.randint(0, len(list_to_shuffle) - 1)))


print(shuffle_list(list_to_shuffle))

