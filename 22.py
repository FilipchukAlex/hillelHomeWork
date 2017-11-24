list_of_enrollees = ['Vasya Pupkin', 'Aleksandr Pushkin', \
                     'Black Cat', 'Mark Zukerberg', 'Chuck Norris']

def group_by_surname(list_of_enrollees):
    students = []
    for student in list_of_enrollees:
        students.append(student.split(' '))
    surnames = [element[1] for element in students]
    surnames_titles = [surname[0] for surname in surnames]
    group1 = group2 = group3 = group4 = 0
    for title in surnames_titles:
        if 'A' <= title  <= 'I':
            group1 += 1
        if 'J' <= title <= 'P':
            group2 += 1
        if 'Q' <= title <= 'T':
            group3 += 1
        if 'U' <= title <= 'Z':
            group4 += 1
    return  group1, group2, group3, group4


print("Number of students in groups: 'A-I' - %d,'J-P' - %d,\
  'Q-T' - %d,'U-Z' - %d " % (group_by_surname(list_of_enrollees)))


