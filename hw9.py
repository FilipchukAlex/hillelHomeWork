# Snake style to Camelized style
name_snake_syle = "employee_first_name"
name_temp = name_snake_syle.split('_')
name_camelized_style = name_temp[0].capitalize() + name_temp[1].capitalize() + name_temp[2].capitalize()
print("Snake style:", name_snake_syle)
print("Camelized style:", name_camelized_style)