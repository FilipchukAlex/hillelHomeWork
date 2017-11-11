string = "Leo Tolstoy*1828-08-28*1910-11-20"
#string = "Marcus Aurelius*121-04-26*180-03-17"
#string = "Dunkan McLeod * 2-11-5, 22:43 * 567 - 4 - 7, 07:21 "

string_new = string.split('*')
birth_date = string_new[1]
death_date = string_new[2]

birth_year = ""
death_year = ""

for letter in birth_date:
    if letter != "-":
         birth_year += letter
    else:
        break

for letter2 in death_date:
    if letter2 != "-":
        death_year += letter2
    else:
         break

age = int(death_year) - int(birth_year)
print(string_new[0], ',', str(age))


