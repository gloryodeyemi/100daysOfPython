import smtplib

MY_EMAIL = "glowcodes01@gmail.com"
PASSWORD = "*****************"
MY_YAHOO_EMAIL = "glowcodes@yahoo.com"
YAHOO_PASSWORD = "***************"  # currently not available


# GMAIL
def send_using_gmail(subject, body, from_email=MY_EMAIL, to_email=MY_YAHOO_EMAIL):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=from_email, password=PASSWORD)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=f"Subject:{subject}\n\n{body}"
        )


# YAHOO
def send_using_yahoo(subject, body, from_email=MY_YAHOO_EMAIL, to_email=MY_EMAIL):
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=from_email, password=YAHOO_PASSWORD)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=f"Subject:{subject}\n\n{body}"
        )
