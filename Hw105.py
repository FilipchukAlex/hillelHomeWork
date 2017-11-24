def is_valid_credit_card(credit_card):
    if len(credit_card) > 1 and credit_card.replace(' ', '').isdigit():
        credit_card = [int(digit) for digit in (credit_card.replace(' ', ''))]
        credit_card.reverse()
        double_digits = []
        for digit in credit_card[1::2]:
            if digit * 2 > 9:
                new_digit = digit * 2 - 9
            else:
                new_digit = digit * 2
            double_digits.append(new_digit)
        credit_card[1::2] = double_digits
        return sum(credit_card) % 10 == 0
    else:
        return False


print(is_valid_credit_card('4539 1488 0343 6467'))