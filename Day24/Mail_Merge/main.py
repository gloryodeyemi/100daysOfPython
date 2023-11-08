# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# get the list of invited names
with open("./Input/Names/invited_names.txt") as names:
    invited_names = names.readlines()

# get the contents of the letter
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.readlines()

# create individual letters for each name
for name in invited_names:
    with open(f"./Output/ReadyToSend/letter_for_{name.strip()}", 'a') as updated_letter:
        for line in letter_contents:
            updated_letter.write(line.replace("[name]", name.strip()))
