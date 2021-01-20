import requests
import os
from twilio.rest import Client

MY_LAT = 40.726390  # Your latitude
MY_LONG = -73.861480  # Your longitude
api_key = "7ee103a5337bd67ccbce5f1ca9090101"
account_sid = "ACe4331a112d51a273a84d5eff6008cfac"
auth_token = "96c190f4e3e03495340eb3acfb4767e7"

weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key

}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_parameters)
weather_data = response.json()
print(weather_data)
condition_code = []
will_rain = False
for day in range(12):
    condition_code = weather_data["hourly"][day]["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+17188699083",
        from_="+16204224537",
        body="It's going to rain today! Bring your umbrella.")


