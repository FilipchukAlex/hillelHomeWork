import pickle


running = True

#------------------------------------------------------------------------------
phone_book = [
              {"name": "Petr", "surname": "Petrov", "age": 35, "phone_number":"+380501234567", "birthdate":"12-05-1978"},
              {"name": "Ivan", "surname": "Ivanov", "age": 49, "phone_number":"+380507654321", "birthdate":"09-11-1967"},
             ]


#------------------------------------------------------------------------------
def print_entry(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname: %20s |"      % entry["surname"])
    print ("| Name:    %20s |"      % entry["name"])
    print ("| Age:     %20s |"      % entry["age"])
    print ("| Birthdate:    %15s |" % entry["birthdate"])
    print ("| Phone number:   %s |" % entry["phone_number"])
    print ()


#------------------------------------------------------------------------------
def print_phonebook():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


#------------------------------------------------------------------------------
def print_phonebook_by_age():
    print()
    print()
    print("#########  Phone book  ##########")
    print("--------- sorted by age --------")
    print()

    number = 1
    for entry in sorted(phone_book, key=lambda elem: elem["age"]):
        print_entry(number, entry)
        number += 1





#------------------------------------------------------------------------------
def add_entry_phonebook():
    surname      = str(input("    Enter surname: "))
    name         = str(input("    Enter name: "))
    age          = int(input("    Enter age: "))
    birthdate    = str(input("    Enter birthdate(DD-MM-YYYY): "))
    phone_number = str(input("    Enter phone number: "))

    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["birthdate"] = birthdate
    entry["phone_number"] = phone_number
    phone_book.append(entry)
    printInfo("'%s' added to phonebook" % name)

#------------------------------------------------------------------------------
def printError(message):
    print ("ERROR: %s" % message)


#------------------------------------------------------------------------------
def printInfo(message):
    print ("INFO: %s" % message)


#------------------------------------------------------------------------------
def find_entry_name_phonebook():
    name = str(input("    Enter name: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"].lower() == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Such name not found!!")


#------------------------------------------------------------------------------
def find_entry_age_phonebook():
    age = int(input("    Enter age: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["age"] == age:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("No entry with age %s" % age)


#------------------------------------------------------------------------------
def delete_entry_name_phonebook():
    name = str(input("    Enter name: "))
    found = False
    for entry in phone_book:
        if name in entry["name"].lower():
            printInfo("Entry '%s' deleted" % entry["name"])
            phone_book.remove(entry)
            found = True
    if not found:
        printError("Such name not found!!")

#------------------------------------------------------------------------------
def count_all_entries_in_phonebook():
    print ("Total number of entries: ", len(phone_book))


#------------------------------------------------------------------------------
def print_avr_age():
    pass


#------------------------------------------------------------------------------
def increase_age():
    number_of_years = int(input("Enter number: "))
    for entry in phone_book:
        entry["age"] += number_of_years
    printInfo("Age increased by %s" % number_of_years)

#------------------------------------------------------------------------------
def automatic_increase_age():
    import datetime
    now = datetime.datetime.now()
    for entry in phone_book:
        entry["age"] = now.year - (int(entry["birthdate"].split('-')[2]))
    printInfo("Age increased")
#------------------------------------------------------------------------------
def avr_age_of_all_persons():
    printInfo("Avr. age: %d" % round(sum([element["age"]
             for element in phone_book]) / len(phone_book)))



#------------------------------------------------------------------------------
def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")


#------------------------------------------------------------------------------
def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


#------------------------------------------------------------------------------
def exit():
      global running
      running = False


#------------------------------------------------------------------------------
def print_prompt():
      print()
      print()
      print()
      print("~ Welcome to phonebook ~")
      print("Select one of actions below:")
      print("     1  - Print phonebook entries")
      print("     2  - Print phonebook entries (by age)")
      print("     3  - Add new entry")
      print("     4  - Find entry by name")
      print("     5  - Find entry by age")
      print("     6  - Delete entry by name")
      print("     7  - The number of entries in the phonebook")
      print("     8  - Avr. age of all persons")
      print("     9  - Increase age by num. of years")
      print("     10 - Automatic increase age")
      print("-----------------------------")
      print("     s - Save to file")
      print("     l - Load from file")
      print("     0 - Exit")
      print()


#------------------------------------------------------------------------------
def main():

    while running:
        try:

            menu = {
                  '1':  print_phonebook,
                  '2':  print_phonebook_by_age,
                  '3':  add_entry_phonebook,
                  '4':  find_entry_name_phonebook,
                  '5':  find_entry_age_phonebook,
                  '6':  delete_entry_name_phonebook,
                  '7':  count_all_entries_in_phonebook,
                  '8':  avr_age_of_all_persons,
                  '9':  increase_age,
                  '10': automatic_increase_age,

                  '0':  exit,
                  's':  save_to_file,
                  'l':  load_from_file,
            }

            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()

        except Exception as ex:
            printError("Something went wrong. Try again...")


#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()