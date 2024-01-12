# Error handling
try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict['key'])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:  # runs if there are no exceptions
    content = file.read()
    print(content)
finally:  # runs no matter what happens
    file.close()
    print("The file was closed.")
    # raise TypeError("This is an error I made up.")

# Sample raise error - Calculating BMI
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(f"BMI = {bmi:.2f}")

# KeyError
# a_dict = {"key": "value"}
# value = a_dict['non_existent_key']

# IndexError
# fruit_list = ['Apple', 'Banana', 'Pear']
# fruit = fruit_list[3]

# TypeError
# text = 'abc'
# print(text + 5)
