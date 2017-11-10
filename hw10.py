string = "Leo Tolstoy*1828-08-28*1910-11-20"
a = string.find('*')
b = string.find('-')
birth_year = int(string[(a + 1):b])
newstring = string[(b + 1):]
c = newstring.find('*')
newstring = newstring[(c + 1):]
d = newstring.find('-')
death_year = int(newstring[:d])
age = death_year - birth_year
print(string[:a] + ",", + age)

string = 'Marcus Aurelius*121-04-26*180-03-17'
a = string.find('*')
b = string.find('-')
birth_year = int(string[(a + 1):b])
newstring = string[(b + 1):]
c = newstring.find('*')
newstring = newstring[(c + 1):]
d = newstring.find('-')
death_year = int(newstring[:d])
age = death_year - birth_year
print(string[:a] + ",", + age)

string = 'Dunkan McLeod * 2-11-5, 22:43 * 567 - 4 - 7, 07:21 '
a = string.find('*')
b = string.find('-')
birth_year = int(string[(a + 1):b])
newstring = string[(b + 1):]
c = newstring.find('*')
newstring = newstring[(c + 1):]
d = newstring.find('-')
death_year = int(newstring[:d])
age = death_year - birth_year
print(string[:a] + ",", + age)



