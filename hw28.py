str_to_encode = input('Please, enter your text...')


def encode(str_to_encode):
    import string
    encryption_table = string.ascii_lowercase + string.digits
    list_to_encode = [symbol for symbol in str_to_encode.lower()]
    for index, symbol in enumerate(list_to_encode):
        if symbol in encryption_table:
            list_to_encode[index] = (encryption_table[encryption_table.find(symbol) - len(encryption_table) + 5])
        else:
            list_to_encode[index] = symbol
    return ''.join(list_to_encode)

print(encode(str_to_encode))
