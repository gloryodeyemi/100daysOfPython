import smtplib
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access the environment variables
FROM_EMAIL = os.getenv('EMAIL_ADDRESS')
T0_EMAIL = os.getenv('TO_EMAIL')
PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_ADDRESS = os.getenv('SMTP_ADDRESS')


# Function to send email
def send_using_gmail(subject, body, from_email=FROM_EMAIL, to_email=T0_EMAIL):
    with smtplib.SMTP(SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=from_email, password=PASSWORD)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=f"Subject:{subject}\n\n{body}".encode('utf-8')
        )


# Scrape the Amazon product page
product_url = "https://appbrewery.github.io/instant_pot/"
response = requests.get(product_url)

amazon_page = response.text
soup = BeautifulSoup(amazon_page, "html.parser")
print(soup.prettify())

# Get the price
product_price = float(soup.select_one("span.a-price span.a-offscreen").getText().strip('$'))
print(f"Here is the price:\n{product_price}\n")

# product_title = soup.select_one("span#productTitle")
product_title = soup.find("span", id="productTitle").getText().split()
product_title = ' '.join(product_title)
print(f"Here is the product title:\n{product_title}")

target_price = 100.00
email_message = f"{product_title} is now ${product_price}. Go grab it asap!!!\n{product_url}"
print(email_message)

# Send email when product_price is below target price
if product_price < target_price:
    try:
        send_using_gmail(
            subject="Amazon Low Price Alert!",
            body=email_message
        )
    except Exception as e:
        print(f"Failed to send email: {e}")
    else:
        print("Email sent successfully!")
