from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from configparser import ConfigParser
import requests

app = Tk()
app.title("Weather App")
app.geometry("700x350")

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json["name"]
        country = json['sys']['country']
        temp_kelvin = json["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin - 273.15)*9/5+32
        weather = json['weather'][0]['main']
        icon = json['weather'][0]['icon']
        final = (city,country,temp_kelvin,temp_celsius,temp_fahrenheit,weather,icon)
        return final
    else:
        return None


def search():
    global image
    city = city_name.get()
    weather = get_weather(city)
    if weather:
        location_entry.insert(15, str('{},{}'.format(weather[0],weather[1])))
        temp_entry.insert(10,str('{:.2f}°K'.format(weather[2])))
        tempc_entry.insert(15,str('{:.2f}°C'.format(weather[3])))
        tempf_entry.insert(15,str('{:.2f}°F'.format(weather[4])))
        weather_entry.insert(15,str('{}'.format(weather[5])))
        image["bitmap"]='weather_icons/{}@2x.png'.format(weather[6])
    else:
        messagebox.showerror("Error","city not found {}".format(city))

def clear():
    location_entry.delete(0, END)
    temp_entry.delete(0, END)
    tempc_entry.delete(0, END)
    tempf_entry.delete(0, END)
    weather_entry.delete(0, END)
    city_name_entry.focus_set()

my_font = Font(family = "Comic Sans Ms", size = 20, underline = 1)
title_label = Label(app,text="LIVE WEATHER GUI APP", font = my_font, bg ="#efefef", fg="green")
title_label.place(x=0, y=0, relwidth = 1)

city_name = StringVar()
city_label  =Label(app, text="CITY NAME:",font =("Comic Sans Ms",10,"bold"),fg = "green")
city_label.place(x=220,y=50)
city_name_entry = Entry(app, textvariable = city_name)
city_name_entry.place(x=350,y=50)

search_button = Button(app, text="SEARCH",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg = "green",command=search)
search_button.place(x=315,y=80)

location_label = Label(app,text="LOCATION :",font =("Comic Sans Ms",10,"bold"),fg = "green")
location_label.place(x=220,y=130)
location_entry = Entry(app)
location_entry.place(x=350,y=130)

image = Label(app,bitmap='')
image.place(x=550,y=150)

temp_label = Label(app, text="TEMP IN °K :",font =("Comic Sans Ms",10,"bold"),fg = "green")
temp_label.place(x=220,y=170)
temp_entry = Entry(app)
temp_entry.place(x=350,y=170)

tempc_label = Label(app, text="TEMP IN °C :",font =("Comic Sans Ms",10,"bold"),fg = "green")
tempc_label.place(x=220,y=210)
tempc_entry = Entry(app)
tempc_entry.place(x=350,y=210)

tempf_label = Label(app, text="TEMP IN °F:",font =("Comic Sans Ms",10,"bold"),fg = "green")
tempf_label.place(x=220,y=240)
tempf_entry = Entry(app)
tempf_entry.place(x=350,y=240)

weather_label=Label(app,text="WEATHER :",font =("Comic Sans Ms",10,"bold"),fg = "green")
weather_label.place(x=220,y=270)
weather_entry = Entry(app)
weather_entry.place(x=350,y=270)

clear_button = Button(app, text="CLEAR",font=("Comic Sans Ms",10),bg ="#efefef",bd=5,fg = "green",command=clear)
clear_button.place(x=315,y=300)


app.mainloop()
