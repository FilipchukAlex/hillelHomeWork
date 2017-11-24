def chess_reward():
    cages = 0
    corns = 1
    while corns <= 1000000:
        corns *= 2
        cages += 1
    return  cages, corns - 1


print(chess_reward())