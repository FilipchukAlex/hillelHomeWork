str = 'Some text, to check.'


def is_isogram(str):
    import string
    lst_str = [symbol for symbol in str if symbol in string.ascii_letters]
    return len(lst_str) == len(set(lst_str))


if is_isogram(str):
    print("'%s' - is isogram" % str)
else:
    print("'%s' - is not isogram" % str)
