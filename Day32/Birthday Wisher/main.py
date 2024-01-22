import datetime as dt
import email_sender
import pandas as pd
import random

# read the Birthday.csv file
birthdays = pd.read_csv("birthdays.csv")

# check if today matches a birthday in the birthdays.csv
current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day

# loop through the birthday data
for index, items in birthdays.iterrows():
    if items.values[3] == current_month and items.values[4] == current_day:
        name = items.values[0]  # get the name
        email_address = items.values[1]  # get the email address
        random_number = random.randint(1, 3)  # generate a random number for the letter

        # open the random letter file
        with open(f"letter_templates/letter_{random_number}.txt") as letter_file:
            letter = letter_file.readlines()
        letter_string = "".join(letter)
        updated_letter = letter_string.replace("[NAME]", name)

        # send the email
        email_sender.send_using_gmail(f"Happy Birthday, {name}!", updated_letter, to_email=email_address)
    else:
        pass
