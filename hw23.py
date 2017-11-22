import random

comp_number = random.randint(1,10)
user_number = int(input("Enter the number from 1 to 10: "))

while user_number != comp_number:
    if user_number > comp_number:
        print("My number is smaller")
        user_number = int(input("Enter the number: "))
    else:
        print("My number is bigger")
        user_number = int(input("Enter the number:"))
else:
    print("Yes, it is %d" % comp_number)
    print(input("Press Enter to quit"))
