# option 1
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# option 2
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# write to a file
with open("my_file.txt", 'w') as file:
    file.write("I am a new text.")

# add to a file
with open("my_file.txt", 'a') as file:
    file.write("\nI am another text.")

# create a new file
with open("new_file.txt", 'w') as file:
    file.write("I am a new file.")
