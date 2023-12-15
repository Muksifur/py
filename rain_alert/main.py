import requests
from twilio.rest import Client

account_sid = 'AC4553896ec9e1e5cd9689e37fe10f73d4'
auth_token = '05fa47c5baadd2d4c57849d23c7ada9a'
LAT = 68
LNG = 129
ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
KEY = "0cbc98c8742761987d2c9876ba56bfde"
PARAMETERS = {
    "lat": LAT,
    "lon": LNG,
    "appid": KEY,
    "units": "metric",
    "exclude": "current,minutely,daily"
}

response = requests.get(url=ENDPOINT, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    code = hour_data["weather"][0]["id"]
    if code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+12512374828',
        body="It will rain today. Bring an Umbrella.",
        to='+8801602121225'
    )
    print(message.sid)




