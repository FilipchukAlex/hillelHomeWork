# Swapping the name and surname
name = "Mark Zuckerberg"
name_new = name.split(" ")
name_new = name_new[1], name_new[0]
name_new = ' '.join(name_new)
print(name_new)
