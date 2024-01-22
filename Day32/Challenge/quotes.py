import smtplib
import datetime as dt
import random

# getting the file
with open("quotes.txt", "r") as quotes_file:
    quotes_list = quotes_file.readlines()
    print(f"Length of quotes: {len(quotes_list)}\nSample quote: {random.choice(quotes_list)}")

#
