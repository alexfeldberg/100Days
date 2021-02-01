import requests
from datetime import datetime as dt

USERNAME = "alexfeldberg"
TOKEN = "tGv01DLN2"

GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# Create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Meditation Graph",
    "unit": "Mins",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = dt.now()

post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you meditate for today?")
}

# Create pixel
response = requests.post(url=pixel_endpoint, json=post_params, headers=headers)
print(response.text)

# Update color to blue, was initially yellow
# response = requests.put(url=pixel_endpoint, json={"color": "sora"}, headers=headers)
# print(response.text)

# Update value after posting it
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.put(url=update_endpoint, json={"quantity": "15"}, headers=headers)
# print(response.text)

# Delete pixel
# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)
