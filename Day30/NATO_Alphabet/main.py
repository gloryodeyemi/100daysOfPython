import pandas as pd

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_alphabet = pd.read_csv('nato_phonetic_alphabet.csv')  # read NATO alphabet csv file
print(f"NATO Alphabet DataFrame:\n------------------------\n{nato_alphabet.head()}\n")

nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
print(f"NATO Alphabet Dictionary:\n-------------------------\n{nato_alphabet_dict}\n")

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ")

while KeyError:
    try:
        nato_list = [nato_alphabet_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        user_input = input("Enter a word: ")
    else:
        print(f"NATO code for {user_input}: {nato_list}")
        break
