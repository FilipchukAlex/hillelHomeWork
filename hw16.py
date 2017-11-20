# Trains crash
v1 = int(input("Please, enter the speed for the first train: "))
v2 = int(input("Please, enter the speed for the second train: "))


def have_trains_crashed(v1, v2):
    return 4 / v1 >= 6 / v2


if have_trains_crashed(v1, v2):
    print("The trains with speeds %d and %d mph have crashed!!!" % (v1, v2))
else:
    print("The trains with speeds %d and %d mph have not crashed" % (v1, v2))



