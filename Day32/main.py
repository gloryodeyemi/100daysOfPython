import datetime as dt
import email_sender

# GMAIL
email_sender.send_using_gmail("Hello", "This is the body of the email.")

# YAHOO
# email_sender.send_using_yahoo("Hello", "This is the body of the email.")

# DATETIME
now = dt.datetime.now()
print(f"Current datetime: {now}")
year = now.year
print(f"Current year: {year}")
month = now.month
print(f"Current month: {month}")
weekday = now.weekday()
print(f"Current weekday: {weekday}")

date_of_birth = dt.datetime(year=2010, month=8, day=8)
print(f"My date of birth is: {date_of_birth}")
