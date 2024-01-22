import smtplib

my_email = "glowcodes01@gmail.com"
password = "ykefpbnmrbibdgyb"

# GMAIL
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="glowcodes@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )

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
