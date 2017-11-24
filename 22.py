list_of_enrollees = ['Vasya Pupkin', 'Aleksandr pushkin', \
                     'Black Cat', 'Mark Zukerberg', 'Chuck norris']


def group_by_surname(list_of_enrollees):
    group1 = group2 = group3 = group4 = 0
    for student in list_of_enrollees:
        first_surname_letter = student.split(' ')[1][0]
        if 'A' <= first_surname_letter.upper()  <= 'I':
            group1 += 1
        elif 'J' <= first_surname_letter.upper() <= 'P':
            group2 += 1
        elif 'Q' <= first_surname_letter.upper() <= 'T':
            group3 += 1
        else:
            group4 += 1
    return  group1, group2, group3, group4


print("Number of students in groups: 'A-I' - %d,'J-P' - %d,\
  'Q-T' - %d,'U-Z' - %d " % (group_by_surname(list_of_enrollees)))


