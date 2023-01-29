import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 26.9096951 # Your latitude
MY_LONG = 75.818504 # Your longitude

MY_EMAIL = "<Your email ID>"
PW = "<your 2FA application password>"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT +5 and MY_LONG -5 <= iss_longitude <= MY_LONG +5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
while True:               #this block of code inside the while loop will continue on running
    time.sleep(60)        #this block of code will run every 60 seconds
    if is_iss_overhead:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= MY_EMAIL, password= PW)
            connection.sendmail(
                from_addr= MY_EMAIL,
                to_addrs= "<reciever's email address>",
                msg= "Subject: Look up \n\nThe ISS is above you in the sky."
            )

