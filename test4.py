while True:
    number = input("Please, enter five digit number, or 'q' to quit: ")
    if number.isdigit() == True and len(number) == 5:
        result = 1
        for digit in number[::2]:
            result *= int(digit)
        print("Your result is: %d" % result)
        break
    if number == 'q':
        print("Come again...")
        break
