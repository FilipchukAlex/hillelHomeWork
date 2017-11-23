ALFABET_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
GROUP1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
GROUP2 = ['J', 'K', 'L', 'M', 'N', 'O', 'P']
GROUP3 = ['Q', 'R', 'S', 'T']
GROUP4 = ['U','V','W','X','Y','Z']

list_of_enrollees = ['Vasya Pupkin', 'Aleksandr Pushkin', \
                     'Black Cat', 'Mark Zukerberg', 'Chuck Norris']

def group_by_surname(list_of_enrollees):
    upper_letters =[]

    for students in list_of_enrollees:
        for letter in students:
            if letter in ALFABET_UPPER:
                upper_letters.append(letter)

    upper_letters_surname = upper_letters[1::2]
    students_in_group1 = 0
    students_in_group2 = 0
    students_in_group3 = 0
    students_in_group4 = 0

    for symbol in upper_letters_surname:
        if symbol in GROUP1:
            students_in_group1 += 1
        if symbol in GROUP2:
            students_in_group2 += 1
        if symbol in GROUP3:
            students_in_group3 += 1
        if symbol in GROUP4:
            students_in_group4 += 1

    return students_in_group1, students_in_group2, \
           students_in_group3, students_in_group3


print("Number of students in groups: 'A-I' - %d,'J-P' - %d,\
  'Q-T' - %d,'U-Z' - %d " % (group_by_surname(list_of_enrollees)))




