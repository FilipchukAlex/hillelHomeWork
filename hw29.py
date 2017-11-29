

def gen_password():
    import random, re
    SYMBOLS = ('_AaBb0CcDdEeFfGgHh9Ii_JjKk8LlMmN7nOo_6Pp5QqRr4SsT3tUu2Vv_Ww1XxYyZz_')
    while True:
        password = ''.join(random.choice(SYMBOLS) for i in range(8))
        # I dont know how to compress that entry, for now, just have begun with re
        if (re.findall('[0-9]', password)) and (re.findall('[a-z]', password)) and (re.findall('[A-Z]', password)):
            return password


print(gen_password())