import smtplib
import requests
from datetime import datetime
import math

MY_LAT = 40.726390  # Your latitude
MY_LONG = -73.861480  # Your longitude
YAHOO_SMTP = "smtp.mail.yahoo.com"
PLACEHOLDER = "[NAME]"

dest_email = "alexfeldberg95@gmail.com"
yahoo_email = "alexfeldberg@yahoo.com"
password = "waxxnywdwgaqqpky"


# Your position is within +5 or -5 degrees of the ISS position.
def iss_nearby():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if math.fabs(iss_latitude - MY_LAT) <= 5 and math.fabs(iss_longitude - MY_LONG):
        return True
    return False


def is_night():
    # "formatted" - Gives time in 24hr format
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True

    return False


# If the ISS is close to my current position and it is currently dark
if iss_nearby() and is_night():
    # Then send me an email to tell me to look up.
    print("trying to send email!")
    with smtplib.SMTP(YAHOO_SMTP) as connection:
        connection.starttls()
        connection.login(user=yahoo_email, password=password)
        connection.sendmail(
            from_addr=yahoo_email,
            to_addrs=dest_email,
            msg="Subject:Look up!\n\nISS above! Look up!".encode("UTF-8")
        )

# BONUS: run the code every 60 seconds.
