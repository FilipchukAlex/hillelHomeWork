string = 'Leo Tolstoy*1828-08-28*1910-11-20'
string2 = string.split('*')
birth_date = string2[1]
death_date = string2[2]
birth_year = int(birth_date.split('-')[0])
death_year = int(death_date.split('-')[0])
age = death_year - birth_year
print(string2[0], ",", str(age))