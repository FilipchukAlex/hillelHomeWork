input_text = "Напишите функцию, которая преобразует передан-ный ей текст.Cпособом, похожим на описанный выше."

lst_punctuation = []
for index, symbol in enumerate([symbol for symbol in input_text]):
    if symbol in ("[, \-!?:;.\"\']+"):
        lst_punctuation.append((index, symbol))

input_words = split(r"[,() \n\-!?:;.\"\'\\]+", input_text)
if input_words[0] == '':
    del input_words[0]
if input_words[-1] == '':
    del input_words[-1]

for word in input_words:
    word2 = [symbol.split() for symbol in word[1: -1]]
    random.shuffle(word2)
    word2.append(word[-1])
    word2.insert(0, word[0])
    print(word2)

    print(word)
