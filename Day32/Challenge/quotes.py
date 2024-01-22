import smtplib
import datetime as dt
import random

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
my_email = "glowcodes01@gmail.com"
password = "ykefpbnmrbibdgyb"

# GMAIL
if current_weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="glowcodes@yahoo.com",
            msg=f"Subject:Weekly Motivation\n\n{random_quote}"
        )
else:
    print("I am not a monday")
