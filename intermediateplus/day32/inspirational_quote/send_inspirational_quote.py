import smtplib
import datetime as dt
import random

GMAIL_SMTP = "smtp.gmail.com"
YAHOO_SMTP = "smtp.mail.yahoo.com"

yahoo_email = "alexfeldberg@yahoo.com"
password = "waxxnywdwgaqqpky"

weekday = dt.datetime.now().weekday()
if weekday == 4:

    with open("inspirational_quote/quotes.txt") as quotes:
        data = quotes.readlines()
        friday_quote = random.choice(data)

    with smtplib.SMTP(YAHOO_SMTP) as connection:
        connection.starttls()
        connection.login(user=yahoo_email, password=password)
        connection.sendmail(
            from_addr=yahoo_email,
            to_addrs="alexfeldberg95@gmail.com",
            msg=((f"Subject:Happy Friday! Here's your inspirational quote:\n\n{friday_quote}").encode("UTF-8"))
        )
