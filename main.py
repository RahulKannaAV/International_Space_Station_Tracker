import requests
import datetime as dt
import smtplib
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

resp = requests.get(url="http://api.open-notify.org/iss-now.json")
json_rep = resp.json()

my_email = "email" # your email id
passw = "password" # your password

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=passw)

latitude = json_rep['iss_position']['latitude']
longitude = json_rep['iss_position']['longitude']

position_iss = (latitude, longitude)

LATITUDE = 13.082680
LONGITUDE = 80.270721

prams = {
    'formatted':0
}

disable_warnings(InsecureRequestWarning)


sunset_req = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={LATITUDE}&lng={LONGITUDE}", verify=False, params=prams)
data = sunset_req.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

td = dt.datetime
time = td.now()

if abs(float(latitude)-LATITUDE) <= 5 and abs(float(longitude)-LONGITUDE) <= 5 and int(time.hour) >= int(sunset) and int(time.hour) <= int(sunrise):
    connection.sendmail(from_addr=my_email, to_addrs="other_email_id",
                        msg="Look up the Sky. You may find something interesting (Not ISS). Just Kidding.")
