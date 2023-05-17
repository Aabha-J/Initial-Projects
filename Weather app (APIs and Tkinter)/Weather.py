
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import requests
from autocorrect import Speller


key = 'insert your key here'

def find_icon_num(icon_url):
    numstr = icon_url[icon_url.rfind("/") + 1:icon_url.rfind("/")+ 4]
    return numstr

def correct_spelling(city_name):
  spell = Speller(lang='en')
  corrected_name = spell(city_name)
  return corrected_name

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

def search(city):
  weather_info = weather(city)
  if weather_info:
      location_lbl['text'] = f'{weather_info["city"]}, {weather_info["country"]}'
      temp_lbl['text'] = f'{weather_info["temp"]} \u00b0C'
      weather_lbl['text'] = weather_info["condition"]

      file = f'{weather_info["day/night"]}/{weather_info["icon num"]}.png'
      
      img = PhotoImage(file=file)
      image.config(image=img)
      image.image = img

  else:
    correction = correct_spelling(city)
    if correction == city or correction == None:
      messagebox.showerror("Error", "Cannot find city, please check spelling or enter another city name")
    else:
      search(correction)

        



app = Tk()
app.title("Weather App")

app.geometry('350x500')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()


search_btn = Button(app, text="Search", width=16, command=lambda: search(city_text.get()))
search_btn.pack()

app.bind('<Return>', lambda event: search(city_text.get()))

location_lbl = Label(app, text = '', font = ('bold', 14),wraplength=300)
location_lbl.pack(pady=10)

#to work with images
blank_image = PhotoImage(width=1, height=1)
image = Label(app, image=blank_image)
image.pack()

weather_lbl = Label(app, text = '', font = 14)
weather_lbl.pack(pady=2)

temp_lbl = Label(app, text = '', font = 14)
temp_lbl.pack(pady=4)


app.mainloop()
