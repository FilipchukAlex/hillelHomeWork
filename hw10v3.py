name_dates = 'Leo Tolstoy*1828-08-28*1910-11-20'
name_dates2 = name_dates.split('*')
birth_date = name_dates2[1]
death_date = name_dates2[2]
birth_year = int(birth_date.split('-')[0])
death_year = int(death_date.split('-')[0])
age = death_year - birth_year
print(name_dates2[0], ",", str(age))