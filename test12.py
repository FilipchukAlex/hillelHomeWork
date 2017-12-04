import random
lst_examples = []
number_of_examples = 0
while number_of_examples <= 14:
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    if (x, y) not in lst_examples and (y, x) not in lst_examples:
        lst_examples.append((x, y))
        number_of_examples += 1
for i, example in enumerate(lst_examples):
    print("Example %d:\t %d * %d = ?" % (i +1, example[0], example[1]))
