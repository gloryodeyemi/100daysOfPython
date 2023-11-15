list_of_strings = input().split(',')  # input = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# 🚨 Do  not change the code above

# TODO: Use list comprehension to convert the strings to integers 👇:
list_of_integers = [int(num) for num in list_of_strings]

# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [even_num for even_num in list_of_integers if even_num % 2 == 0]

# Write your code 👆 above:
print(result)
