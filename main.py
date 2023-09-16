# numbers = [1, 2, 3]
# new_list = [n+1 for n in numbers]
# print(new_list)

# name = ["sanjay"]
# new_letter = [letter for letter in name]
# print(new_letter)

names = ["sanjay", "praba", "ila", "magesh"]
short_names = [name for name in names if len(name) <= 5]

larger_names = [name for name in names if len(name) >= 5]

largest_names = [name.upper()   for name in names if len(name) >= 5]
print(largest_names)