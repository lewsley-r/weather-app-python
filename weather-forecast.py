import requests
import os
import tkinter as tk
from dotenv import load_dotenv
from tkinter.simpledialog import askstring
from tkinter import *

def get_weather_data():
    city = askstring("Input", "Enter you City")
    url = "http://api.weatherapi.com/v1/forecast.json?key={}&q={}&days=7&aqi=no&alerts=no".format(api_key, city)
    response = requests.get(url).json()
    return response


def get_todays_weather():
    today_data = weather_data['forecast']['forecastday'][0]['day']
    today_date = weather_data['forecast']['forecastday'][0]['date']
    listbox.delete(0,END)
    list_items = ['Date: '+ today_date,
                  'Condition: '+ today_data['condition']['text'], 
                  'Avg Temp (C): '+str(today_data['avgtemp_c']),
                  'Max Wind (MPH): '+ str(today_data['maxwind_mph']),
                  'Avg Humidity(%): '+str(today_data['avghumidity'])]
    listbox.insert(1, 'City: Belfast')
    list_counter = 2
    for (item) in list_items:
        listbox.insert(list_counter, item)
        list_counter+=1


def get_x_day_weather(x):
    x_day_data = weather_data['forecast']['forecastday'][0:x]
    
    listbox.delete(0,END)
    listbox.insert('end', 'City: Belfast')
    listbox.insert('end', '\n\n')
    for day in x_day_data:
        list_items = ['Date: '+ day['date'],
                    'Condition: '+ day['day']['condition']['text'], 
                    'Avg Temp (C): '+str(day['day']['avgtemp_c']),
                    'Max Wind (MPH): '+ str(day['day']['maxwind_mph']),
                    'Avg Humidity(%): '+str(day['day']['avghumidity']),
                    '\n']
        for (item) in list_items:
            print (item)
            listbox.insert('end', item)


load_dotenv()
api_key = os.environ["API_KEY"]
top = Tk()
top.geometry("300x300")
listbox = Listbox(top, height = 10, 
                width = 40, 
                bg = "grey",
                activestyle = 'dotbox', 
                font = "Helvetica",
                fg = "yellow")

weather_data = get_weather_data()
todays_weather = Button(top, text = "Today's weather", command = get_todays_weather)
todays_weather.pack(fill=tk.X)
three_day_weather = Button(top, text = "Three day weather forecast", command = lambda:get_x_day_weather(3))
three_day_weather.pack(fill=tk.X)
seven_day_weather = Button(top, text = "Seven day weather forecast", command = lambda:get_x_day_weather(7))
seven_day_weather.pack(fill=tk.X)
listbox.pack()
top.mainloop()
