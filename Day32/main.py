import smtplib

my_email = "glowcodes01@gmail.com"
password = "abc1234"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="glowcodes@yahoo.com")

