import smtplib

MY_EMAIL = "glowcodes01@gmail.com"
PASSWORD = "ykefpbnmrbibdgyb"
MY_YAHOO_EMAIL = "glowcodes@yahoo.com"
YAHOO_PASSWORD = "***************"  # currently not available


# GMAIL
def send_using_gmail(subject, body):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="glowcodes@yahoo.com",
            msg=f"Subject:{subject}\n\n{body}"
        )


# YAHOO
def send_using_yahoo(subject, body):
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MY_YAHOO_EMAIL, password=YAHOO_PASSWORD)
        connection.sendmail(
            from_addr=MY_YAHOO_EMAIL,
            to_addrs="glowcodes01@gmail.com",
            msg=f"Subject:{subject}\n\n{body}"
        )
