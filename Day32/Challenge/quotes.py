import datetime as dt
import random
from email_sender import send_using_gmail

# getting the file
with open("quotes.txt", "r") as quotes_file:
    quotes_list = quotes_file.readlines()
    random_quote = random.choice(quotes_list)
    print(f"Length of quotes: {len(quotes_list)}\nSample quote: {random_quote}")

# getting the current weekday
current_date = dt.datetime.now()
current_weekday = current_date.weekday()
print(f"The current weekday is: {current_weekday}")

# sending the email
if current_weekday == 0:
    send_using_gmail("Weekly Motivation", random_quote)
else:
    print("I am not a monday")
