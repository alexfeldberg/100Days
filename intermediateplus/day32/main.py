##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas

GMAIL_SMTP = "smtp.gmail.com"
YAHOO_SMTP = "smtp.mail.yahoo.com"
PLACEHOLDER = "[NAME]"

yahoo_email = "alexfeldberg@yahoo.com"
password = "waxxnywdwgaqqpky"
data = pandas.read_csv("birthdays.csv")


# Testing dates
# curr_date = 12
# curr_month = 3

curr_date = dt.datetime.now().day
curr_month = dt.datetime.now().month
dest_email = ""
for index, row in data.iterrows():
    if curr_date == row["day"] and curr_month == row["month"]:
        # print(f"It is {row['name']}'s BIRTHDAY!")
        dest_email = row["email"]
        letter_num = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_num}.txt") as starting_letter:
            letter = starting_letter.read()
            bday_letter = letter.replace(PLACEHOLDER, row["name"])
            print(bday_letter)


with smtplib.SMTP(YAHOO_SMTP) as connection:
    connection.starttls()
    connection.login(user=yahoo_email, password=password)
    connection.sendmail(
        from_addr=yahoo_email,
        to_addrs=dest_email,
        msg=((f"Subject:Happy Birthday!\n\n{bday_letter}").encode("UTF-8"))
    )







