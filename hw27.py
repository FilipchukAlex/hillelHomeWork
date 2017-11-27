def gen_primes():
    lst_primes =[]
    for i in range(2, 101):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst_primes.append(i)
    return lst_primes


print(gen_primes())