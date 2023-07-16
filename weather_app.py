#This weather app is made with the OpenWeatherMap API

import requests
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from io import BytesIO

class SkyCast:
    api_key = 'd078dfc0e65a5b6f60dddd88900e35e7'

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SkyCast - Your Weather Forecasting App")
        self.root.geometry("400x400")

        self.input_label = tk.Label(self.root, text="Enter city name ", font=('Inter, 18'))
        self.input_label.pack(padx=20, pady=20)

        self.city = tk.Entry(self.root)
        self.city.pack()

        self.submit_button = tk.Button(self.root, text="Get weather", command = self.get_weather)
        self.submit_button.pack(padx=10, pady=10)

        self.icon_label = tk.Label(self.root)
        self.icon_label.pack()

        self.result = tk.Text(self.root)
        self.result.pack()

        self.root.mainloop()

    def get_weather(self):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={self.city.get()}&appid={SkyCast.api_key}'
        response = requests.get(url)  # stores weather data fetched

        if response.status_code == 200:  # status code 200: request has succeeded
            data = response.json()  # extracts JSON data from response and stores in data as a dictionary
            temp = data['main']['temp']
            tempC = temp - 273.15
            tempF = tempC * (9 / 5) + 32
            desc = data['weather'][0]['description']
            icon = data['weather'][0]['icon']

            icon_url = f'http://openweathermap.org/img/wn/{icon}.png'
            response_icon = requests.get(icon_url)

            if response_icon.status_code == 200:
                icon_data = response_icon.content
                icon_image = Image.open(BytesIO(icon_data))
                icon_photo = ImageTk.PhotoImage(icon_image)
                self.icon_label.configure(image=icon_photo)
                self.icon_label.image = icon_photo
                self.icon_label.pack()
            else:
                messagebox.showerror("Error", "Error fetching icon")

            #icon_url = f'http://openweathermap.org/img/w/ {icon}.png'
            #response_icon = requests.get(icon_url)

            self.result.delete('1.0', tk.END)

            self.result.insert(tk.END, f'temperature: {temp} K\n')
            self.result.insert(tk.END, f'temperature: {tempC:.2f} °C\n')
            self.result.insert(tk.END, f'temperature: {tempF:.2f} °F\n')
            self.result.insert(tk.END, f'Description: {desc} \n')
            #self.result.insert(tk.END, f'{img}')

        else:
            messagebox.showerror("Error", 'Error fetching weather data')

SkyCast()





