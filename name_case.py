'''
hello comments

'''
person_name = (input("hey what is your name? ")).strip().lower()
print(f"thanks {person_name}")
split_name = person_name.split()
print(split_name)
print(len(split_name))
name1 = split_name[0]
print(len(name1))
print([*name1])

print("SUPPPERR")