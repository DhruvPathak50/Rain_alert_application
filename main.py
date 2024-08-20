import requests
import os
from twilio.rest import Client
api_key = "5400830134329803de88aa3cea72a5ad"
account_sid = 'AC95cdd9f1d4890234ff9d373ad575670d'
auth_token = '31dbb11c21aac68febc3c6084ac48aa1'

param = {
    "lat":18.461620,
    "lon":73.850533,
    "appid":"5400830134329803de88aa3cea72a5ad",
    "cnt":4
}

with requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=param) as conn:
    conn.raise_for_status()
    data = conn.json()
    for hour_data in data["list"]:
        weather_code = hour_data["weather"][0]["id"]
        if weather_code < 700:
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body= "It's going to rain today. Remember to bring an ☂️",
                from_='+12566459426',
                to='+919075251630'
            )

            print(message.status)
            break
