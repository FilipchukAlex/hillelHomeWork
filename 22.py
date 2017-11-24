list_of_enrollees = ['Vasya Pupkin', 'Aleksandr pushkin', \
                     'Black Cat', 'Mark Zukerberg', 'Chuck norris']

def group_by_surname(list_of_enrollees):
    students = []
    for student in list_of_enrollees:
        students.append(student.split(' '))
    surnames = [element[1] for element in students]
    group1 = group2 = group3 = group4 = 0
    for title in surnames:
        if 'A' <= title[0].upper()  <= 'I':
            group1 += 1
        elif 'J' <= title[0].upper() <= 'P':
            group2 += 1
        elif 'Q' <= title[0].upper() <= 'T':
            group3 += 1
        else:
            group4 += 1
    return  group1, group2, group3, group4


print("Number of students in groups: 'A-I' - %d,'J-P' - %d,\
  'Q-T' - %d,'U-Z' - %d " % (group_by_surname(list_of_enrollees)))


