# Conversion of the American date format to European
american_date = "05.17.2016"
print('The American date format:', american_date)
temp_date = american_date.split('.')
european_date = temp_date[1], temp_date[0], temp_date[2]
european_date = '.'.join(european_date)
print("The result of conversion,the European data format:", european_date)
