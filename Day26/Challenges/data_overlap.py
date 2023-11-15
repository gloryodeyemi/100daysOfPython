def read_file(file):
    with open(file) as file:
        contents = file.readlines()
    return contents


def modify_file_list(file_list):
    modified_list = [int(num.strip()) for num in file_list]
    return modified_list


file1 = read_file("file1.txt")
modified_list1 = modify_file_list(file1)
# print(modified_file1)

file2 = read_file("file2.txt")
modified_list2 = modify_file_list(file2)
# print(modified_file2)

result = [num for num in modified_list1 if num in modified_list2]
# result = [int(num) for num in file1 if num in file2]
# Write your code above 👆
print(result)
