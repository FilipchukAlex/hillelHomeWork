def gen_primes():
    import math
    lst_primes =[]
    for i in range(2, 101):
        for j in range(2, i):
            if j > math.sqrt(i):
                lst_primes.append(i)
                break
            if i % j == 0:
                break
        else:
            lst_primes.append(i)
    return lst_primes


print(gen_primes())