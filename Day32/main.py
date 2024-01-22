import smtplib
import datetime as dt

my_email = "glowcodes01@gmail.com"
password = "ykefpbnmrbibdgyb"

# GMAIL
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="glowcodes@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

# YAHOO
my_yahoo_email = "glowcodes@yahoo.com"
yahoo_password = "***************"  # currently not available

# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_yahoo_email, password=yahoo_password)
#     connection.sendmail(
#         from_addr=my_yahoo_email,
#         to_addrs="glowcodes01@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

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
