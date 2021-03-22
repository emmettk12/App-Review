import tkinter as tk
import requests


import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str

def get_weather(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)

def tempForDrink(temp):
    if (temp<=40):
        drink="Get a hot drink"
       # return(drink)
    elif (temp>=41) and (temp<=60):
        drink="Get a  warm team"
        #print(drink)
    elif (temp>=61) and (temp<=80):
        drink="Get a  ice coffee"
        #print(drink)
    elif (temp>=81) and (temp<=100):
        drink="Get a  iced sweet tea"
        #print(drink)
    else:
        drink="Get ice cream"
        #print(drink)
    label['text'] = drink

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#background_image = tk.PhotoImage(file='landscape.png')
#background_label = tk.Label(root, image=background_image)
#background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

button1 = tk.Button(frame, text="Drink", font=40, command=lambda: tempForDrink(40))
button1.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()


