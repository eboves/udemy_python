"""
Day 33 - API

Description:
Working with API, using the International Space Station API

"""
import requests
from tkinter import *
import datetime as dt

########################################### THIS IS FOR THE ISS ###########################################
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# lon = data["iss_position"]['longitude']
# lat = data["iss_position"]['latitude']
# position = (lon,lat)
# print(position)



########################################### This is getting Kanye quotes ###########################################
# def get_quote():
#     response = requests.get('https://api.kanye.rest')
#     response.raise_for_status()

#     data = response.json()['quote']
#     canvas.itemconfig(quote_text, text=data)

# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="/Users/elvisboves/Desktop/projects/python/Angela_Yu/udemy_python/Day-033/resources/background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="/Users/elvisboves/Desktop/projects/python/Angela_Yu/udemy_python/Day-033/resources/kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)

# window.mainloop()



########################################### This is for the ISS using datetime and a different API ###########################################
# date = dt.datetime.now()
# now = date.now()

# MY_LAT = 27.664827
# MY_LNG = -81.515755


# parameters = {
#     'lat':MY_LAT,
#     'lng':MY_LNG,
#     'formatted': 0,
# }


# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()

# data = response.json()
# sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
# sunset = data['results']['sunset'].split("T")[1].split(":")[0]
# print(sunrise)
# print(sunset)


########################################### This is for the ISS using datetime and sunrise/sunset to know how far is from me ###########################################

MY_LAT = 27.664827
MY_LNG = -81.515755

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

# print("Fetching data...")
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# iss_latitude = 31.459643
# iss_longitude = -80.948332
# print(iss_latitude, iss_longitude)


#create a function that returns True if ISS is nearby and False if is not. if True and is dark, then send email


#Your position is within +5 or -5 degrees of the ISS position. between 22.66 to 33.66 and -76.51 to -86.51


def with_in_range():

    global MY_LAT, MY_LNG, iss_latitude, iss_longitude

    lat_down = MY_LAT - 5
    lat_upper = MY_LAT + 5
    lng_down = MY_LNG - 5
    lng_upper = MY_LNG + 5

    if (lat_down < iss_latitude < lat_upper) and (lng_down < iss_longitude < lng_upper):
        return True
    
    return FALSE

# print(with_in_range())

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise, "sunrise")
print(sunset, "sunset")

time_now = dt.datetime.now()
print(time_now)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.








