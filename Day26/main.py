import random
import pandas as pd

# list comprehension
print("List Comprehension\n------------------")
numbers = [1, 2, 3]

new_list = [n + 1 for n in numbers]
print(f"Previous list: {numbers}\nNew list: {new_list}")

name = "Glory"
letters_list = [letter for letter in name]
print(f"Name list: {letters_list}")

# Python sequences - list, range, tuple, dictionary.

doubled_numbers = [num * 2 for num in range(1, 5)]
print(f"Doubled numbers list: {doubled_numbers}")

# conditional list comprehension - new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
print(f"Short names: {short_names}")

long_names = [name.upper() for name in names if len(name) >= 5]
print(f"Long names: {long_names}\n")

# dictionary comprehension
print("Dictionary Comprehension\n------------------------")

score_dict = {name: random.randint(1, 100) for name in names}
print(f"Student scores: {score_dict}")

# conditional dictionary comprehension
passed_students = {student: score for (student, score) in score_dict.items() if score >= 60}
print(f"Passed students: {passed_students}\n")

# looping through a dictionary
print("Looping through a dictionary\n----------------------------")
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(f"{key}: {value}")

# iterate over a Pandas DataFrame
print("\nLooping through a DataFrame\n---------------------------")
student_df = pd.DataFrame(student_dict)
print(f"Student DataFrame:\n{student_df}\n")

for (index, row) in student_df.iterrows():
    print(f"Index {index}:\n{row}\n")
    print(f"Student: {row.student}\nScore: {row.score}\n")
