import random
lst = [random.randint(-1, 1) for i in range(11)]


def calc_frequency(lst):
    results = []
    for digit in set(lst):
        results.append((digit, lst.count(digit)))
    results.sort(key = lambda x: x[::-1], reverse=True)
    times = [results[i][1] for i in range(0, len(results))]
    if len(set(times)) == len(results):
        return results[0][0]


print(calc_frequency(lst))