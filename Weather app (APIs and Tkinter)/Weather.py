
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import requests


key = 'de9e19a4981d42f7b7b143816230305'

def find_icon_num(icon_url):
    numstr = icon_url[icon_url.rfind("/") + 1:icon_url.rfind("/")+ 4]
    return numstr


def weather(city):
    url = f'http://api.weatherapi.com/v1/current.json?key={key}&q={city}'
    response = requests.get(url)

    if response.status_code != 200:
        return None
    
    data = response.json()

    country = data["location"]["country"]
    city = data["location"]["name"]
    condition_text = data["current"]["condition"]["text"]
    icon_num = find_icon_num(data["current"]["condition"]["icon"])
    is_day = bool(data["current"]["is_day"])
    day_or_night = "day" if is_day else "night"
    tempc = data["current"]["temp_c"]
    feels_like = data["current"]["feelslike_c"]
    percip_mm = data["current"]["precip_mm"]

    info = {
        'city':city,
        'country':country,
        'condition':condition_text,
        'day/night':day_or_night,
        'icon num': icon_num,
        'temp':tempc,
        'feels_like':feels_like,
        'percip_mm':percip_mm
    }

    return info

def search():
    city = city_text.get()
    weather_info = weather(city)

    if weather_info:
        location_lbl['text'] = f'{weather_info["city"]}, {weather_info["country"]}'
        temp_lbl['text'] = f'{weather_info["temp"]} \u00b0C'
        weather_lbl['text'] = weather_info["condition"]
        
        #important to change and add images
        img = PhotoImage(file=f'{weather_info["day/night"]}\{weather_info["icon num"]}.png')
        image.config(image=img)
        image.image = img

    else:
        messagebox.showerror("Error", "Cannot find city, please check spelling or enter another city name")
        



app = Tk()
app.title("Weather App")

app.geometry('350x300')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()


search_btn = Button(app, text = "Search", width = 16, command = search)
search_btn.pack()

location_lbl = Label(app, text = '', font = ('bold', 16))
location_lbl.pack(pady=10)

#to work with images
blank_image = PhotoImage(width=1, height=1)
image = Label(app, image=blank_image)
image.pack()

weather_lbl = Label(app, text = '', font = 14)
weather_lbl.pack(pady=8)

temp_lbl = Label(app, text = '', font = 14)
temp_lbl.pack(pady=4)


#add lbl for feels like and percipitation mm

app.mainloop()