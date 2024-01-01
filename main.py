import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "123564465465484351251685351jksfsfs"
account_sid = "AC43e3d4429ce678f161e5509223e28bdb"
auth_token = "sagafkjvdsrg548d65z4v8d4gff65sdfs3s"

weather_params = {
    "lat":3.139003,
    "lon":101.686852,
    "appid": api_key,
    "cnt":4,
}
will_rain = False
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_='+16502413241',
        to='+601167602964'
    )
    print(message.status)