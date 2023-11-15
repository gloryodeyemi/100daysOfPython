# list comprehension
numbers = [1, 2, 3]

new_list = [n + 1 for n in numbers]
print(f"Previous list: {numbers}\nNew list: {new_list}\n")

name = "Glory"
letters_list = [letter for letter in name]
print(f"Name list: {letters_list}\n")

# Python sequences - list, range, tuple, dictionary.

doubled_numbers = [num * 2 for num in range(1, 5)]
print(f"Doubled numbers list: {doubled_numbers}\n")

# conditional list comprehension - new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
print(f"Short names: {short_names}\n")

long_names = [name.upper() for name in names if len(name) >= 5]
print(f"Long names: {long_names}\n")
